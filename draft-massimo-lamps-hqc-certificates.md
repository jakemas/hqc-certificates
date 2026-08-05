---
title: >
  Internet X.509 Public Key Infrastructure - Algorithm Identifiers
  for the Hamming Quasi-Cyclic Key-Encapsulation Mechanism (HQC-KEM)
abbrev: HQC in Certificates
category: std

docname: draft-massimo-lamps-hqc-certificates-latest
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
  latest: "https://jakemas.github.io/hqc-certificates/#go.draft-massimo-lamps-hqc-certificates.html"

author:
 -
    ins: J. Massimo
    name: Jake Massimo
    organization: AWS
    email: jakemas@amazon.com
 -
    ins: P. Kampanakis
    name: Panos Kampanakis
    organization: AWS
    email: kpanos@amazon.com

normative:
  FIPS207:
    title: "Hamming Quasi-Cyclic Key-Encapsulation Mechanism (HQC-KEM)"
    target: https://csrc.nist.gov/pubs/fips/207
    author:
    - org: National Institute of Standards and Technology (NIST)
    seriesinfo:
      NIST: FIPS 207
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
  RFC7468:

informative:
  HQC:
    target: https://pqc-hqc.org/
    title: "HQC: Hamming Quasi-Cyclic"
    author:
      - org: HQC Team
    date: 2025
  NIST-PQC:
    target: https://csrc.nist.gov/projects/post-quantum-cryptography
    title: >
      Post-Quantum Cryptography Project
    author:
    - org: National Institute of Standards and Technology (NIST)
    date: 2016-12-20
  CDM23:
    title: "Keeping Up with the KEMs: Stronger Security Notions for KEMs and automated analysis of KEM-based protocols"
    target: https://eprint.iacr.org/2023/1933
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
  ABDGZ16:
    title: "Efficient Encryption from Random Quasi-Cyclic Codes"
    target: https://eprint.iacr.org/2016/1194
    date: 2016
    author:
      - {ins: C. Aguilar Melchor, name: Carlos Aguilar Melchor}
      - {ins: O. Blazy, name: Olivier Blazy}
      - {ins: J-C. Deneuville, name: Jean-Christophe Deneuville}
      - {ins: P. Gaborit, name: Philippe Gaborit}
      - {ins: G. Zémor, name: Gilles Zémor}
  SENDRIER11:
    title: "Decoding One Out of Many"
    target: https://eprint.iacr.org/2011/367
    date: 2011
    author:
      - {ins: N. Sendrier, name: Nicolas Sendrier}
  SDE21:
    title: "Syndrome Decoding Estimator"
    target: https://eprint.iacr.org/2021/1243
    date: 2021
    author:
      - {ins: A. Esser, name: Andre Esser}
      - {ins: E. Bellini, name: Emanuele Bellini}
  ISD-HQC-2026:
    title: "Multilevel Amortized Gaussian Elimination in Information-Set Decoding: Applications to HQC and PCG"
    target: https://eprint.iacr.org/2026/1498
    date: 2026
    author:
      - {ins: K. Carrier, name: Kévin Carrier}
      - {ins: V. Hatey, name: Valérian Hatey}
      - {ins: L. Luzzi, name: Laura Luzzi}
      - {ins: J-P. Tillich, name: Jean-Pierre Tillich}
  GJS16:
    title: "A Key Recovery Attack on MDPC with CCA Security Using Decoding Errors"
    target: https://eprint.iacr.org/2016/858
    date: 2016
    author:
      - {ins: Q. Guo, name: Qian Guo}
      - {ins: T. Johansson, name: Thomas Johansson}
      - {ins: P. Stankovski, name: Paul Stankovski}
  HQC-TIMING-2019:
    title: "A Practicable Timing Attack Against HQC and its Countermeasure"
    target: https://eprint.iacr.org/2019/909
    date: 2019
    author:
      - {ins: G. Wafo-Tapa, name: Guillaume Wafo-Tapa}
      - {ins: S. Bettaieb, name: Slim Bettaieb}
      - {ins: L. Bidoux, name: Loïc Bidoux}
      - {ins: P. Gaborit, name: Philippe Gaborit}
      - {ins: E. Marcatel, name: Etienne Marcatel}
  HQC-REJECT-2021:
    title: "Don't Reject This: Key-Recovery Timing Attacks Due to Rejection-Sampling in HQC and BIKE"
    target: https://eprint.iacr.org/2021/1485
    date: 2021
    author:
      - {ins: Q. Guo, name: Qian Guo}
      - {ins: C. Hlauschek, name: Clemens Hlauschek}
      - {ins: T. Johansson, name: Thomas Johansson}
      - {ins: N. Lahr, name: Norman Lahr}
      - {ins: A. Nilsson, name: Alexander Nilsson}
      - {ins: R. L. Schröder, name: Robin Leander Schröder}
  HQC-DIV-2024:
    title: "Divide and Surrender: Exploiting Variable Division Instruction Timing in HQC Key Recovery Attacks"
    target: https://eprint.iacr.org/2024/299
    date: 2024
    author:
      - {ins: R. L. Schröder, name: Robin Leander Schröder}
      - {ins: S. Gast, name: Stefan Gast}
      - {ins: Q. Guo, name: Qian Guo}
  HQC-AVX2-2026:
    title: "Breaking Optimized HQC: The First Cache-Timing Full Decryption Oracle Key-Recovery Attack in Post-Quantum Cryptography"
    target: https://eprint.iacr.org/2026/693
    date: 2026
    author:
      - {ins: H. Dong, name: Haiyue Dong}
      - {ins: Q. Guo, name: Qian Guo}
  HQC-POWER-2022:
    title: "A Power Side-Channel Attack on the Reed-Muller Reed-Solomon Version of the HQC Cryptosystem"
    target: https://eprint.iacr.org/2022/724
    date: 2022
    author:
      - {ins: T. Schamberger, name: Thomas Schamberger}
      - {ins: L. Holzbaur, name: Lukas Holzbaur}
      - {ins: J. Renner, name: Julian Renner}
      - {ins: A. Wachter-Zeh, name: Antonia Wachter-Zeh}
      - {ins: G. Sigl, name: Georg Sigl}
  HQC-TRACE-2025:
    title: "Single-Trace Key Recovery Attacks on HQC Using Valid and Invalid Ciphertexts"
    target: https://eprint.iacr.org/2025/1987
    date: 2025
    author:
      - {ins: H. Dong, name: Haiyue Dong}
      - {ins: Q. Guo, name: Qian Guo}
      - {ins: D. Nabokov, name: Denis Nabokov}

--- abstract

The Hamming Quasi-Cyclic Key-Encapsulation Mechanism (HQC) is a
quantum-resistant, code-based key-encapsulation mechanism (KEM). This
document specifies the conventions for using HQC in the Internet X.509
Public Key Infrastructure. The conventions for the subject public keys and
private keys are also specified.

--- middle

# Introduction

The Hamming Quasi-Cyclic Key-Encapsulation Mechanism (HQC) is a
quantum-resistant, code-based key-encapsulation mechanism (KEM)
standardized by the US National Institute of Standards and Technology
(NIST) PQC Project {{NIST-PQC}} in, the forthcoming, {{FIPS207}}. This
document specifies the use of HQC in Public Key Infrastructure X.509 (PKIX)
certificates {{!RFC5280}} at three security levels corresponding to NIST
Security Categories 1, 3, and 5, referred to in this document as HQC-KEM-128,
HQC-KEM-192, and HQC-KEM-256, respectively. The private key format is also
specified.

The security of HQC is based on the hardness of decoding random
quasi-cyclic codes. As a code-based scheme, HQC rests on a different
mathematical assumption than the lattice-based ML-KEM
{{?I-D.ietf-lamps-kyber-certificates}}.

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
`id-alg-hqc-kem` object identifiers (OID) listed below, based on the security
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

  id-alg-hqc-kem-128 OBJECT IDENTIFIER ::= { kems TBD1 }

  id-alg-hqc-kem-192 OBJECT IDENTIFIER ::= { kems TBD2 }

  id-alg-hqc-kem-256 OBJECT IDENTIFIER ::= { kems TBD3 }
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
  pk-hqc-kem-128 PUBLIC-KEY ::= {
    IDENTIFIER id-alg-hqc-kem-128
    -- KEY no ASN.1 wrapping; 2241 octets --
    PARAMS ARE absent
    CERT-KEY-USAGE { keyEncipherment }
    PRIVATE-KEY HQC-KEM-128-PrivateKey -- defined in Section 6
    }

  pk-hqc-kem-192 PUBLIC-KEY ::= {
    IDENTIFIER id-alg-hqc-kem-192
    -- KEY no ASN.1 wrapping; 4514 octets --
    PARAMS ARE absent
    CERT-KEY-USAGE { keyEncipherment }
    PRIVATE-KEY HQC-KEM-192-PrivateKey -- defined in Section 6
    }

  pk-hqc-kem-256 PUBLIC-KEY ::= {
    IDENTIFIER id-alg-hqc-kem-256
    -- KEY no ASN.1 wrapping; 7237 octets --
    PARAMS ARE absent
    CERT-KEY-USAGE { keyEncipherment }
    PRIVATE-KEY HQC-KEM-256-PrivateKey -- defined in Section 6
  }

  HQC-KEM-128-PublicKey ::= OCTET STRING (SIZE (2241))

  HQC-KEM-192-PublicKey ::= OCTET STRING (SIZE (4514))

  HQC-KEM-256-PublicKey ::= OCTET STRING (SIZE (7237))
~~~

<aside markdown="block">
  EDITOR'S NOTE: The public key sizes above are provisional, based on the
  HQC parameters under consideration for FIPS 207, and MUST be confirmed
  against the published standard.
</aside>

When an HQC public key appears outside of a `SubjectPublicKeyInfo`
type in an environment that uses ASN.1 encoding, it can be encoded
as an OCTET STRING by using the `HQC-KEM-128-PublicKey`,
`HQC-KEM-192-PublicKey`, and `HQC-KEM-256-PublicKey` types corresponding to
the correct key size.

{{!RFC5958}} describes the Asymmetric Key Package's `OneAsymmetricKey`
type for encoding asymmetric keypairs. When an HQC private key or
keypair is encoded as a `OneAsymmetricKey`, it follows the description
in {{priv-key}}.

# Key Usage Bits

The intended application for the key is indicated in the keyUsage certificate
extension; see {{Section 4.2.1.3 of RFC5280}}. If the `keyUsage` extension is
present in certificates, then `keyEncipherment` MUST be the only key usage set
for certificates that indicate `id-alg-hqc-kem-*` in `SubjectPublicKeyInfo`,
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
  HQC-KEM-128-PrivateKey ::= CHOICE {
    seed [0] OCTET STRING (SIZE (32))
    }

  HQC-KEM-192-PrivateKey ::= CHOICE {
    seed [0] OCTET STRING (SIZE (32))
    }

  HQC-KEM-256-PrivateKey ::= CHOICE {
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
public-key cryptography. HQC is a Key-Encapsulation Mechanism, so the
private key is a decapsulation key: an entity that obtains it can
decapsulate any ciphertext produced for the corresponding public key and
recover the resulting shared secrets. Disclosure of the private-key
material therefore leads to loss of confidentiality for all data protected
by those shared secrets, including data protected before the disclosure
occurred.

The generation of private keys relies on random numbers. The use of
inadequate pseudo-random number generators (PRNGs) to generate these
values can result in little or no security. An attacker may find it
much easier to reproduce the PRNG environment that produced the keys,
searching the resulting small set of possibilities, rather than brute
force searching the whole key space. The generation of quality
random numbers is difficult. Because the entire HQC keypair is derived
deterministically from the seed (see {{priv-key}}), the secrecy and
entropy of the seed are paramount: a weak or predictable PRNG at key
generation compromises the whole long-term key.

## Underlying Assumption and Cryptanalysis

The security of HQC is based on the hardness of the decisional
Quasi-Cyclic Syndrome Decoding (DQCSD) problem for random quasi-cyclic
codes {{ABDGZ16}}. The reduction relies on two DQCSD instances, governing
the indistinguishability of the public key and of the ciphertext
respectively. Unlike code-based schemes that rely on a hidden code with
algebraic structure (for example, the Goppa codes of Classic McEliece),
HQC uses random quasi-cyclic codes, so its security does not depend on
concealing the structure of the underlying code. HQC therefore rests on a
different mathematical foundation than the lattice-based ML-KEM
{{?I-D.ietf-lamps-kyber-certificates}}, offering cryptographic diversity
against advances in lattice cryptanalysis.

The best known attacks against DQCSD reduce to generic Information Set
Decoding (ISD); the quasi-cyclic structure yields only a Decoding One Out
of Many {{SENDRIER11}} speedup on the order of the square root of the
number of instances (equal to the circulant block length for quasi-cyclic
codes), which is already accounted for in the HQC parameters. The concrete
cost of these attacks is estimated using tools such as the Syndrome
Decoding Estimator {{SDE21}}. The concrete security of ISD against HQC
remains an area of active research, and refinements continue to be
published (for example, {{ISD-HQC-2026}}). The HQC parameters were
selected to offer a smaller security margin than Classic McEliece.
Because the parameters, and hence the mapping from parameter set to object
identifier in this document, are provisional pending {{FIPS207}}, relying
parties are advised to track cryptanalytic developments; see also the
editor's notes in {{oids}} and {{params}}.

## Decapsulation Failures

HQC is designed so that the decapsulation failure rate (DFR) is negligible
with respect to the targeted security level of each parameter set. This is
relevant to the IND-CCA security of the KEM: the tightness of the
Fujisaki-Okamoto security argument depends on the correctness error of the
underlying public-key encryption scheme. Moreover, for code-based schemes a
decapsulation failure is correlated with the secret key, so an adversary
who can detect failures can mount a reaction (decryption-failure) attack to
recover secret-key structure {{GJS16}}. Because HQC uses implicit
rejection, a failure is not directly observable at the KEM interface (a
pseudorandom shared secret is returned in either case) and can only be
detected through a side channel or a protocol-level distinguisher.
Choosing a DFR below the security level makes locating even a single
failure infeasible for a bounded adversary.

The claimed DFR is a property of the specific HQC decoder (a concatenated
construction using an outer Reed-Solomon code and an inner Reed-Muller
code). An implementation that substitutes a different or approximate
decoder, or that otherwise raises the failure probability, can weaken the
IND-CCA security argument. Implementations should use the decoding
procedure fixed by {{FIPS207}} and avoid optimizations that increase the
decapsulation failure rate.

## Side-Channel Attacks

HQC has an extensive side-channel and micro-architectural attack
literature. A notable feature of this literature is that a constant-time C
implementation is not by itself sufficient: several key-recovery attacks
succeed against source code intended to be constant-time, because compiler
optimizations or micro-architectural behaviour reintroduce
secret-dependent timing in the compiled binary.

Documented attacks include chosen-ciphertext timing attacks against the
(then Reed-Muller/BCH) decoder {{HQC-TIMING-2019}}; timing attacks
exploiting the rejection sampling used to generate fixed-weight vectors,
which succeed even when the decoder itself is constant-time
{{HQC-REJECT-2021}}; attacks exploiting variable-time division
instructions emitted by the compiler {{HQC-DIV-2024}}; cache-timing
key-recovery attacks against optimized (for example, AVX2) implementations
that claim to be constant-time {{HQC-AVX2-2026}}; power analysis of the
Reed-Solomon decoder {{HQC-POWER-2022}}; and single-trace key recovery,
in both passive and chosen-ciphertext variants {{HQC-TRACE-2025}}. The
decoder and the fixed-weight vector sampler are recurring leakage sites.

Implementations of HQC decapsulation are advised to be verified as
constant-time at the level of the emitted machine code, not merely the
source, and to avoid data-dependent branches, table lookups, and
variable-latency instructions (such as integer division) on
secret-dependent values.

A public key carried in an X.509 certificate is, by its nature, a
long-lived key that is reused across many decapsulations. The adaptive
chosen-ciphertext timing and cache attacks noted above
({{HQC-TIMING-2019}}, {{HQC-REJECT-2021}}, {{HQC-DIV-2024}},
{{HQC-AVX2-2026}}) require many decapsulation queries against a fixed key,
so a long-lived certificate key increases the opportunity to accumulate
them; these attacks additionally require the deployment to expose a
decapsulation oracle whose timing or micro-architectural behaviour is
observable to the attacker. By contrast, the single-trace attacks
({{HQC-TRACE-2025}}) can recover the key from a single decapsulation and
are not mitigated by limiting key reuse. Implementations that decapsulate
with a certificate-bound HQC private key SHOULD use side-channel-hardened
implementations.

In a certificate ecosystem, a single static key is exposed to many
ciphertexts from many parties (a multi-target setting). The FIPS 207-track
HQC construction incorporates a per-ciphertext salt in its key derivation
to strengthen multi-target and multi-ciphertext resistance; the exact
construction is fixed by {{FIPS207}}.

## KEM Binding Properties

Many protocols rely only on the IND-CCA security of a KEM. Some
(implicitly) require further binding properties, formalized in {{CDM23}}.
The private key format can influence these binding properties. Specifying
a single seed-based private key format (see {{priv-key}}), rather than a
caller-supplied expanded key, ensures that the decapsulation key is always
derived by the key generation procedure and is consistent with the public
key.

HQC is an implicitly-rejecting KEM: it uses a secret rejection value in the
Fujisaki-Okamoto transform so that decapsulating an invalid ciphertext
returns a pseudorandom shared secret rather than an explicit error. The
binding properties of implicitly-rejecting KEMs, and specifically their
application to BIKE and HQC, are analyzed in {{KSW24}}. Implicitly-
rejecting Fujisaki-Okamoto KEMs do not automatically satisfy the strongest
binding notions; implementers and protocol designers who rely on binding
properties beyond IND-CCA SHOULD consult that analysis. Where a protocol
requires the shared secret to bind uniquely to a particular public key or
ciphertext, that property is best established explicitly at the protocol
layer (for example, by including the certificate or public key in the key
derivation) rather than assumed of the KEM.

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

# Parameter Set Security and Sizes {#params}

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
| 1     | HQC-KEM-128       | 2241       | 4433       | 32            |
| 3     | HQC-KEM-192       | 4514       | 8978       | 32            |
| 5     | HQC-KEM-256       | 7237       | 14421      | 32            |
{: #tab-strengths title="Mapping between NIST Security Level, HQC parameter set, and provisional sizes in bytes"}

# Examples {#examples}

This appendix contains examples of HQC-KEM public keys and private keys.

<aside markdown="block">
  RFC EDITOR: The algorithm identifiers in these examples use placeholder
  object identifiers under the NIST "kems" arc pending assignment by NIST/CSOR
  once FIPS 207 is published; the examples will be regenerated with the
  assigned values. The key sizes shown are those produced by a reference
  implementation of the HQC specification and are provisional until confirmed
  against the published FIPS 207 standard.
</aside>

## Example Private Keys {#example-private}

The following examples show HQC-KEM private keys for each security level,
all derived from the same seed `000102...1e1f`. HQC uses the seed as the only
private-key representation (using a context-specific `[0]` primitive tag with
an implicit encoding of `OCTET STRING`).

### HQC-KEM-128 Private Key

Each of the examples includes the textual encoding {{RFC7468}} followed by
the so-called "pretty print"; the private keys are the same.

~~~
{::include ./example/HQC-KEM-128-seed.priv}
~~~

~~~
{::include ./example/HQC-KEM-128-seed.priv.txt}
~~~

### HQC-KEM-192 Private Key

Each of the examples includes the textual encoding {{RFC7468}} followed by
the so-called "pretty print"; the private keys are the same.

~~~
{::include ./example/HQC-KEM-192-seed.priv}
~~~

~~~
{::include ./example/HQC-KEM-192-seed.priv.txt}
~~~

### HQC-KEM-256 Private Key

Each of the examples includes the textual encoding {{RFC7468}} followed by
the so-called "pretty print"; the private keys are the same.

~~~
{::include ./example/HQC-KEM-256-seed.priv}
~~~

~~~
{::include ./example/HQC-KEM-256-seed.priv.txt}
~~~

## Example Public Keys {#example-public}

The following is the HQC-KEM-128 public key corresponding to the private
key in the previous section. The textual encoding {{RFC7468}} is
followed by the so-called "pretty print"; the public keys are the same.

~~~
{::include ./example/HQC-KEM-128.pub}
~~~

~~~
{::include ./example/HQC-KEM-128.pub.txt}
~~~

The following is the HQC-KEM-192 public key corresponding to the private
key in the previous section. The textual encoding {{RFC7468}} is
followed by the so-called "pretty print"; the public keys are the same.

~~~
{::include ./example/HQC-KEM-192.pub}
~~~

~~~
{::include ./example/HQC-KEM-192.pub.txt}
~~~

The following is the HQC-KEM-256 public key corresponding to the private
key in the previous section. The textual encoding {{RFC7468}} is
followed by the so-called "pretty print"; the public keys are the same.

~~~
{::include ./example/HQC-KEM-256.pub}
~~~

~~~
{::include ./example/HQC-KEM-256.pub.txt}
~~~

# Acknowledgments
{:numbered="false"}

TODO acknowledge.
