# The Human Record — surviving residue attack

Status: **HOSTILE SUBTRACTION / LIVE CORRECTION-ROUTING MICROCASE / NOT CANON / NO NEW REGISTRY SEMANTICS**

Date: 19 September 2026

Target:
FRACTAL_ARCHITECTURE.md

Question:

> After stronger-owner subtraction, does THR actually need to own
> "evidentiary independence" or "correction propagation" as generic concepts?

Current answer:

~~~text
UNIVERSAL INDEPENDENCE ONTOLOGY = NOT EARNED
GENERIC CORRECTION-PROPAGATION ONTOLOGY = NOT EARNED

QUESTION-SPECIFIC INDEPENDENCE ASSESSMENT = STILL USEFUL
LOAD-BEARING CORRECTION IMPACT ROUTING = STILL USEFUL
~~~

Those surviving functions fit inside current THR assertion/source/correction machinery.
No new global type is earned.

---

## 1. Stronger owners already carry most dependency structure

### W3C PROV

Official source:
https://www.w3.org/TR/prov-o/

PROV already carries:
- derivation;
- revision;
- quotation / primary-source ancestry;
- usage / generation;
- influence;
- invalidation.

Important boundary:

~~~text
PROV INVALIDATION
!=
EPISTEMIC RETRACTION / CORRECTION BY DEFAULT
~~~

PROV invalidation means an entity becomes unavailable for use after an invalidating
activity. It should not be reused as a generic "this claim was shown false" relation.

### CRMinf

Official sources:
- https://cidoc-crm.org/crminf
- https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.2.1.html

CRMinf explicitly models premise -> inference-making -> conclusion relationships.

Its I5 Inference Making scope note says the model enables tracing dependency from a
conclusion back through premises and subsequent inferences, including narrowing the range
of influence of a revision at an intermediate stage.

That is very close to the generic dependency mechanism THR would otherwise be tempted to
invent for correction propagation.

### Crossmark / Crossref

Official sources:
- https://www.crossref.org/services/crossmark/
- https://www.crossref.org/documentation/principles-practices/best-practices/versioning
- https://www.crossref.org/documentation/register-maintain-records/maintaining-your-metadata/registering-updates/

Crossmark provides a domain-specific owner for the current status of scholarly content,
including corrections, retractions, withdrawals and other editorially significant
updates. Crossref's best practice preserves a separate correction/retraction notice and
links it to the item being updated rather than silently overwriting the original.

This is not a universal THR correction model, but it is a strong owner wherever a THR
source is already a Crossref-managed research output.

### Nanopublication patterns

Community sources:
- https://nanopub.net/guidelines/working_draft/
- https://github.com/knowledgepixels/nanopub-http

Nanopublications are immutable publication objects with established supersession and
retraction patterns in current tooling.

Again:

~~~text
EXISTING UPDATE / SUPERSESSION PATTERN
!=
THR SHOULD REIMPLEMENT IT
~~~

---

## 2. Independence should shrink again

The first RFC said:

> independence is a graph property, not a count.

That is still too strong.

A graph can show:
- known common ancestry;
- known distinct capture events;
- common process/tool;
- shared owner;
- shared stated source;
- separate custody;
- unknown relationship.

But absence of a known common ancestor does not prove independence.

And independence always needs a question.

Two archives can be independent for custody while wholly dependent for attribution.
Two photographs can be separate physical captures while sharing the same false caption.
Two models can be separate runtimes while sharing training/data ancestry material to the
bounded claim.

Therefore:

~~~text
INDEPENDENCE
!=
INTRINSIC SOURCE PROPERTY

NO KNOWN COMMON ANCESTOR
!=
INDEPENDENT

DISTINCT URL
!=
INDEPENDENT

DISTINCT INSTITUTION
!=
INDEPENDENT

DISTINCT MODEL / AGENT
!=
INDEPENDENT
~~~

The more accurate formulation is:

~~~text
INDEPENDENCE ASSESSMENT
= BOUNDED CLAIM
  ABOUT A DECLARED QUESTION / FUNCTION
  SUPPORTED BY ANCESTRY / OBSERVATION / CUSTODY / PROCESS EVIDENCE
  WITH UNKNOWN RELATIONS PRESERVED
~~~

THR already has enough conceptual machinery to carry such a finding as an assertion or
record-local analysis.

It does not need:
- a global independence object;
- a universal independence score;
- a global pairwise independence matrix;
- a rule that absence of a known edge means independence.

### Consequence

Replace:

~~~text
INDEPENDENCE IS A GRAPH PROPERTY
~~~

with:

~~~text
ANCESTRY / PROCESS / CUSTODY GRAPH
-> EVIDENCE FOR A BOUNDED INDEPENDENCE ASSESSMENT

GRAPH != INDEPENDENCE VERDICT
~~~

---

## 3. "Correction propagation" should become impact routing

A correction to an upstream proposition does not automatically tell us the correct state
of every downstream proposition.

Example:

~~~text
P PREMISE CORRECTED
Q DEPENDED ON P
~~~

It does not follow that:

~~~text
Q = FALSE
Q = CORRECTED AUTOMATICALLY
~~~

The safe generic consequence is narrower:

~~~text
LOAD-BEARING DEPENDENCY CHANGED
-> DOWNSTREAM REVIEW REQUIRED
~~~

until the downstream claim is reassessed.

Preserve:

~~~text
UPSTREAM CORRECTION
!=
DOWNSTREAM CORRECTION

DEPENDENCY TOUCHED
!=
DESCENDANT FALSE

REVIEW REQUIRED
!=
INVALID

CORRECTION ROUTED
!=
CORRECTION COMPLETED
~~~

CRMinf / PROV can carry much of the dependency graph. Crossmark, nanopublication or other
domain owners can carry domain-native correction/supersession state where they already
apply.

THR's surviving job is therefore not to define a universal propagation ontology.

It is:

1. know which THR assertions/views materially depended on the changed object;
2. distinguish current surfaces from historical receipts;
3. route current dependents to review;
4. preserve earlier states;
5. record the later reassessment without pretending that the corrected answer was known
   at the earlier time.

This is a **correction-impact query / review-state function**.

It may eventually be automated.

That does not make it a new ontology.

---

## 4. Live correction-routing microcase — PR #52 itself

This RFC produced its own useful specimen.

### T0 — first PROV mapping

The first examples/fractal-validator-run.prov.ttl:
- parsed successfully;
- represented a validation activity;
- called the later THR JSON receipt an entity generated by the historical validator run;
- mapped GitHub run updated_at to prov:endedAtTime.

The Turtle parsed as 42 triples.

### T1 — independent answer-back

Codex comment:
human-record#52 issuecomment-5744776818

found two semantic defects:

1. the THR JSON receipt was first introduced in Git commit
   0b74aea9c559ad29737057898f4accec23cac6ef at
   2026-09-19T19:22:29Z, after the historical GitHub validation run;
2. run_updated_at is not evidence for an exact PROV activity end-time.

Therefore:

~~~text
RDF PARSES
!=
PROVENANCE CLAIM TRUE
~~~

### T2 — direct repair

The branch was repaired so:

~~~text
VALIDATION ACTIVITY
-> GENERATES GITHUB OPERATIONAL OUTPUT

LATER THR JSON RECEIPT
-> DERIVED FROM GITHUB OPERATIONAL OUTPUT
-> FIRST INTRODUCED IN A LATER GIT COMMIT
~~~

The unsupported PROV start/end time claims were removed from the Turtle.

The JSON receipt now explicitly bounds run_started_at / run_updated_at as GitHub metadata
fields rather than exact PROV activity start/end claims.

The repaired Turtle parses as 48 triples.

### T3 — impact routing

The direct source repair creates different consequences for different dependents.

#### Current surfaces

Current summaries that claim:
- exact branch head;
- 42 triples;
- the old generation relationship;
- start/end-time mapping;

must be revised because they are intended to describe current state.

#### Historical receipts

The dated COM receipt:

coordination/build_ledger/THR_FRACTAL_PROV_INTEROP_20260919.md

is evidence of what was believed / recorded at T0.

It should **not** be silently rewritten to make the earlier mistake disappear.

Instead:
- preserve the old receipt;
- issue a later correction receipt;
- make current hot surfaces point to the correction.

This yields an important distinction:

~~~text
CURRENT SURFACE STALE
-> UPDATE CURRENT SURFACE

HISTORICAL RECEIPT WRONG IN RETROSPECT
-> PRESERVE RECEIPT
-> APPEND CORRECTION / SUPERSESSION ROUTE

CORRECTION
!=
HISTORY REWRITE
~~~

This is correction routing in real use, not a paper schema exercise.

---

## 5. Existing THR machinery is probably enough for now

Current SOURCE_MODEL.md already carries evidence-bearing ancestry relations such as:
- cites;
- quotes;
- summarizes;
- derives_from;
- mirrors;
- reposts;
- transcodes;
- same_institutional_owner;
- relation_unknown.

Current ASSERTION_MODEL.md already:
- allows assertions about assertions;
- carries evidence/source/observation refs;
- includes superseded;
- preserves correction references;
- requires re-evaluation rather than blind movement after identity correction.

That is enough to test the next layer without adding:
- an independence registry;
- a correction-propagation registry;
- a dependency ontology;
- a universal review-state ontology.

A future implementation can derive a local review queue from existing evidence relations
if real scale makes that useful.

---

## 6. Revised residue

After this attack, replace:

~~~text
PRESERVE CORRECTION PROPAGATION
PRESERVE QUESTION-SPECIFIC INDEPENDENCE
~~~

with the narrower:

~~~text
PRESERVE EVIDENCE NEEDED TO ASSESS INDEPENDENCE
FOR THE QUESTION ACTUALLY BEING ASKED

ROUTE LOAD-BEARING CORRECTIONS TO AFFECTED DEPENDENTS
WITHOUT AUTO-CORRECTING THEM
~~~

A tighter working compression is now:

~~~text
THR VALUE HYPOTHESIS
=
PRESERVE MATERIAL JOINS
+ PRESERVE EVIDENCE CEILINGS
+ PRESERVE CORRECTABLE HISTORY
+ ROUTE MATERIAL CHANGE TO THE PLACES THAT NEED RE-EXAMINATION
+ KEEP THE INQUIRY CONTINUABLE WITHOUT TRUSTING THR
~~~

Still a hypothesis.

---

## 7. Continuation without trusting THR — stronger-owner subtraction

The remaining phrase:

> can a future reader continue without trusting the current THR operator?

is important, but it should not silently become a new THR archival protocol.

Mature preservation / portability owners already cover much of the mechanism.

### OAIS

Current OAIS Reference Model:
https://ccsds.org/Pubs/650x0m3.pdf

OAIS already treats long-term understandability as requiring Representation Information
and Preservation Description Information, including:
- provenance;
- context;
- reference;
- fixity;
- access-rights information.

That is extremely close to the generic "future reader can still make sense of the object"
problem.

### OCFL

Official source:
https://ocfl.io/

OCFL owns an application-independent layout for versioned digital objects. Prior object
versions are intended to remain immutable, with inventories and fixity support.

### BagIt

Official source:
https://www.rfc-editor.org/rfc/rfc8493

BagIt already owns a simple transfer/storage package with payload manifests and checksums.

### RO-Crate

Official source:
https://www.researchobject.org/ro-crate/specification

RO-Crate provides an existing JSON-LD packaging pattern for a bounded object plus
human/machine-readable contextual metadata.

### LOCKSS

Official sources:
- https://www.lockss.org/about/preservation-principles
- https://www.lockss.org/use-lockss/how-lockss-works

LOCKSS explicitly addresses preservation across independent / mutually distrusting peers,
and rejects one canonical fixity store as a central point of failure.

### THR consequence

THR should not build by momentum:
- a custom archival package;
- a custom fixity format;
- an OCFL replacement;
- a BagIt replacement;
- a custom distributed-consensus preservation network;
- a mandatory THR resolver;
- a federation protocol merely because "fractal" sounds distributed.

The correct architecture rule is narrower:

~~~text
CONTINUATION WITHOUT TRUSTING THR
= ACCEPTANCE CRITERION

NOT
= THR MUST OWN THE PRESERVATION STACK
~~~

A future export can use whichever stronger owners fit the actual object.

For example:

~~~text
THR RECORD / BOUNDED EXPORT
-> CURRENT THR MACHINE/HUMAN MATERIAL
-> EXTERNAL IDS / PROVENANCE LINKS
-> REPRESENTATION / CONTEXT NEEDED TO INTERPRET IT
-> FIXITY / VERSION HISTORY
-> RIGHTS / ACCESS BOUNDARY
-> OPTIONAL STRONG-OWNER PACKAGE / PRESERVATION ROUTE
~~~

The specific packaging choice should be earned by a real transfer/preservation need.

~~~text
PORTABLE != NEW CONTAINER REQUIRED
MIRRORED != INDEPENDENT EVIDENCE
DISTRIBUTED != INDEPENDENT GOVERNANCE
ARCHIVED != INTERPRETED CORRECTLY
FIXITY != TRUTH
~~~

This subtraction does not make THR empty.

It clarifies that THR's possible value is in the **epistemic joins and correction
discipline across heterogeneous owner systems**, while archival mechanics stay with
archives.

---

## 8. Revised surviving centre

After the independence, correction-routing and continuation attacks, the working centre
is now smaller again:

~~~text
THR VALUE HYPOTHESIS
=
MAKE A BOUNDED HUMAN/MACHINE RECORD WALKABLE
ACROSS HETEROGENEOUS STRONGER OWNERS

WHILE PRESERVING:
- WHAT THR ACTUALLY OBSERVED
- WHAT EACH SOURCE / EXTERNAL OBJECT ACTUALLY CLAIMS
- CLAIM SCOPE
- EVIDENCE ANCESTRY
- EVIDENCE CEILINGS / UNKNOWN
- TYPED / SCOPED / TEMPORAL AUTHORITY
- CORRECTABLE HISTORY
- REVIEW ROUTING WHEN LOAD-BEARING DEPENDENCIES CHANGE
- PRIVACY / RIGHTS / CONSENT / CULTURAL-CONTROL BOUNDARIES
- ENOUGH REPRESENTATION / CONTEXT FOR A FUTURE READER TO CONTINUE
~~~

This looks less like a new universal protocol and more like a **portable integration and
answerability discipline**.

That may be the right result.

~~~text
SMALLER ARCHITECTURE
!=
SMALLER PURPOSE

INTEGRATION VALUE
!=
ONTOLOGY NOVELTY

THR CAN BE USEFUL
WITHOUT OWNING THE LOWER LAYERS
~~~

---

## 9. New hostile question

The next cut is now very sharp:

> Does THR need any new cross-record semantic layer beyond its existing sparse
> source / observation / assertion / identity models, or is the right next architecture
> simply to make those current distinctions exportable/interoperable with stronger owners?

A valid result is:

~~~text
NO NEW CORE TYPES
NO NEW PROTOCOL
KEEP CURRENT SPARSE THR MODEL
+ INTEROP / EXPORT PROFILES WHEN REAL CASES EARN THEM
~~~

That would be a successful architecture result, not a failure to invent.


---

## 10. Prior hostile question

The remaining residue may shrink again.

Ask:

> If PROV / CIDOC / CRMinf / PREMIS / domain correction systems carry the dependency and
> history, is THR's only distinct role a readable public integration and continuation
> discipline over those systems?

If yes, that is not failure.

It may be exactly the right size.

~~~text
INTEGRATION != INVENTION
PORTABLE REASONING / CONTINUATION VALUE
!=
NEW ONTOLOGY REQUIRED
~~~

---

## 8. Current disposition

~~~text
UNIVERSAL INDEPENDENCE TYPE = NOT EARNED
UNIVERSAL INDEPENDENCE SCORE = REJECT
GENERIC CORRECTION-PROPAGATION TYPE = NOT EARNED
AUTO-CORRECTION OF DEPENDENTS = REJECT

CUSTOM THR ARCHIVAL PACKAGE = NOT EARNED
CUSTOM THR FIXITY / VERSION FORMAT = NOT EARNED
CUSTOM THR FEDERATION / PRESERVATION CONSENSUS = NOT EARNED
CONTINUATION WITHOUT TRUSTING THR = ACCEPTANCE CRITERION

BOUNDED INDEPENDENCE ASSESSMENT = KEEP
LOAD-BEARING IMPACT ROUTING = KEEP
HISTORICAL CORRECTION VISIBILITY = KEEP

NEW GLOBAL REGISTRY SEMANTICS = NONE
PUBLIC THR RECORDS = UNCHANGED
~~~
