# The Human Record — fractal record architecture RFC

Status: **WORKING RFC / EXPLORATORY SCALE LAYER / NOT CANON / NO CURRENT REGISTRY SEMANTICS CHANGE**

Date: 19 September 2026

This RFC starts from the current Human Record rather than replacing it.

The current project already separates:

```text
NAME != ENTITY
MENTION != ENTITY
URL != SOURCE
SOURCE != OBSERVATION
OBSERVATION != PRESERVED COPY
PRESERVED COPY != TRUTH
ENTITY != ASSERTION
ASSERTION != TRUTH
CUSTODY != GOVERNANCE
```

It already has opaque entity, source and assertion identifiers; source observations;
preservation routes; correction history; identity merge/split handling; living-subject
boundaries; and sparse cross-record registries.

The next problem is larger:

> How can a future reader, human or machine, keep asking **why should I believe this
> representation, where did it come from, who or what changed it, under which authority,
> through which process, and what independent history remains if one custodian lies,
> disappears or is compromised?**

This RFC proposes a recursive grammar for answering those questions without turning THR
into a central truth authority, a universal people database, or a cryptographic
authenticity oracle.

It is deliberately a design target, not an instruction to populate new registries now.

---

## Falsification pass 1 — earned constraints

The first paper test against all four current Human Record machine records is preserved in
`FRACTAL_FALSIFICATION.md`.

That pass found ten constraints that this RFC now adopts before any implementation work.

### A. Three levels of addressability

Not every meaningful thing should receive a globally durable THR identifier.

```text
LOCAL VALUE / LOCAL NODE
-> meaningful only inside one bounded record

RECORD-LOCAL ADDRESSABLE OBJECT
-> stable inside one record / export

SHARED THR OBJECT
-> cross-record durable identifier earned by repeated need
```

```text
RECORDABLE != GLOBALLY ENUMERABLE
CAN ASSIGN ID != SHOULD ASSIGN SHARED ID
```

### B. Recursion is materiality-bounded

The fractal model must not become infinite graph expansion.

Recurse only when the next layer could materially change:
- identity;
- evidence;
- independence;
- authority;
- correction;
- preservation;
- interpretation;
- or a consequential handling boundary.

```text
RECURSION POSSIBLE != RECURSION MATERIAL
NO MATERIAL CONSEQUENCE -> STOP DESCENT
```

### C. Event object is not event proof

An event object can provide a stable referent for competing claims.

It does not prove that the event occurred, occurred at the claimed time, involved the
claimed participants, or had the claimed meaning.

```text
EVENT OBJECT != ASSERTION EVENT OCCURRED
EVENT ID != EVENT CERTAINTY
```

### D. Process referent is not process observation

THR may need to distinguish:
- a process claimed by a source;
- a process described by documentation;
- a process actually executed by THR;
- a process independently observed by another party.

```text
PROCESS CLAIMED BY SOURCE
!=
PROCESS OBSERVED BY THR
!=
PROCESS EXECUTED BY THR
```

### E. Source statement, observation, attestation and process receipt stay distinct

These are different evidence-bearing acts:

```text
SOURCE STATEMENT
!=
OBSERVATION
!=
ATTESTATION
!=
PROCESS RECEIPT
```

Do not wrap every source statement in an `attestation` object merely because the
attestation vocabulary is convenient.

### F. Authority is typed, scoped and temporal

Authority must state **authority for what**.

Examples:
- custody;
- current status classification;
- technical operation;
- publication;
- preservation;
- governance;
- correction execution;
- representation of a community under a documented process.

Where material it must also be time-bounded or observation-bounded.

```text
AUTHORITY IN ONE FUNCTION != AUTHORITY IN ALL FUNCTIONS
LATER AUTHORITY != RETROACTIVE CONTROL OF EARLIER STATES
```

Do not collapse bounded status ownership into cultural, moral or governance authority.

### G. Independence is proposition/function-specific

The same two objects can be independent for one question and dependent for another.

Examples:
- two independent archives may independently hold the same bytes;
- they may still derive the artwork attribution from one museum catalogue;
- two photographs may be independent captures of one physical object while sharing the
  same stated provenance.

Therefore:

```text
INDEPENDENT FOR BYTE CUSTODY
!=
INDEPENDENT FOR CLAIM ORIGINATION
!=
INDEPENDENT FOR PHYSICAL OBSERVATION
!=
INDEPENDENT GOVERNANCE
```

No universal independence score is implied.

### H. Shared interfaces do not imply one universal record schema

Camp Fire, the flak claim, sieve/riddle revival and Hannibal require different local
structures for good reasons.

The fractal architecture should standardise the joins that need interoperability, not
flatten all records into one triple store.

```text
COMMON ADDRESSING / RELATION PRINCIPLES
!=
ONE UNIVERSAL RECORD SHAPE
```

### I. No universal trust score

Trustworthiness is multidimensional and claim-specific.

Do not create a core architecture such as:

```text
trust_score = 0.94
```

Prefer inspectable provenance, bounded authority, source ancestry, explicit observations
and preserved disagreements.

### J. Living-person anti-enumeration applies to principals too

A living person appearing in a source, lineage or interaction does not automatically earn:
- a shared entity;
- a shared principal;
- a public key mapping;
- a cross-record profile.

```text
LIVING MENTION != PUBLIC PRINCIPAL
PRINCIPAL ADDRESSABILITY != PERSON DOSSIER
```

These constraints are now part of the RFC's design target.

---

## 1. The fractal proposition

A mature Human Record should not terminate at "the record".

Every evidentiary object may itself have identity, provenance, claims, observations,
corrections and custody.

Examples:

```text
WORK
-> OWNER CATALOGUE RECORD
-> CATALOGUE RECORD OBSERVATION
-> IMAGE REPRODUCTION
-> IMAGE CAPTURE PROCESS
-> PRESERVATION COPY
-> INSTITUTION
-> INSTITUTIONAL ATTESTATION
-> SOFTWARE TRANSFORM
-> VALIDATOR RESULT
-> THR RECORD STATE
-> HUMAN VIEW
```

Each node can itself be questioned.

The same grammar should therefore work at many scales:

```text
WHAT IS THIS?
HOW IS IT ADDRESSED?
WHAT CLAIMS ARE MADE ABOUT IT?
WHAT EVIDENCE BEARS ON THOSE CLAIMS?
WHO OR WHAT ATTESTED TO THAT?
UNDER WHAT AUTHORITY?
WHICH PROCESS PRODUCED THIS STATE?
WHAT CHANGED?
WHAT IS PRESERVED?
WHAT IS INDEPENDENT?
WHAT IS UNKNOWN?
WHAT CAN STILL ANSWER BACK?
```

This is the sense in which THR may become fractal.

```text
RECORD -> RELATIONS -> RECORDABLE OBJECTS -> RELATIONS -> ...
```

A reader should be able to stop at a useful level. The architecture must not require
infinite expansion or universal collection.

---

## 2. Separate the functions of the "identifier"

A future THR identifier must not become a master token that conflates identity,
authority, authenticity and access.

The useful analogy to an API key, network address and payment identifier should be split
into separate functions.

### 2.1 Public address

The existing opaque THR IDs already serve the first function.

Examples:

```text
thr:entity:<uuid>
thr:source:<uuid>
thr:observation:<uuid>
thr:assertion:<uuid>
```

Future types may be earned, for example:

```text
thr:event:<uuid>
thr:process:<uuid>
thr:attestation:<uuid>
thr:principal:<uuid>
thr:anchor:<uuid>
```

A public THR ID means only:

> This is the stable reference THR uses for this recordable object.

```text
THR_ID != IDENTITY PROOF
THR_ID != PRIVATE KEY
THR_ID != AUTHORITY
THR_ID != AUTHENTICITY
THR_ID != TRUTH
```

### 2.2 Content identity / fixity

Where bytes exist, a digest or content-addressed identifier can say which bytes were
observed.

```text
CONTENT HASH -> BYTE IDENTITY CLAIM
CONTENT HASH != ORIGIN
CONTENT HASH != AUTHORSHIP
CONTENT HASH != TRUTH
```

### 2.3 Attesting principal

A principal is a bounded actor capable of making an attestation.

Possible principals include:
- an institution;
- a human acting in a stated role;
- an archive;
- a sensor or capture device;
- an AI system / bounded runtime aperture;
- a software service;
- a validator/release process.

A principal identifier does not imply that the actor is trustworthy or entitled to act.

### 2.4 Keys and signatures

A cryptographic key may authenticate that a holder of that key signed particular bytes.

Keys must be replaceable and revocable without replacing the identity of the principal or
the object.

```text
KEY != PRINCIPAL
SIGNATURE != AUTHORITY
SIGNATURE != TRUTH
KEY LOSS != ENTITY DEATH
KEY ROTATION != IDENTITY CHANGE
```

The first THR RFC does **not** require introducing a project PKI.

Existing signed Git commits, archive receipts or institution-supplied signatures can be
recorded as evidence when they already exist.

### 2.5 Capability / authority

Authority answers a different question:

> What was this principal legitimately permitted or delegated to do in this context?

Examples might eventually include:
- attest to institutional custody;
- publish a record state;
- operate a validator;
- correct a particular record;
- serve a replica;
- represent a community under a documented process.

Authority must be scoped, sourced and correctable.

```text
CAN_SIGN != MAY_GOVERN
CREDENTIAL_CUSTODY != POLICY_AUTHORITY
TECHNICAL_ACCESS != LEGITIMATE_AUTHORITY
FORMAL_AUTHORITY != MORAL LEGITIMACY
```

Do not create a global authority score.

---

## 3. Candidate recursive object types

The existing entity/source/observation/assertion layers remain valid.

The following are candidate additional concepts. They should become registry types only
when real records require cross-record use.

### 3.1 Event

A bounded occurrence or claimed occurrence.

An event object may represent:
- creation;
- publication;
- accession;
- transfer of custody;
- experiment;
- correction;
- interview;
- capture;
- software release;
- validator execution;
- destruction/loss;
- observation of a physical state.

Important:

```text
EVENT RECORD != EVENT ITSELF
EVENT ID != PROOF EVENT OCCURRED
```

Claims about an event still require assertions/evidence.

### 3.2 Process / transform

A process describes how an input became an output.

Examples:
- image scan;
- OCR;
- translation;
- colour restoration;
- data analysis;
- model inference;
- schema migration;
- validator;
- human editorial transformation;
- record-to-public-view generation.

A process instance should be able, where material, to point to:
- inputs;
- outputs;
- software / method identity;
- operator/principal;
- time;
- parameters or bounded configuration;
- relevant environment;
- receipt / log / attestation;
- known limitations.

```text
OUTPUT EXISTS != PROCESS REPRODUCIBLE
PROCESS REPRODUCIBLE != RESULT TRUE
```

### 3.3 Attestation

An attestation records that a principal asserted something at a bounded time under a
stated role or authority basis.

Minimum conceptual shape:

```json
{
  "id": "thr:attestation:<uuid>",
  "principal": "thr:principal:<uuid>",
  "statement_ref": "thr:assertion:<uuid>",
  "made_at": "...",
  "role": "...",
  "authority_basis": "...",
  "signature": null,
  "scope": "...",
  "revocation_or_correction_refs": []
}
```

This is not a claim that signatures are always required.

```text
ATTESTATION != ENDORSEMENT BY THR
SIGNED ATTESTATION != TRUE ATTESTATION
MANY ATTESTATIONS != INDEPENDENT EVIDENCE
```

### 3.4 Principal

A principal is an addressable source of action/attestation, not a universal identity
profile.

A principal may be thinner than an entity.

For a living human, public principal identity must not silently become a general person
record.

### 3.5 Anchor / checkpoint

An anchor is evidence that a bounded state existed no later than, no earlier than, or at
a claimed time under the limitations of the anchoring system.

Possible anchor owners might include:
- signed Git history;
- transparency logs;
- archival captures;
- timestamp authorities;
- institutional deposit receipts;
- independent mirrors;
- later content-addressed/distributed systems.

```text
TIMESTAMP != CREATION TIME
ANCHOR != TRUTH
ONE HOST'S LOG != INDEPENDENT HISTORY
```

---

## 4. Recursive self-description

A serious THR cannot preserve provenance for the world while treating its own machinery
as invisible.

Eventually, THR should be capable of recording:

- schema/specification versions;
- validator source versions;
- validator executions;
- record-construction processes;
- migration processes;
- generated-view processes;
- releases;
- stewardship/governance decisions;
- correction propagation;
- public export/checkpoint identity.

This does not mean every execution must become a public record.

It means that when the trustworthiness of a material THR state depends on a process, that
process should be addressable and its evidence inspectable.

Example:

```text
THR RECORD STATE R7
-> GENERATED FROM record.json @ blob X
-> VALIDATED BY validator release V
-> validator source @ blob Y
-> validation run receipt Z
-> PUBLIC VIEW generated by process P
-> published in checkpoint C
```

Again:

```text
VALIDATOR PASS != TRUTH
REPRODUCIBLE BUILD != ETHICAL LEGITIMACY
SIGNED RELEASE != CORRECT RECORD
```

---

## 5. Independence is a graph property, not a count

Synthetic abundance makes apparent multiplicity cheap.

A robust THR must keep distinguishing:

```text
TEN COPIES OF ONE ORIGIN
!=
TEN INDEPENDENT WITNESSES
```

Independence can be partial and claim-specific.

Two institutions may independently preserve one carrier while both derive an attribution
from the same catalogue.

Two photographs may be independent captures of the same physical object but not
independent evidence for its creator.

Therefore future independence representation should support:

- common source ancestry;
- common owner;
- shared process/tool;
- shared training/data pipeline where known and relevant;
- independent physical observation;
- independent custody;
- unknown relation.

Do not force a universal numerical independence score.

---

## 6. Distributed survival and anti-rewrite properties

A future robust THR should become harder to rewrite retrospectively than a single website
or database.

This does not require inventing a blockchain.

Candidate properties:

1. **Portable public exports**
   - a complete bounded record can be mirrored without the original service.

2. **Content-addressed checkpoints**
   - a checkpoint identifies the exact exported bytes.

3. **Independent witnesses / mirrors**
   - unrelated custodians can retain or attest to a checkpoint.

4. **Append-visible correction**
   - current state can change without deleting earlier material states.

5. **Cross-owner anchoring**
   - where useful, a material checkpoint can be externally witnessed by stronger owners.

6. **No mandatory central resolver**
   - thehumanrecord.net should be a useful entrance, not the single machine that can tell
     the world what every THR identifier means.

The design target is:

```text
COMPROMISE ONE HOST
!=
SILENTLY REWRITE ALL SURVIVING HISTORY
```

A future federation may allow independent THR-compatible stores to exchange signed or
hashed bundles while disagreeing about conclusions.

```text
SHARED PROTOCOL != SHARED GOVERNANCE
MIRROR != ENDORSEMENT
REPLICA != INDEPENDENT EVIDENCE
```

---

## 7. Physical-world anchors

Digital provenance alone cannot establish physical reality.

For a physical object or event, useful future evidence may include:
- accession/custody records;
- independent photographs;
- laboratory measurements;
- conservation observations;
- serial/manufacturer identifiers;
- secure capture-device receipts;
- material fingerprints;
- sensor outputs;
- witness testimony;
- contemporaneous printed records;
- independently held reproductions.

No one method should be elevated into a universal authenticity oracle.

```text
DIGITAL CHAIN != PHYSICAL CONTINUITY
SENSOR SIGNATURE != SENSOR HONESTY
SECURE HARDWARE != TRUE INTERPRETATION
PHYSICAL MEASUREMENT != COMPLETE PROVENANCE
```

THR should interoperate with domain experts and stronger custody owners rather than
pretending to replace conservation science, archives, laboratories or courts.

---

## 8. Living-human anti-enumeration is architectural

The current identity model already states that scalable identity is not permission to
build profiles on everyone.

A fractal architecture increases that risk and therefore needs stronger negative design
requirements.

For living humans:

- do not automatically allocate public globally enumerable entity IDs merely because a
  name can be resolved;
- prefer record-local mentions when cross-record identity is unnecessary;
- support contextual or pairwise identifiers if a future private/restricted function
  genuinely requires stable linkage without public enumeration;
- separate public historical assertions from private contact/verification data;
- minimise relation traversal that would accidentally construct a dossier;
- preserve consent, refusal, correction and authority boundaries where material;
- do not convert cryptographic identity into permission to publish;
- do not make global participation in THR necessary for ordinary dignity, correction or
  access to public records.

```text
IDENTIFIABLE != ENTITLED_TO_AGGREGATE
VERIFIABLE != PUBLIC
PUBLIC_SOURCE != DOSSIER_PERMISSION
BETTER LINKAGE != BETTER FUTURE
```

A mature THR may intentionally use different identity mechanics for:
- physical/historical objects;
- deceased historical subjects;
- institutions;
- living humans;
- communities;
- artificial agents.

One global person-number is not the default design target.

---

## 9. Threat model

The architecture must be useful even when some participants are wrong, compromised,
self-interested or malicious.

### Threat: identifier spoofing

An attacker creates a lookalike ID or claims two IDs are one thing.

Response:
- opaque IDs;
- explicit merge/split history;
- signed/attributed mapping assertions where available;
- identity remains evidence-bearing and correctable.

### Threat: key compromise

An attacker obtains a principal's signing key.

Response:
- key history;
- rotation/revocation;
- bounded authority;
- later compromise must not automatically erase earlier evidence or silently validate
  new claims.

### Threat: sybil repetition

Thousands of synthetic endpoints repeat one origin.

Response:
- ancestry and independence graph;
- copies do not become independent evidence merely through count.

### Threat: retroactive source rewrite

A live source changes or is compromised.

Response:
- observations;
- digests;
- preservation routes;
- independent historical copies/checkpoints.

### Threat: compromised THR operator

An operator attempts to silently rewrite the public record.

Response target:
- public Git/history;
- exact-byte checkpoints;
- independent mirrors/witnesses;
- correction history;
- eventually replaceable operators.

### Threat: model hallucination

An AI invents a source relation, identity link or authority.

Response:
- machine proposals remain proposals;
- required source/evidence references;
- validators check structure, not truth;
- human or independent agent review where consequence warrants.

### Threat: false timestamp confidence

An old-looking timestamp is treated as proof of origin.

Response:
- timestamp type / owner / limits explicit;
- distinguish observation time, claimed creation time and anchor time.

### Threat: physical forgery

A digitally coherent provenance graph refers to a counterfeit physical object.

Response:
- physical-world observations remain separate evidence;
- independent custody/material analysis where warranted;
- digital coherence is not physical authenticity.

### Threat: privacy weaponisation

A provenance graph becomes an efficient surveillance graph.

Response:
- living-person anti-enumeration;
- record-local mentions;
- bounded publication purposes;
- restricted/private data never required for public graph completeness.

### Threat: cryptographic ageing

Algorithms weaken over decades.

Response target:
- algorithm agility;
- preserve original signatures/digests plus later migration/renewal attestations;
- do not erase old cryptographic context.

---

## 10. Core invariants

Candidate invariants for hostile testing:

```text
IDENTIFIER != IDENTITY PROOF

KEY != PRINCIPAL
SIGNATURE != TRUTH
SIGNATURE != AUTHORITY

CAPABILITY != LEGITIMACY
CREDENTIAL CUSTODY != GOVERNANCE

TIMESTAMP != ORIGIN
ANCHOR != TRUTH

URL != SOURCE
SOURCE != OBSERVATION
OBSERVATION != PRESERVED COPY
PRESERVED COPY != TRUTH

COPY COUNT != INDEPENDENCE
REPLICA != INDEPENDENT EVIDENCE

ENTITY != ASSERTION
ATTESTATION != THR ENDORSEMENT
ASSERTION != TRUTH

CURRENT STATE != HISTORICAL STATE
CORRECTION != ERASURE

PROCESS RECEIPT != RESULT VALIDITY
VALIDATOR PASS != TRUTH

AUTHENTICITY != TRUTH
PROVENANCE != MORAL AUTHORITY

IDENTIFIABLE != PERMISSION TO PROFILE
PUBLIC != PERMISSION TO AGGREGATE

THR MUST NOT REQUIRE TRUST IN THR
```

The final line is a design direction, not a claim that the current small repository has
already achieved decentralised trust.

---

## 11. What "THR must not require trust in THR" means

A future reader should be able to separate:

- what THR observed;
- what a source claimed;
- what THR inferred;
- who attested;
- which process generated a state;
- which bytes were preserved;
- which independent owners hold related evidence;
- what changed;
- which parts cannot be independently checked.

The strongest possible answer is not:

> THR certifies this as true.

It is:

> Here is the inspectable ancestry and the remaining uncertainty. You can continue the
> investigation without needing the original THR operator to be honest, online or alive.

---

## 12. The current four records as architecture probes

Do not add a fifth public record merely to exercise this RFC.

Use the existing four as hostile test vectors.

### Camp Fire

Can the grammar represent:
- physical work identity;
- Met owner-source attribution;
- digital image observation;
- byte-identical project copy;
- rights basis;
- custody/preservation;
- a future independent physical/material observation;
- a record/view generation process;

without turning any one of them into an authenticity certificate?

### Viral flak claim

Can it represent:
- one originating claim;
- derivative propagation;
- source ancestry;
- challenge;
- corrected/contradictory downstream statements;
- bounded checked aperture;
- unknown aggregate truth;

without counting copies as corroboration?

### Sieve/riddle revival

Can it represent:
- a living practice;
- strongest current status owner;
- reported transmission events;
- uncertain reconstruction/transmission boundary;
- public attention versus actual skill continuation;
- living practitioners without constructing universal profiles?

### Hannibal

Can it represent:
- modern entity convention;
- source-literal mentions;
- attributed ancient assertions;
- translations/read surfaces;
- lost intermediates;
- source evaluation by another historical source;
- incomplete genealogy;

without turning the graph into a biography oracle?

If the candidate grammar cannot represent all four without flattening their different
epistemic structures, the grammar is too rigid.

---

## 13. First implementation path

Do **not** implement all candidate object types now.

The next earned steps are:

### Phase A — paper falsification

1. Map each existing record onto the candidate recursive grammar.
2. List information lost or distorted by the mapping.
3. Try to create:
   - false independence;
   - false authority;
   - false temporal priority;
   - a living-person dossier;
   - a signature-as-truth failure;
   - a compromised-operator rewrite.
4. Repair the RFC only where the current records expose a real gap.

### Phase B — self-description microcase

If Phase A survives, add one bounded internal microcase rather than a fifth public
historical record:

> Can THR describe one of its own validator executions without claiming that the validator
> establishes truth?

Candidate chain:

```text
VALIDATOR SOURCE VERSION
-> PROCESS INSTANCE
-> INPUT CHECKPOINT
-> OUTPUT RECEIPT
-> OPERATOR / EXECUTION ENVIRONMENT
-> PASS / WARNINGS
-> PUBLIC RECORD CHECKPOINT
```

This would test event/process/attestation semantics on an object THR actually controls.

### Phase C — independent witness microcase

Only if a real independent participant exists, test whether another agent/person/store can:
- retrieve the same bounded export;
- verify byte identity;
- produce its own receipt;
- disagree about interpretation without corrupting the underlying provenance.

```text
INDEPENDENT WITNESS != SECOND COPY UNDER SAME CONTROL
```

### Phase D — registry/schema growth

Only after the previous phases expose repeated cross-record need should THR add shared:
- event;
- process;
- principal;
- attestation;
- anchor

registries or schema requirements.

---

## 14. What not to build yet

Do not build by momentum:

- a blockchain;
- a token;
- a universal human identifier;
- a global reputation score;
- a central certificate authority;
- a "truth score";
- biometric identity infrastructure;
- a giant property graph of living people;
- mandatory cryptographic signing for every source;
- a custom archive replacing stronger preservation institutions;
- an AI authenticity detector;
- a public API merely because IDs resemble API-addressable objects.

```text
ARCHITECTURAL POSSIBILITY != EARNED IMPLEMENTATION
```

---

## 15. Open questions

The RFC is deliberately incomplete.

Questions that need real pressure:

1. Which object classes genuinely need globally durable THR IDs versus record-local IDs?
2. What is the minimum principal model that does not become a personhood/identity system?
3. How should key rotation and historical signature verification be represented?
4. How can distributed mirrors witness a checkpoint without becoming fake "independent
   evidence"?
5. How should temporal ordering work when source publication time, observation time,
   event time and anchor time differ?
6. What is the smallest process receipt useful across different record types?
7. Which authority claims deserve explicit typed representation?
8. How can restricted/community-held evidence participate without leaking its existence or
   contents?
9. When does an event deserve its own object rather than remaining an assertion within a
   record?
10. How should THR expose competing interpretations of one evidence graph without
    pretending they are equivalent?
11. What cryptographic renewal strategy is adequate for decades-long preservation?
12. How can public exports remain usable if thehumanrecord.net, GitHub and the current
    founder all disappear?

---

## 16. Success condition for this RFC

This RFC is not successful because it sounds comprehensive.

It earns implementation only if it helps the current project survive concrete hostile
cases while preserving its existing boundaries.

The near-term test is:

```text
CURRENT FOUR RECORDS
+ CURRENT IDENTITY / SOURCE / ASSERTION MODELS
+ HOSTILE SYNTHETIC-ERA THREAT CASES
-> DOES THE RECURSIVE GRAMMAR PRESERVE MORE ANSWERABILITY
   WITHOUT CREATING FALSE AUTHORITY OR NEW SURVEILLANCE?
```

If no, revise or stop.

If yes, implement the smallest repeated need first.

```text
COMPREHENSIVE PURPOSE != COLLECT EVERYTHING NOW
FRACTAL ARCHITECTURE != INFINITE RECORD EXPANSION
THR PROTOCOL != THR AUTHORITY
```
