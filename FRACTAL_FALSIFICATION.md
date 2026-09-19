# The Human Record — fractal architecture falsification pass 1

Status: **HOSTILE PAPER TEST / RFC EVIDENCE / NOT RECORD EVIDENCE / NOT CANON**

Date: 19 September 2026

Target RFC:
`FRACTAL_ARCHITECTURE.md`

Source state tested:
THR main `1f5a5919938f385f43f1e2383bdfbb52807b206e`

Records tested:
1. `specimen.json` — Camp Fire artwork/provenance specimen;
2. `cases/viral-flak-claim.json` — claim-provenance case;
3. `cases/sieve-riddle-revival.json` — living-practice transmission lineage;
4. `cases/hannibal-barca.json` — historical-person source-survival case.

Purpose:

> Try to make the proposed recursive grammar lose information, manufacture authority,
> create false independence, force local objects into global identity, or weaken the
> living-person boundary.

This is a design falsification pass, not evidence that the RFC is correct.

---

## 1. Cross-record result

The proposed direction survives only if it preserves this rule:

```text
EVERYTHING MAY BE RECORDABLE
!=
EVERYTHING MUST BECOME A GLOBAL RECORD OBJECT
```

The four current records repeatedly use record-local structures because global identity
would add little value or create harm.

Therefore a fractal THR needs at least three addressability levels:

```text
LOCAL VALUE / LOCAL NODE
-> meaningful only inside one bounded record

LOCAL ADDRESSABLE OBJECT
-> stable within one record / export

SHARED THR OBJECT
-> cross-record durable identifier earned by repeated need
```

The RFC should not treat globally durable IDs as the default simply because an object can
be named.

---

## 2. Camp Fire — artwork/provenance specimen

Current machine record contains:
- artefact description;
- owner-source observations;
- project copy;
- byte reconciliation;
- rights layers;
- selection provenance;
- witness;
- correction history;
- epistemic boundaries.

### What the recursive grammar handles well

Candidate process objects could represent:
- owner-source retrieval;
- image-byte comparison;
- reconciliation;
- public-view generation;
- future validator execution.

Candidate attestations could represent:
- a museum publishing an attribution;
- THR recording that it observed the museum API response;
- a project operator recording a byte-comparison result.

Candidate anchors could represent:
- exact source bytes/digests;
- signed Git history;
- preserved third-party copies where legitimate.

### Failure attempt A — museum attribution becomes object identity

Bad flattening:

```text
WORK ENTITY
creator = Winslow Homer
```

This loses the current distinction that the Met **attributes** the work to Homer.

Required preservation:

```text
WORK ENTITY
<- ASSERTION: creator_attribution
<- SOURCE / OBSERVATION
<- possible owner/institution attestation
```

Result:
**RFC survives only if assertions remain separate from entity identity.**

### Failure attempt B — byte identity becomes authenticity

The current record observes byte-identical image copies.

Bad inference:

```text
SHA256 MATCH
-> IMAGE AUTHENTIC
-> WORK AUTHENTIC
```

Required:

```text
BYTE MATCH
-> same observed bytes
ONLY
```

Result:
**content-addressing cannot be presented as provenance completion.**

### Failure attempt C — project witness becomes authority

The specimen has a `witness` block.

Bad promotion:

```text
THR OPERATOR WITNESSED RECONCILIATION
-> THR CERTIFIES WORK
```

Required:
a future process/attestation object must preserve:
- who performed the comparison;
- what was compared;
- method;
- result;
- limits;

without upgrading the operator into art-historical authority.

### New RFC pressure from Camp Fire

The proposed `attestation` concept needs a typed **attestation subject**:

```text
ATTESTS TO BYTES / PROCESS RESULT
!=
ATTESTS TO PROPOSITION ABOUT WORLD
```

A signature over a reconciliation receipt must not silently sign the museum attribution.

---

## 3. Viral flak claim — propagation/provenance case

Current record contains:
- one bounded primary claim;
- nine heterogeneous nodes;
- derivative/repetition relationships;
- review receipts;
- challenges;
- changed scopes;
- unknowns/not-checked;
- current finding `unsupported_in_sources_checked`;
- explicit historical-truth status `unknown`.

### What the recursive grammar handles well

The current record strongly supports:
- claim objects;
- source ancestry;
- derivative relationships;
- correction/challenge events;
- process receipts for source review;
- claim-level independence.

### Failure attempt A — every node becomes an entity/event

The nine nodes are intentionally heterogeneous.

Bad migration:

```text
FOR EACH node
-> CREATE GLOBAL ENTITY
-> CREATE GLOBAL EVENT
```

This creates registry noise and false permanence.

Required:
most propagation nodes may remain record-local until reused elsewhere.

Result:
**global object creation must be demand-driven.**

### Failure attempt B — URL count becomes evidence count

The current case already demonstrates:

```text
MANY URLS
-> shared origin
-> NOT independent corroboration
```

A federated THR could make this worse if ten replicas each re-attest the same copied claim.

Required:

```text
REPLICA COUNT
!=
EVIDENTIARY INDEPENDENCE
```

and:

```text
ATTESTATION INDEPENDENCE
must be evaluated relative to
WHAT IS BEING ATTESTED
```

Ten independent mirrors can independently attest that they possess the same bytes.
They cannot thereby become ten independent witnesses to the historical mortality claim.

### Failure attempt C — review process becomes world observation

A THR reviewer checks sources and finds no support.

Bad process model:

```text
REVIEW PROCESS PASS
-> CLAIM FALSE
```

Required:

```text
REVIEW PROCESS
-> establishes bounded checked aperture
-> may support "unsupported_in_sources_checked"
-> does not establish historical falsehood
```

### New RFC pressure from flak case

Independence must be **typed by proposition/evidentiary function**.

Candidate future relation:

```text
independent_for:
- byte custody
- source retrieval
- physical observation
- claim origination
- analysis
- governance
```

Do not add this schema yet; first preserve the requirement.

---

## 4. Sieve/riddle revival — living-practice lineage

Current record contains:
- living practice status;
- strongest current status owner;
- public-source nodes;
- six lineage events;
- source independence groups;
- authority/consent boundary;
- practitioner-contact ceiling;
- explicit separation between attention pathway and skill transmission.

### What the recursive grammar handles well

A future event layer could represent:
- reported last-maker state;
- extinction classification;
- revival/training events;
- later status checks.

Authority representation could help distinguish:
- Heritage Crafts as current status owner;
- public reporters;
- THR;
- practitioners;
- future community/stewardship authorities.

### Failure attempt A — living practitioner becomes public principal

Bad extraction:

```text
NAME APPEARS IN LINEAGE
-> CREATE thr:principal
-> LINK ALL FUTURE RECORDS
```

This creates the surveillance graph the current project explicitly resists.

Required:

```text
LIVING MENTION
-> may remain local/public mention
-> no shared identity/principal unless cross-record need + legitimate purpose
```

Result:
**principal creation must inherit living-person anti-enumeration.**

### Failure attempt B — strongest owner becomes governance authority

Heritage Crafts is the strongest identified owner for current status.

Bad promotion:

```text
STATUS OWNER
-> GOVERNANCE AUTHORITY OVER PRACTICE
```

Required:

```text
AUTHORITY TYPE = bounded claim/status authority
NOT universal cultural ownership
NOT practitioner consent
NOT governance of THR
```

Result:
**authority must be scoped by function and claim.**

### Failure attempt C — event identity implies event certainty

The record has `lineage_events`, some based on public reporting.

Bad migration:

```text
thr:event:<id>
-> event definitely occurred exactly as represented
```

Required:

```text
EVENT REFERENT
!=
CLAIM EVENT OCCURRED
```

The event object can provide a stable referent for competing assertions without proving
the event.

### New RFC pressure from sieve/riddle

The RFC needs an explicit distinction:

```text
EVENT OBJECT
= addressable subject of claims

EVENT ASSERTION
= evidence-bearing proposition about occurrence/time/participants
```

And:

```text
AUTHORITY IS TYPED + SCOPED
NOT GLOBAL
```

---

## 5. Hannibal — historical-person source-survival case

This is already the closest current record to the shared registry architecture.

It contains:
- shared historical entity;
- two checked sources;
- source-literal mentions;
- candidate identity resolution;
- five assertions;
- source relationships;
- explicit inspection boundaries;
- rights/custody boundary.

### What the recursive grammar handles well

It demonstrates why:
- entity;
- mention;
- source;
- observation;
- assertion;

must remain distinct.

It also provides real pressure for:
- historical source genealogy;
- lost intermediates;
- translation/read-surface processes;
- competing source evaluation.

### Failure attempt A — ancient author becomes modern attesting principal

Polybius reports claims about his own investigation and other sources.

Bad conversion:

```text
Polybius
-> thr:principal
-> signed-style attestation semantics
```

There is no cryptographic or modern formal attestation event here.

Required:
the system may represent:
- historical author/source entity;
- source statement;
- reported investigative method;

without pretending a modern attestation protocol existed.

Result:
**attestation is one possible evidence form, not the universal wrapper around all source statements.**

### Failure attempt B — translation/read surface disappears

A modern English read surface is not identical to the lost/ancient carrier.

Bad graph:

```text
POLYBIUS ASSERTION
-> ancient text directly observed
```

Required process chain may eventually need:

```text
ANCIENT WORK
-> surviving textual tradition
-> edition / translation / reading surface
-> THR observation
-> assertion extraction
```

Unknown links must remain unknown.

### Failure attempt C — reported method becomes direct observation

Polybius says he questioned people and inspected the route.

Bad promotion:

```text
THR SOURCE OBSERVATION
-> THR OBSERVED ANCIENT INTERVIEWS
```

Required:
the reported method remains an assertion attributed to the source.

### New RFC pressure from Hannibal

A process layer must support:

```text
PROCESS CLAIMED BY SOURCE
!=
PROCESS OBSERVED BY THR
```

The recursive grammar therefore needs **process referents plus assertions about processes**,
not only executable modern process receipts.

---

## 6. Cross-cutting failure: "everything is an attestation"

The first RFC risks making `attestation` too attractive.

The four records show at least four distinct things:

1. a source states a proposition;
2. THR observes a source representation;
3. a principal signs or formally attests something;
4. THR executes a process and records a receipt.

These must not collapse.

```text
SOURCE STATEMENT
!=
OBSERVATION
!=
ATTESTATION
!=
PROCESS RECEIPT
```

An attestation should be used only where an actor genuinely performs an act of attesting,
not as a generic wrapper for all evidence.

---

## 7. Cross-cutting failure: recursive explosion

The fractal metaphor can become an excuse to record everything about everything.

Example:

```text
SOURCE
-> publisher
-> employee
-> software
-> dependency
-> dependency maintainer
-> their machine
-> ...
```

That is not a record architecture; it is uncontrolled graph expansion.

Required materiality rule:

> Recurse only when the next layer could materially change identity, evidence,
> independence, authority, correction, preservation or interpretation for the bounded
> question.

Candidate invariant:

```text
RECURSION POSSIBLE
!=
RECURSION MATERIAL
```

and:

```text
NO MATERIAL CONSEQUENCE
-> STOP DESCENT
```

This should be promoted into the RFC.

---

## 8. Cross-cutting failure: one universal object grammar

The records differ for good reasons.

Camp Fire needs:
- physical/digital reconciliation and rights.

Flak needs:
- claim propagation and bounded negative finding.

Sieve/riddle needs:
- living-practice/authority boundaries and lineage.

Hannibal needs:
- source-literal mentions, historical source genealogy and translation boundaries.

Therefore:

```text
COMMON ADDRESSING / RELATION PRINCIPLES
!=
ONE UNIVERSAL RECORD SCHEMA
```

The fractal model should specify shared interfaces at the joins, not flatten every record
into identical triples.

---

## 9. Cross-cutting failure: authority without time

Authority can change.

Examples:
- an institution changes custodianship;
- a status owner changes method;
- a project steward is replaced;
- a key rotates;
- a source is superseded.

Candidate requirement:

```text
AUTHORITY CLAIM
must be capable of carrying
VALID / OBSERVED / CLAIMED TIME SCOPE
```

But:

```text
LATER AUTHORITY
!=
RETROACTIVE CONTROL OF ALL EARLIER STATES
```

EvidenceWatch's temporal-authority repair is a useful engineering analogy, not an automatic
THR schema import.

---

## 10. Cross-cutting failure: one global trust score

The four records demonstrate that trust is multidimensional.

An institution may be:
- authoritative for custody;
- derivative for a historical claim;
- independent for a new physical measurement;
- not authoritative for cultural legitimacy.

Therefore do not build:

```text
trust_score: 0.94
```

as the core architecture.

Prefer inspectable relations and bounded authority claims.

---

## 11. Required RFC repairs before any implementation

Pass 1 earns the following textual repairs to the RFC:

1. Add the three-level addressability distinction:
   - local value/node;
   - record-local addressable object;
   - shared THR object.

2. Make recursion materiality explicit:
   `RECURSION POSSIBLE != RECURSION MATERIAL`.

3. Clarify event semantics:
   `EVENT OBJECT != ASSERTION EVENT OCCURRED`.

4. Clarify process semantics:
   `PROCESS CLAIMED BY SOURCE != PROCESS OBSERVED / EXECUTED BY THR`.

5. Clarify attestation semantics:
   source statement / observation / attestation / process receipt are distinct.

6. Require typed/scoped authority rather than universal authority.

7. State that independence is proposition/function-specific.

8. State that shared interfaces do not imply one universal record schema.

9. Require time scope on material authority claims.

10. Explicitly reject universal trust scoring.

These are architecture corrections, not registry/schema changes.

---

## 12. Current verdict

```text
FRACTAL DIRECTION = SURVIVES FIRST PASS
CURRENT RFC = REPAIR REQUIRED BEFORE MICROCASE
CURRENT REGISTRY CHANGE = NOT EARNED
FIFTH PUBLIC RECORD = NOT EARNED
CRYPTO / PKI BUILD = NOT EARNED
```

The strongest next move is **not** adding more object types.

It is:
1. repair the RFC with the ten earned constraints above;
2. rerun the four-record paper test;
3. then attempt the self-description validator microcase.

---

## 13. Why this matters to the synthetic-era problem

The current records show why provenance cannot be reduced to watermarking or a single
origin token.

A robust system needs to preserve different questions separately:

```text
WHICH BYTES?
WHO PUBLISHED THEM?
WHO OBSERVED THEM?
WHAT DOES THE SOURCE SAY?
WHAT PROCESS PRODUCED THIS DERIVATIVE?
WHAT CLAIM IS THR MAKING?
WHAT AUTHORITY IS RELEVANT TO THAT CLAIM?
WHICH EVIDENCE IS INDEPENDENT FOR THAT PARTICULAR QUESTION?
WHAT CHANGED?
WHAT REMAINS UNKNOWN?
```

A synthetic artifact can carry a valid watermark and still make a false claim.

A human artifact can lack a watermark and still have strong independent ancestry.

The target is therefore not:

```text
AI OR HUMAN?
```

It is:

```text
CAN THE OBJECT / CLAIM / PROCESS STILL ANSWER FOR ITS ANCESTRY?
```

That is the burden this RFC is trying to make tractable.
