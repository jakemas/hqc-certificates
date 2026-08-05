#!/usr/bin/env python3
"""Generate example HQC-KEM public keys and seed-format private keys.

This is the HQC analogue of the Go example generator used for the ML-KEM
(draft-ietf-lamps-kyber-certificates) and ML-DSA drafts. Because no HQC
implementation exists in the Go cloudflare/circl library, the examples here
are produced with the local Python reference implementation `hqc-py` (by
Markku-Juhani O. Saarinen), which follows the 2025-08-22 HQC specification and
performs genuine seed-based key generation.

For each of HQC-KEM-128/192/256 it derives a key pair from a fixed,
deterministic 32-byte seed and writes:

  * <name>.pub        SubjectPublicKeyInfo, PEM "PUBLIC KEY"
  * <name>-seed.priv  OneAsymmetricKey with the seed [0] OCTET STRING CHOICE,
                      PEM "PRIVATE KEY"

Unlike ML-KEM, HQC keys in this draft use the seed as the ONLY private-key
representation, so there are no "expanded" or "both" variants.

NOTE ON OIDs: FIPS 207 has not been published, so the algorithm OIDs are TBD.
Placeholder sub-arcs under the NIST "kems" arc (2.16.840.1.101.3.4.4) are used
purely so the DER encodes and pretty-prints; they are NOT real assignments and
MUST be replaced once NIST/CSOR assigns them.
"""

import os
import sys

# Make the local hqc-py reference implementation importable. Adjust HQC_PY if
# the reference tree lives elsewhere.
HQC_PY = os.environ.get(
    "HQC_PY",
    os.path.join(os.path.dirname(__file__), "..", "..", "reference", "hqc-py"),
)
sys.path.insert(0, os.path.abspath(HQC_PY))

import hqc as H  # noqa: E402


# --- Minimal DER encoder -------------------------------------------------

def _der_len(n):
    if n < 0x80:
        return bytes([n])
    body = b""
    while n:
        body = bytes([n & 0xFF]) + body
        n >>= 8
    return bytes([0x80 | len(body)]) + body


def _tlv(tag, value):
    return bytes([tag]) + _der_len(len(value)) + value


def der_integer(v):
    if v == 0:
        return _tlv(0x02, b"\x00")
    body = b""
    while v:
        body = bytes([v & 0xFF]) + body
        v >>= 8
    if body[0] & 0x80:
        body = b"\x00" + body
    return _tlv(0x02, body)


def der_octet_string(b):
    return _tlv(0x04, b)


def der_bit_string(b):
    # Zero unused bits.
    return _tlv(0x03, b"\x00" + b)


def der_sequence(*elems):
    return _tlv(0x30, b"".join(elems))


def der_oid(arc):
    first = 40 * arc[0] + arc[1]
    body = bytes([first])
    for n in arc[2:]:
        if n == 0:
            body += b"\x00"
            continue
        chunk = []
        while n:
            chunk.insert(0, n & 0x7F)
            n >>= 7
        for i in range(len(chunk) - 1):
            chunk[i] |= 0x80
        body += bytes(chunk)
    return _tlv(0x06, body)


def der_context_primitive(tagno, b):
    # [tagno] PRIMITIVE, context-specific class (0x80).
    return _tlv(0x80 | tagno, b)


def pem(label, der):
    import base64
    b64 = base64.encodebytes(der).decode().replace("\n", "")
    lines = [b64[i:i + 64] for i in range(0, len(b64), 64)]
    return (
        "-----BEGIN {0}-----\n".format(label)
        + "\n".join(lines)
        + "\n-----END {0}-----\n".format(label)
    )


# --- Fixed deterministic seed PRNG for keygen ----------------------------

class SeedReader:
    """Feeds keygen a fixed byte string. keygen reads exactly seed_sz bytes."""

    def __init__(self, seed):
        self.buf = seed
        self.pos = 0

    def read(self, n):
        out = self.buf[self.pos:self.pos + n]
        self.pos += n
        return out


# --- Per-level definitions -----------------------------------------------

# name, hqc-py parameter object, placeholder OID sub-arc value under `kems`.
LEVELS = [
    ("HQC-KEM-128", H.HQC_1, 1),
    ("HQC-KEM-192", H.HQC_3, 2),
    ("HQC-KEM-256", H.HQC_5, 3),
]

# NIST "kems" arc: joint-iso-ccitt(2) country(16) us(840) organization(1)
# gov(101) csor(3) nistAlgorithm(4) kems(4). The final component is a TBD
# PLACEHOLDER, not a real assignment.
KEMS_ARC = (2, 16, 840, 1, 101, 3, 4, 4)


def alg_identifier(oid_tail):
    # AlgorithmIdentifier ::= SEQUENCE { algorithm OID } -- no parameters
    return der_sequence(der_oid(KEMS_ARC + (oid_tail,)))


def example(name, param, oid_tail):
    seed = bytes(range(32))
    ek, dk = param.keygen(SeedReader(seed))

    # Sanity: seedKEM is the last 32 bytes of dk and must equal our input.
    assert dk[-param.seed_sz:] == seed, "seedKEM round-trip mismatch"
    assert len(ek) == param.pk_sz

    alg = alg_identifier(oid_tail)

    # SubjectPublicKeyInfo ::= SEQUENCE { algorithm, subjectPublicKey BIT STRING }
    spki = der_sequence(alg, der_bit_string(ek))

    # OneAsymmetricKey ::= SEQUENCE {
    #   version INTEGER (0),
    #   privateKeyAlgorithm AlgorithmIdentifier,
    #   privateKey OCTET STRING   -- containing the DER of the CHOICE
    # }
    # The privateKey OCTET STRING wraps HQC-KEM-*-PrivateKey, here the
    # seed [0] OCTET STRING alternative.
    inner_choice = der_context_primitive(0, seed)
    oak = der_sequence(
        der_integer(0),
        alg,
        der_octet_string(inner_choice),
    )

    with open("{0}.pub".format(name), "w") as f:
        f.write(pem("PUBLIC KEY", spki))
    with open("{0}-seed.priv".format(name), "w") as f:
        f.write(pem("PRIVATE KEY", oak))

    print(
        "{0}: pk={1}B  dk(seed-form priv payload)=32B  OID tail={2} (PLACEHOLDER)".format(
            name, len(ek), oid_tail
        )
    )


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    for name, param, oid_tail in LEVELS:
        example(name, param, oid_tail)


if __name__ == "__main__":
    main()
