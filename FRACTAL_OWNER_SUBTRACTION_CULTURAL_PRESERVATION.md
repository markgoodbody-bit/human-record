# The Human Record — cultural / inference / preservation owner subtraction

Status: **SECOND EXTERNAL OWNER PASS / RFC PRESSURE / NOT CANON / NO NEW REGISTRY SEMANTICS**

Date: 19 September 2026

Target:
`FRACTAL_ARCHITECTURE.md`

Purpose:

> Test whether the candidate fractal concepts called event, process, principal,
> attestation, inference and preservation are already substantially owned by mature
> cultural-heritage, digital-provenance and preservation models.

This is not a conformance claim and it is not a decision to migrate THR to RDF.

The question is narrower:

```text
IF A STRONGER OWNER ALREADY MODELS THE GENERIC THING
THR SHOULD PRESERVE THE JOIN / EVIDENCE CEILING / CORRECTION RESIDUE
NOT MINT A PARALLEL UNIVERSAL TYPE
```

---

## 1. CIDOC CRM — cultural-heritage things, events, actors and time

Official sources:

- https://cidoc-crm.org/get-last-official-release
- https://cidoc-crm.org/html/cidoc_crm_version_7.1.3_documentation_text.html

The current official/stable CIDOC CRM release is 7.1.3. Later 7.3.x / 7.4
documents exist as drafts.

CIDOC CRM is a formal ontology for integration, mediation and interchange of
heterogeneous cultural-heritage information. It already provides a mature event-centred
model for things, actors, activities, events, time, places, information objects,
attribute assignments, custody-like relationships and other heritage documentation
structures.

That overlaps directly with a large part of the RFC's generic candidate `event`,
`principal` and historical-object relation layer.

### THR consequence

Do not create a THR-native universal historical-event / actor / cultural-object ontology.

Where a museum, archive or heritage record needs richer event semantics, test a mapping
to CIDOC CRM first.

THR still has separate work:

```text
CRM ENTITY / EVENT REPRESENTATION
!=
THR OBSERVATION OF THAT REPRESENTATION

CRM ATTRIBUTE / RELATION
!=
CLAIM TRUE

CULTURAL-HERITAGE MODEL
!=
PUBLICATION / PRIVACY / GOVERNANCE AUTHORITY
```

The THR residue is the bounded relation between:
- what THR actually observed;
- which external object/statement was inspected;
- evidence ancestry and claim-specific independence;
- disagreement / correction / unknowns;
- authority and rights boundaries;
- downstream review consequences.

### Owner-subtraction result

```text
GENERIC CULTURAL-HERITAGE THING / EVENT / ACTOR / TIME SEMANTICS
-> STRONG OWNER FOUND: CIDOC CRM

THR-NATIVE UNIVERSAL EVENT / PRINCIPAL ONTOLOGY
-> NOT EARNED
```

---

## 2. CRMdig — digitisation, software execution and physical-measurement provenance

Official sources:

- https://cidoc-crm.org/crmdig
- https://cidoc-crm.org/node/9101
- https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html

CRMdig 5.0 is an approved CIDOC CRM extension for provenance metadata. It includes
digital objects, digitisation processes, formal derivation, software execution, digital
measurement events, devices, transfers, annotations and log-producing processes.

This cuts directly into RFC territory currently described with examples such as:
- image scan;
- OCR / transform;
- colour restoration;
- software execution;
- capture device;
- physical measurement;
- process log.

### THR consequence

For cultural/scientific digitisation provenance, a bespoke THR `process` object should
not be the default.

A THR record can instead preserve a relation to a CRMdig description where it exists or
where mapping is materially useful.

The important ceiling remains:

```text
CRMDIG PROCESS GRAPH
!=
PROCESS EXECUTION HONEST

DIGITAL MEASUREMENT PROVENANCE
!=
PHYSICAL OBJECT AUTHENTIC

DOCUMENTED TRANSFORM
!=
RESULT TRUE
```

### Owner-subtraction result

```text
DIGITISATION / SYNTHETIC-DIGITAL / PHYSICAL-MEASUREMENT PROVENANCE
-> STRONG OWNER FOUND: CRMdig

GENERIC THR PROCESS ONTOLOGY FOR THAT TERRITORY
-> NOT EARNED
```

---

## 3. CRMinf — argumentation and inference lineage

Official sources:

- https://cidoc-crm.org/crminf
- https://cidoc-crm.org/crminf/ModelVersion/crminf-1.2.1
- https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.2.1.html

CRMinf 1.2.1 is a stable CIDOC CRM extension for argumentation. It explicitly models
relationships between premises, conclusions and reasoning activities, including inference
making and the logic/method used.

That is highly material to THR because a future Human Record must be able to distinguish:

```text
SOURCE SAID P
THR OBSERVED SOURCE SAID P
P WAS USED AS PREMISE
METHOD / INFERENCE M PRODUCED CONCLUSION Q
Q WAS LATER CORRECTED
```

CRMinf already owns much of the generic premise -> inference -> conclusion graph.

### THR consequence

Do not invent a parallel universal THR inference ontology merely to make claim ancestry
walkable.

The THR-specific residue remains substantial:

```text
ARGUMENT CHAIN RECORDED
!=
ARGUMENT SOUND

INFERENCE DOCUMENTED
!=
PREMISE TRUE

BELIEF / PROPOSITION REPRESENTED
!=
THR ENDORSEMENT

SHARED PREMISE ANCESTRY
-> MAY MATTER TO EVIDENTIARY INDEPENDENCE

CORRECTION OF PREMISE
-> MAY REQUIRE DOWNSTREAM REVIEW
```

The last two are especially important. CRMinf can help represent dependency; THR still
needs the bounded operational question of which downstream Human Record material must be
revisited and what evidence ceiling remains.

### Owner-subtraction result

```text
GENERIC PREMISE / INFERENCE / CONCLUSION LINEAGE
-> STRONG OWNER FOUND: CRMinf

THR RESIDUE
-> observation boundary
-> claim-specific independence
-> correction propagation / downstream review
-> unknown / unexamined
-> authority / privacy / cultural-control boundary
```

---

## 4. PREMIS — long-term digital preservation metadata

Official source:

- https://www.loc.gov/standards/premis/v3/index.html

PREMIS 3.0 is a practical international preservation-metadata standard. Its data model
covers preservation Objects, Events, Agents and Rights, with an RDF/OWL representation
also available.

This overlaps directly with candidate THR concepts around:
- preserved digital objects;
- preservation actions/events;
- software or institutional agents;
- rights relevant to preservation;
- fixity / environment / event outcomes;
- long-term custodial process metadata.

### THR consequence

Do not turn THR into a replacement digital-preservation metadata system.

Where THR has a preservation route or preserved copy, PREMIS should be treated as a
strong external owner for detailed preservation metadata when that detail is needed.

THR should still say exactly what it has and has not established:

```text
PREMIS RECORD EXISTS
!=
OBJECT HISTORICALLY AUTHENTIC

PRESERVATION EVENT RECORDED
!=
ALL FUTURE ACCESS GUARANTEED

FIXITY PRESERVED
!=
CONTEXT PRESERVED

RIGHT RECORDED
!=
THR HAS EVERY NECESSARY PUBLICATION RIGHT
```

### Owner-subtraction result

```text
GENERIC DIGITAL-PRESERVATION OBJECT / EVENT / AGENT / RIGHTS METADATA
-> STRONG OWNER FOUND: PREMIS

THR
-> LINK / MAP / RECORD ITS OWN OBSERVATION AND EVIDENCE CEILING
```

---

## 5. Nanopublications — assertion + provenance + publication provenance packaging

Official/community sources:

- https://nanopub.net/
- https://nanopub.net/guidelines/working_draft/

Nanopublications are a community-driven semantic-web approach in which a small assertion
is packaged separately from:
1. provenance of the assertion; and
2. provenance / publication information for the nanopublication itself.

This is not the same kind of standards authority as CIDOC CRM or PREMIS, so this pass does
**not** declare a universal strongest owner.

It is nevertheless an important existing interoperability pattern because it overlaps
with THR's desire to keep:

```text
CLAIM
!=
WHY / HOW CLAIM AROSE
!=
WHO / WHEN PUBLISHED THIS CLAIM PACKAGE
```

### THR consequence

Before creating a bespoke portable assertion envelope beyond current THR needs, test
whether nanopublication packaging already carries the generic assertion/provenance split.

THR still needs distinctions nanopublication well-formedness does not settle:

```text
WELL-FORMED NANOPUBLICATION
!=
ASSERTION TRUE

PROVENANCE GRAPH
!=
EVIDENTIARY INDEPENDENCE

ATTRIBUTION
!=
LEGITIMATE AUTHORITY

PUBLICATION
!=
PERMISSION TO AGGREGATE A LIVING PERSON
```

### Owner-subtraction result

```text
ASSERTION + ASSERTION-PROVENANCE + PUBLICATION-PROVENANCE PACKAGE
-> EXISTING STRONG INTEROP PATTERN: NANOPUBLICATIONS

THR-NATIVE REPLACEMENT
-> NOT EARNED
```

---

## 6. Revised owner boundary

The first pass already owner-subtracted generic provenance, media provenance,
credentials, decentralised identifiers, software attestations, transparency logs,
web-time routing and software preservation.

This second pass removes more generic territory:

```text
CULTURAL-HERITAGE THING / EVENT / ACTOR / TIME
-> CIDOC CRM

DIGITISATION / DIGITAL DERIVATION / PHYSICAL-MEASUREMENT PROVENANCE
-> CRMdig

PREMISE / INFERENCE / CONCLUSION LINEAGE
-> CRMinf

DIGITAL PRESERVATION OBJECT / EVENT / AGENT / RIGHTS
-> PREMIS

ASSERTION / ASSERTION-PROVENANCE / PUBLICATION-PROVENANCE PACKAGING
-> NANOPUBLICATIONS (INTEROP PATTERN; NOT MANDATORY)
```

The RFC should therefore stop describing `event`, `process`, `principal`,
`attestation` and `anchor` as though THR is likely to need universal native schemas
for them.

Those words may remain useful **local conceptual roles**.

Their generic ontology should be imported, mapped or left external when a stronger owner
fits.

---

## 7. What survives as specifically THR-shaped residue

After both owner-subtraction passes, the surviving centre is smaller:

```text
WHAT DID THR ACTUALLY OBSERVE?

WHAT EXACT EXTERNAL OBJECT / STATEMENT / VERSION DID IT OBSERVE?

WHAT PROPOSITION IS LOAD-BEARING FOR THIS RECORD?

WHAT IS THE ANCESTRY OF THAT PROPOSITION?

WHICH EVIDENCE IS INDEPENDENT FOR THIS PARTICULAR QUESTION?

WHAT AUTHORITY APPLIES TO THIS PARTICULAR FUNCTION, SCOPE AND TIME?

WHAT CHANGED / WAS CORRECTED?

WHICH DOWNSTREAM RECORDS NOW REQUIRE REVIEW?

WHAT REMAINS UNKNOWN / UNEXAMINED?

WHAT RIGHTS / PRIVACY / CONSENT / CULTURAL-CONTROL BOUNDARY APPLIES?

CAN A FUTURE READER CONTINUE THE INQUIRY WITHOUT TRUSTING THE CURRENT THR OPERATOR?
```

That is not a universal ontology.

It is closer to a **continuation and answerability layer across stronger owners**.

Potentially:

```text
THR VALUE
= PRESERVE THE MATERIAL JOINS
+ PRESERVE EVIDENCE CEILINGS
+ PRESERVE CORRECTION PROPAGATION
+ PRESERVE QUESTION-SPECIFIC INDEPENDENCE
+ PRESERVE THE ABILITY TO CONTINUE ASKING WHY
```

This remains a hypothesis, not a contribution claim.

---

## 8. New falsifiers

The next review should try to show that even this residue is already adequately owned.

In particular:

1. Can CIDOC CRM + CRMinf + PREMIS + PROV already express every material join in one
   current THR record without a THR-specific relation layer?
2. Is "claim-specific independence" already better owned by argumentation/evidence
   standards we have not yet checked?
3. Is correction propagation merely dependency tracking plus ordinary version control?
4. Does living-person anti-enumeration belong entirely to access/privacy/governance
   policy rather than the record model?
5. Does "future reader can continue without trusting THR" reduce to ordinary archival
   preservation + open export + documented provenance?
6. Is a dedicated THR layer useful only because the current four records need a readable
   public synthesis, not because a new protocol is required?

A successful hostile answer may shrink THR again.

That is desirable.

---

## 9. Current disposition

```text
SECOND OWNER SUBTRACTION = MATERIAL DELTA

CIDOC CRM = STRONG OWNER FOUND
CRMdig = STRONG OWNER FOUND
CRMinf = STRONG OWNER FOUND
PREMIS = STRONG OWNER FOUND
NANOPUBLICATIONS = STRONG EXISTING INTEROP PATTERN

NEW GLOBAL THR EVENT TYPE = NOT EARNED
NEW GLOBAL THR PROCESS TYPE = NOT EARNED
NEW GLOBAL THR PRINCIPAL TYPE = NOT EARNED
NEW GLOBAL THR ATTESTATION TYPE = NOT EARNED
NEW GLOBAL THR ANCHOR TYPE = NOT EARNED

THR FRACTAL RESIDUE = SURVIVES, NARROWER AGAIN
```

Do not build another ontology because the vocabulary is available.
