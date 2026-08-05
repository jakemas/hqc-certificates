# HQC-KEM certificate examples

Example `SubjectPublicKeyInfo` public keys and seed-format private keys for
HQC-KEM-128/192/256, the analogue of the ML-KEM examples in
[draft-ietf-lamps-kyber-certificates](https://datatracker.ietf.org/doc/draft-ietf-lamps-kyber-certificates).

## How these are generated

`generate.py` derives a key pair for each level from a fixed, deterministic
32-byte seed (`00 01 02 ... 1f`) and writes:

| File | Contents |
|-|-|
| `HQC-KEM-<lvl>.pub` | `SubjectPublicKeyInfo`, PEM `PUBLIC KEY` |
| `HQC-KEM-<lvl>-seed.priv` | `OneAsymmetricKey` with the `seed [0] OCTET STRING` CHOICE, PEM `PRIVATE KEY` |

Unlike ML-KEM (which offers `seed`, `expanded`, and `both`), HQC uses the seed
as the **only** private-key representation, so there is a single `.priv` per
level.

The generator uses the local [`hqc-py`](../../reference/hqc-py) reference
implementation (M-J. O. Saarinen, 2025-08-22 spec) rather than Go: unlike
ML-KEM/ML-DSA, there is no HQC implementation in `cloudflare/circl`. Point
`HQC_PY` at the reference tree if it lives elsewhere.

```sh
python3 generate.py   # requires pycryptodome (Crypto.Hash) + hqc-py on the path
./pretty              # der2ascii pretty-prints -> *.txt (needs der2ascii)
```

## Caveats (will change once FIPS 207 is final)

- **OIDs are placeholders.** FIPS 207 is not yet published, so the algorithm
  identifiers use TBD sub-arcs under the NIST `kems` arc
  (`2.16.840.1.101.3.4.4`). They encode and pretty-print but are **not** real
  assignments. (`openssl asn1parse` will mislabel `...4.4.1` as `ML-KEM-512`
  because it reuses that arc — ignore that.)
- **Sizes are provisional.** The reference implementation produces public keys
  of 2241 / 4514 / 7237 bytes for levels 1 / 3 / 5. The draft's ASN.1 currently
  states 2249 / 4522 / 7245; these will be reconciled against published
  FIPS 207 values.
- A KEM cannot self-sign, so no example certificate (`.crt`) is produced here;
  only the raw public-key and private-key structures.
