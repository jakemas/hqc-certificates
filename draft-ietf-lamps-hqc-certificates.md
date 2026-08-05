---
title: >
  Internet X.509 Public Key Infrastructure - Algorithm Identifiers
  for the Hamming Quasi-Cyclic Key-Encapsulation Mechanism (HQC)
abbrev: HQC in Certificates
category: std

docname: draft-ietf-lamps-hqc-certificates-latest
submissiontype: IETF
number:
date:
consensus: true
v: 3
area: SEC
workgroup: LAMPS
keyword:
  HQC
  KEM
  Certificate
  X.509
  PKIX
  Post-Quantum
venue:
  group: "Limited Additional Mechanisms for PKIX and SMIME (lamps)"
  type: "Working Group"
  mail: "spasm@ietf.org"
  arch: "https://mailarchive.ietf.org/arch/browse/spasm/"
  github: "jakemas/hqc-certificates"
  latest: "https://jakemas.github.io/hqc-certificates/#go.draft-ietf-lamps-hqc-certificates.html"

author:
 -
    ins: J. Massimo
    name: Jake Massimo
    organization: AWS
    email: jakemas@amazon.com

normative:
  X680:
    target: https://www.itu.int/rec/T-REC-X.680
    title: >
      Information technology - Abstract Syntax Notation One (ASN.1):
      Specification of basic notation
    date: 2021-02
    author:
    -  org: ITU-T
    seriesinfo:
      ITU-T Recommendation: X.680
      ISO/IEC: 8824-1:2021
  X690:
    target: https://www.itu.int/rec/T-REC-X.690
    title: >
      Information technology - Abstract Syntax Notation One (ASN.1):
      ASN.1 encoding rules: Specification of Basic Encoding Rules (BER),
      Canonical Encoding Rules (CER) and Distinguished Encoding Rules (DER)
    date: 2021-02
    author:
    -  org: ITU-T
    seriesinfo:
      ITU-T Recommendation: X.690
      ISO/IEC: 8825-1:2021
  CSOR:
     target: https://csrc.nist.gov/projects/computer-security-objects-register/algorithm-registration
     title: Computer Security Objects Register
     author:
       name: National Institute of Standards and Technology
       ins: NIST
     date: 2024-08-20

informative:
  HQC:
    target: https://pqc-hqc.org/
    title: "HQC: Hamming Quasi-Cyclic"
    author:
      - org: HQC Team
    date: 2025
  NIST-HQC-SELECTION:
    target: https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption
    title: >
      NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption
    author:
    - org: National Institute of Standards and Technology (NIST)
    date: 2025-03-11
  NIST-PQC:
    target: https://csrc.nist.gov/projects/post-quantum-cryptography
    title: >
      Post-Quantum Cryptography Project
    author:
    - org: National Institute of Standards and Technology (NIST)
    date: 2016-12-20
  CDM23:
    title: "Keeping Up with the KEMs: Stronger Security Notions for KEMs and automated analysis of KEM-based protocols"
    target: https://eprint.iacr.org/2023/1933.pdf
    date: 2023
    author:
      -
        ins: C. Cremers
        name: Cas Cremers
        org: CISPA Helmholtz Center for Information Security
      -
        ins: A. Dax
        name: Alexander Dax
        org: CISPA Helmholtz Center for Information Security
      -
        ins: N. Medinger
        name: Niklas Medinger
        org: CISPA Helmholtz Center for Information Security
  KSW24:
    title: "Binding Security of Implicitly-Rejecting KEMs and Application to BIKE and HQC"
    target: https://eprint.iacr.org/2024/1233
    date: 2024
    author:
      -
        ins: J. Krämer
        name: Juliane Krämer
      -
        ins: P. Struck
        name: Patrick Struck
      -
        ins: M. Weishäupl
        name: Maximiliane Weishäupl

--- abstract

The Hamming Quasi-Cyclic (HQC) Key-Encapsulation Mechanism is a
code-based, quantum-resistant key-encapsulation mechanism (KEM) selected
by the US National Institute of Standards and Technology (NIST) for
standardization as FIPS 207. This document specifies the conventions for
using HQC in the Internet X.509 Public Key Infrastructure. The conventions
for the subject public keys and private keys are also specified.

--- middle

# Introduction

The Hamming Quasi-Cyclic (HQC) Key-Encapsulation Mechanism is a
quantum-resistant KEM whose security is based on the hardness of decoding
random quasi-cyclic codes (the syndrome decoding problem). HQC was selected
by the US National Institute of Standards and Technology (NIST) PQC Project
{{NIST-PQC}} in March 2025 {{NIST-HQC-SELECTION}} as a fifth algorithm for
post-quantum encryption, complementing the lattice-based ML-KEM
{{?I-D.ietf-lamps-kyber-certificates}}. NIST is standardizing HQC as
FIPS 207.

HQC provides an alternative to ML-KEM that rests on a different mathematical
assumption (code-based rather than lattice-based), offering algorithm
diversity for deployments that wish to hedge against advances in
cryptanalysis of structured lattices.

This document specifies the use of HQC in Public Key Infrastructure X.509
(PKIX) certificates {{!RFC5280}} at three security levels corresponding to
NIST Security Categories 1, 3, and 5, referred to in this document as
HQC-128, HQC-192, and HQC-256, respectively. The private key format is also
specified.

<aside markdown="block">
  EDITOR'S NOTE: At the time of writing, FIPS 207 has not been published.
  The HQC parameters, algorithm construction, key sizes, and object
  identifiers referenced in this document are provisional and are based on
  the round-4 HQC submission {{HQC}} and on changes announced by NIST as
  under consideration for FIPS 207. All values marked "TBD" or described as
  provisional MUST be reconciled against the published FIPS 207 standard
  before this document is finalized.
</aside>

## Applicability Statement

HQC certificates are used in protocols where the public key is used to
generate and encapsulate a shared secret used to derive a symmetric key
used to encrypt a payload. NIST positions HQC as well suited to
applications requiring long-term keys, small ciphertexts relative to other
code-based KEMs, and fast encapsulation and decapsulation. To be used in
TLS, HQC certificates could only be used as end-entity identity
certificates and would require significant updates to the protocol.

# Conventions and Definitions

{::boilerplate bcp14-tagged}

# Algorithm Identifiers {#oids}

The `AlgorithmIdentifier` type is defined in {{!RFC5912}} as follows:

~~~
  AlgorithmIdentifier{ALGORITHM-TYPE, ALGORITHM-TYPE:AlgorithmSet} ::=
    SEQUENCE {
      algorithm   ALGORITHM-TYPE.&id({AlgorithmSet}),
      parameters  ALGORITHM-TYPE.
                    &Params({AlgorithmSet}{@algorithm}) OPTIONAL
    }
~~~

<aside markdown="block">
  NOTE: The above syntax is from {{!RFC5912}} and is compatible with the
  2021 ASN.1 syntax {{X680}}. See {{RFC5280}} for the 1988 ASN.1 syntax.
</aside>

The fields in `AlgorithmIdentifier` have the following meanings:

* `algorithm` identifies the cryptographic algorithm with an object
  identifier.

* `parameters`, which are optional, are the associated parameters for
  the algorithm identifier in the `algorithm` field.

The `AlgorithmIdentifier` for an HQC public key MUST use one of the
`id-alg-hqc` object identifiers (OID) listed below, based on the security
level. The `parameters` field of the `AlgorithmIdentifier` for the HQC
public key MUST be absent.

<aside markdown="block">
  EDITOR'S NOTE: The object identifiers below are PLACEHOLDERS. NIST is
  expected to assign HQC object identifiers under the Computer Security
  Objects Register (CSOR) {{CSOR}} once FIPS 207 is published. The arc
  shown mirrors the ML-KEM "kems" assignment and MUST be replaced with the
  values assigned by NIST.
</aside>

~~~
  nistAlgorithms OBJECT IDENTIFIER ::= { joint-iso-ccitt(2)
    country(16) us(840) organization(1) gov(101) csor(3)
    nistAlgorithm(4) }

  kems OBJECT IDENTIFIER ::= { nistAlgorithms 4 }

  id-alg-hqc-128 OBJECT IDENTIFIER ::= { kems TBD1 }

  id-alg-hqc-192 OBJECT IDENTIFIER ::= { kems TBD2 }

  id-alg-hqc-256 OBJECT IDENTIFIER ::= { kems TBD3 }
~~~

# Subject Public Key Fields  {#pub-key}

In the X.509 certificate, the `subjectPublicKeyInfo` field has the
`SubjectPublicKeyInfo` type, which has the following ASN.1 syntax:

~~~
  SubjectPublicKeyInfo {PUBLIC-KEY: IOSet} ::= SEQUENCE {
      algorithm        AlgorithmIdentifier {PUBLIC-KEY, {IOSet}},
      subjectPublicKey BIT STRING
  }
~~~

The fields in `SubjectPublicKeyInfo` have the following meaning:

* `algorithm` is the algorithm identifier and parameters for the
  public key (see above).

* `subjectPublicKey` contains the byte stream of the public key.

For each HQC parameter set, see {{tab-strengths}},
we define a `PUBLIC-KEY` ASN.1 type as follows.

~~~
  pk-hqc-128 PUBLIC-KEY ::= {
    IDENTIFIER id-alg-hqc-128
    -- KEY no ASN.1 wrapping; 2249 octets --
    PARAMS ARE absent
    CERT-KEY-USAGE { keyEncipherment }
    PRIVATE-KEY HQC-128-PrivateKey -- defined in Section 6
    }

  pk-hqc-192 PUBLIC-KEY ::= {
    IDENTIFIER id-alg-hqc-192
    -- KEY no ASN.1 wrapping; 4522 octets --
    PARAMS ARE absent
    CERT-KEY-USAGE { keyEncipherment }
    PRIVATE-KEY HQC-192-PrivateKey -- defined in Section 6
    }

  pk-hqc-256 PUBLIC-KEY ::= {
    IDENTIFIER id-alg-hqc-256
    -- KEY no ASN.1 wrapping; 7245 octets --
    PARAMS ARE absent
    CERT-KEY-USAGE { keyEncipherment }
    PRIVATE-KEY HQC-256-PrivateKey -- defined in Section 6
  }

  HQC-128-PublicKey ::= OCTET STRING (SIZE (2249))

  HQC-192-PublicKey ::= OCTET STRING (SIZE (4522))

  HQC-256-PublicKey ::= OCTET STRING (SIZE (7245))
~~~

<aside markdown="block">
  EDITOR'S NOTE: The public key sizes above are provisional, based on the
  HQC parameters under consideration for FIPS 207, and MUST be confirmed
  against the published standard.
</aside>

When an HQC public key appears outside of a `SubjectPublicKeyInfo`
type in an environment that uses ASN.1 encoding, it can be encoded
as an OCTET STRING by using the `HQC-128-PublicKey`,
`HQC-192-PublicKey`, and `HQC-256-PublicKey` types corresponding to
the correct key size.

{{!RFC5958}} describes the Asymmetric Key Package's `OneAsymmetricKey`
type for encoding asymmetric keypairs. When an HQC private key or
keypair is encoded as a `OneAsymmetricKey`, it follows the description
in {{priv-key}}.

# Key Usage Bits

The intended application for the key is indicated in the keyUsage certificate
extension; see {{Section 4.2.1.3 of RFC5280}}. If the `keyUsage` extension is
present in certificates, then `keyEncipherment` MUST be the only key usage set
for certificates that indicate `id-alg-hqc-*` in `SubjectPublicKeyInfo`,
(with `*` either 128, 192, or 256.)

# Private Key Format {#priv-key}

An HQC keypair is generated from a single seed. The seed is sampled
uniformly at random from a cryptographically secure random number
generator, and the decapsulation key and public key are derived
deterministically from the seed during key generation.

Because the entire keypair is reproducible from the seed, this document
specifies the seed as the private key format. This aligns with the
direction NIST has indicated for FIPS 207, in which the seed is expected to
be the permissible key format, and it avoids the interoperability
complexity of supporting multiple private key representations.

<aside markdown="block">
  EDITOR'S NOTE: The seed length is provisional pending FIPS 207. A
  32-octet seed is used here consistent with the HQC construction under
  consideration. This MUST be confirmed against the published standard.
</aside>

"Asymmetric Key Packages" {{RFC5958}} describes how to encode a private
key in a structure that both identifies which algorithm the private key
is for and allows for the public key and additional attributes about the
key to be included as well. For illustration, the ASN.1 structure
`OneAsymmetricKey` is replicated below.

~~~
  OneAsymmetricKey ::= SEQUENCE {
    version                  Version,
    privateKeyAlgorithm      SEQUENCE {
    algorithm                PUBLIC-KEY.&id({PublicKeySet}),
    parameters               PUBLIC-KEY.&Params({PublicKeySet}
                               {@privateKeyAlgorithm.algorithm})
                                  OPTIONAL}
    privateKey               OCTET STRING (CONTAINING
                               PUBLIC-KEY.&PrivateKey({PublicKeySet}
                                 {@privateKeyAlgorithm.algorithm})),
    attributes           [0] Attributes OPTIONAL,
    ...,
    [[2: publicKey       [1] BIT STRING (CONTAINING
                               PUBLIC-KEY.&Params({PublicKeySet}
                                 {@privateKeyAlgorithm.algorithm})
                                 OPTIONAL ]],
    ...
  }
~~~

For HQC private keys, the privateKey field in `OneAsymmetricKey` contains
the following DER-encoded `CHOICE` structure. The `seed` format is a fixed
`OCTET STRING` for all security levels.

~~~
  HQC-128-PrivateKey ::= CHOICE {
    seed [0] OCTET STRING (SIZE (32))
    }

  HQC-192-PrivateKey ::= CHOICE {
    seed [0] OCTET STRING (SIZE (32))
    }

  HQC-256-PrivateKey ::= CHOICE {
    seed [0] OCTET STRING (SIZE (32))
    }
~~~

The `seed` format (tag [0]) contains the seed value from which both the
decapsulation key and the public key are deterministically derived by the
HQC key generation procedure.

The `privateKeyAlgorithm` field uses the `AlgorithmIdentifier` structure
with the appropriate OID as defined in {{oids}}.

If present, the `publicKey` field will hold the encoded public key as
defined in {{pub-key}}.

<aside markdown="block">
  EDITOR'S NOTE: This document currently specifies a single, seed-only
  private key format, following NIST's stated leaning for FIPS 207 and the
  working preference for a single portable format. If FIPS 207 ultimately
  permits an expanded/decapsulation-key format in addition to the seed,
  this section will be revisited (compare the seed / expandedKey / both
  `CHOICE` in {{?I-D.ietf-lamps-kyber-certificates}}).
</aside>

# Security Considerations

The Security Considerations section of {{RFC5280}} applies to this
specification as well.

Protection of the private-key information, i.e., the seed, is vital to
public-key cryptography. Disclosure of the private-key material to another
entity can lead to masquerades.

The generation of private keys relies on random numbers. The use of
inadequate pseudo-random number generators (PRNGs) to generate these
values can result in little or no security. An attacker may find it
much easier to reproduce the PRNG environment that produced the keys,
searching the resulting small set of possibilities, rather than brute
force searching the whole key space. The generation of quality
random numbers is difficult.

Many protocols only rely on the IND-CCA security of a KEM. Some
(implicitly) require further binding properties, formalized in {{CDM23}}.
The private key format can influence these binding properties. Specifying
a single seed-based private key format, rather than a caller-supplied
expanded key, ensures that the decapsulation key is always derived by the
key generation procedure and is consistent with the public key.

HQC is an implicitly-rejecting KEM (it uses a secret rejection value in
the Fujisaki-Okamoto transform). The binding properties of implicitly-
rejecting KEMs, and specifically their application to BIKE and HQC, are
analyzed in {{KSW24}}. Implementers and protocol designers relying on
binding properties beyond IND-CCA SHOULD consult that analysis.

# IANA Considerations

For the ASN.1 Module in {{asn1}}, IANA is requested to assign an
object identifier (OID) for the module identifier (TBD) with a
Description of "id-mod-x509-hqc-2026". The OID for the module
should be allocated in the "SMI Security for PKIX Module Identifier"
registry (1.3.6.1.5.5.7.0).

--- back

# ASN.1 Module {#asn1}

This appendix includes the ASN.1 module {{X680}} for HQC. Note that
as per {{RFC5280}}, certificates use the Distinguished Encoding Rules; see
{{X690}}. This module imports objects from {{RFC5912}} and {{!RFC9629}}.

~~~
<CODE BEGINS>
{::include X509-HQC-2026.asn}
<CODE ENDS>
~~~

# Parameter Set Security and Sizes {#arnold}

NIST has defined security levels by picking a reference scheme that
NIST expects to offer notable levels of resistance to both quantum and
classical attack. A KEM algorithm that achieves NIST PQC security must
require computational resources to break IND-CCA security comparable or
greater than that required for key search on AES-128, AES-192, and AES-256
for Levels 1, 3, and 5, respectively.

The sizes in the table below are provisional and MUST be confirmed against
the published FIPS 207 standard.

| Level | Parameter Set | Public Key | Ciphertext | Shared Secret |
|-      |-              |-           |-           |-              |
| 1     | HQC-128       | 2249       | 4497       | 32            |
| 3     | HQC-192       | 4522       | 9042       | 32            |
| 5     | HQC-256       | 7245       | TBD        | 32            |
{: #tab-strengths title="Mapping between NIST Security Level, HQC parameter set, and provisional sizes in bytes"}

# Acknowledgments
{:numbered="false"}

TODO acknowledge.
