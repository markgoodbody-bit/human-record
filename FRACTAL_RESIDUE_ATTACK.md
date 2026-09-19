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

## 7. New hostile question

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

BOUNDED INDEPENDENCE ASSESSMENT = KEEP
LOAD-BEARING IMPACT ROUTING = KEEP
HISTORICAL CORRECTION VISIBILITY = KEEP

NEW GLOBAL REGISTRY SEMANTICS = NONE
PUBLIC THR RECORDS = UNCHANGED
~~~
