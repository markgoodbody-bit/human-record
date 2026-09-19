# The Human Record — fractal architecture independent review packet

Status: **OPEN REVIEW PACKET / FOR HUMANS OR AI SYSTEMS / NOT AN ENDORSEMENT REQUEST**

Target branch:
`framework/fractal-thr-rfc-20260919`

Target documents:
- `FRACTAL_ARCHITECTURE.md`
- `FRACTAL_FALSIFICATION.md`
- `FRACTAL_OWNER_SUBTRACTION.md`
- `FRACTAL_OWNER_SUBTRACTION_CULTURAL_PRESERVATION.md`
- `FRACTAL_RESIDUE_ATTACK.md`
- `FRACTAL_INTEROP_PROV_MICROCASE.md`

Current public THR baseline for comparison:
main `1f5a5919938f385f43f1e2383bdfbb52807b206e`

This packet exists because a provenance/knowledge architecture that only survives its
authors' intuitions is not robust enough.

The reviewer is invited to disagree.

---

## 1. What this proposal is trying to do

The current Human Record already separates:
- entity from name;
- mention from entity;
- source from URL;
- observation from source;
- preserved copy from truth;
- assertion from entity;
- custody from governance.

The RFC asks what additional structure is needed for a synthetic-information environment
where plausible artifacts can be generated cheaply and where the history of a record,
process or source may itself become contested.

Earlier candidate concepts included event, process, principal, attestation and
anchor/checkpoint.

Two owner-subtraction passes now treat those as local conceptual roles unless a
cross-record THR-specific residue survives stronger owners such as PROV, CIDOC CRM,
CRMdig, CRMinf, PREMIS, C2PA, Crossmark or domain-specific systems.

The current residue is narrower:
- THR's own bounded observation;
- evidence ceilings;
- material joins between stronger owners;
- evidence needed for question-specific independence assessment;
- typed/scoped/temporal authority;
- correctable history;
- routing load-bearing changes to affected downstream review;
- privacy / rights / consent / cultural-control boundaries;
- continuation without trusting the current THR operator.

The proposal explicitly rejects:
- truth scores;
- universal person IDs;
- blockchain-by-default;
- mandatory signing;
- universal record schemas;
- automatic public principal creation;
- THR as central truth authority.

---

## 2. What the reviewer should try to break

### A. False authority

Find a path where:
- a signature becomes truth;
- a key-holder becomes legitimate governor;
- a museum/custodian becomes authority outside its scope;
- THR itself silently becomes certification authority.

### B. False independence

Find a path where:
- copies become witnesses;
- independent preservation becomes independent claim evidence;
- multiple AI agents trained on one source appear independent;
- mirror count becomes corroboration.

### C. Identity failure

Try to cause:
- two entities to be merged incorrectly;
- one entity to split silently;
- a living mention to become a dossier;
- a key rotation to create a new person/entity;
- an external ID to replace evidence-bearing identity resolution.

### D. Time failure

Try to confuse:
- event time;
- source publication time;
- observation time;
- signing time;
- anchor time;
- correction time;
- authority-validity time.

Look for any route where later authority rewrites earlier history.

### E. Recursive explosion

Show where the "fractal" model:
- requires infinite descent;
- records irrelevant dependencies;
- creates an unmanageable global graph;
- exposes sensitive relationships merely because they are graphable.

### F. Physical-world failure

Construct a case where:
- all digital provenance is coherent;
- the physical object/event is nevertheless counterfeit or misidentified.

Does the RFC keep that possibility visible?

### G. Compromised THR

Assume:
- thehumanrecord.net is compromised;
- the current GitHub owner is malicious;
- a validator is backdoored;
- an AI contributor hallucinates relations;
- a signing key is stolen.

What history can still be recovered, by whom, and why?

### H. Long-term decay

Assume 30–100 years pass.

Consider:
- broken URLs;
- dead organisations;
- expired certificates;
- weak hash/signature algorithms;
- obsolete software;
- missing context;
- changed names/identifiers;
- inaccessible restricted evidence.

Which parts of the architecture still work?

### I. Governance capture

Can a technically distributed network still be governed by one hidden operator?

Does the proposal separate:
- replication;
- credential custody;
- publication;
- policy;
- stewardship;
- legitimate authority?

### J. Privacy / anti-surveillance

Could an apparently benign provenance graph become:
- a people-search engine;
- a relationship map;
- a political/religious/medical inference graph;
- an irreversible identity layer?

Identify concrete protections that are missing.

### K. Residue collapse

Try to show that the surviving THR layer is still too large.

In particular:

- Is "question-specific independence" already fully handled by domain evidence methods,
  so THR should only preserve ancestry/evidence and never name independence?
- Is correction impact routing merely a query over PROV/CRMinf/dependency relations plus
  ordinary currentness handling?
- Is "continuation without trusting THR" already adequately owned by open archival
  packaging, preservation systems and documented provenance?
- Are "material joins" simply ordinary integration work rather than a THR protocol?
- Does THR need any new protocol at all, or only a readable public discipline for
  preserving these distinctions across heterogeneous owner systems?

A result of "THR should shrink to integration / continuation discipline" is valid.

The current RFC now makes a stronger provisional claim:

~~~text
NEW SHARED THR CORE TYPES NEEDED FOR CURRENT FOUR RECORDS + MICROCASES = ZERO
~~~

Try to break it.

Find one concrete consequential distinction in Camp Fire, flak, sieve/riddle, Hannibal,
the validator self-description, correction routing or long-term continuation that cannot
be preserved using:
- current sparse THR entity / mention / source / observation / assertion layers;
- record-local structures;
- stronger-owner interoperability when material.

If you find one, identify the **smallest** new shared type required.

If you do not, say so. Do not invent a type to make the review look productive.

---

## 3. Use the existing four records

Do not review only at the level of abstract diagrams.

Try the RFC against:

### Camp Fire

Can it preserve:
- physical work;
- museum attribution;
- source observations;
- byte comparison;
- rights;
- custody;
- correction;

without converting byte identity or institutional ownership into authenticity/truth?

### Viral flak claim

Can it preserve:
- source propagation;
- changed wording/scope;
- derivative lineage;
- bounded failure to find support;
- unknown aggregate truth;

without turning replicas/attestations into corroboration?

### Sieve/riddle revival

Can it preserve:
- living practice;
- reported lineage events;
- current status owner;
- uncertain transmission/reconstruction;
- living-practitioner boundaries;

without building profiles on practitioners or granting a status owner universal authority?

### Hannibal

Can it preserve:
- modern entity convention;
- source-literal mentions;
- ancient attributed assertions;
- translations/read surfaces;
- lost sources;
- incomplete genealogy;

without treating ancient source statements as modern attestations or direct THR world
observations?

---

## 4. Synthetic-era hostile cases

Please add at least one case not already covered.

Examples:

### Fake historical image with forged metadata

The image carries:
- convincing EXIF;
- old-looking timestamp;
- fake institutional webpage;
- many derivative copies.

What could THR establish and what must remain unknown?

### Genuine human work falsely accused of being AI

Can the architecture preserve positive ancestry evidence without requiring an AI detector?

### AI-generated work honestly disclosed

Can THR preserve its provenance without treating AI origin as defect or inauthenticity?

### Institution compromised after decades of legitimate custody

Can later compromise be represented without destroying all prior evidence?

### Two honest institutions disagree

Can both states remain visible without forcing a false consensus?

---

## 5. Review rules

Do not:
- assume the RFC must survive;
- reward complexity;
- propose a blockchain merely because immutability matters;
- propose global identity merely because matching is convenient;
- convert cryptographic validity into epistemic validity;
- collect private/living-person data to improve a toy example;
- insist every conceptual object become a registry/schema type now.

Prefer:
- smallest missing distinctions;
- explicit failure states;
- interoperability with stronger owners;
- removable/reversible mechanisms;
- independent falsification;
- preservation of uncertainty.

---

## 6. Requested response

Please return:

```text
THR FRACTAL REVIEW

TARGET_HEAD:
HEAD_MATCH: YES / NO

SUMMARY:
<what you think the RFC is actually trying to accomplish>

BLOCKERS:
- ...

FALSE_AUTHORITY_PATHS:
- ...

FALSE_INDEPENDENCE_PATHS:
- ...

IDENTITY_PRIVACY_RISKS:
- ...

TIME_CORRECTION_RISKS:
- ...

DISTRIBUTED_SURVIVAL:
- ...

PHYSICAL_WORLD_GAPS:
- ...

CURRENT_FOUR_RECORDS:
Camp Fire:
Flak:
Sieve/riddle:
Hannibal:

MISSING_CASE:
<one hostile case + outcome>

CUT:
<what should be removed>

ADD:
<smallest missing concepts, if any>

ZERO_NEW_TYPES_ATTACK:
<one concrete counterexample, or NO COUNTEREXAMPLE FOUND>

RESIDUE_ATTACK:
<what, if anything, still appears genuinely THR-shaped after strongest-owner subtraction>

DO_NOT_BUILD_YET:
- ...

VERDICT:
SHRINK_AGAIN
or
KEEP_NARROW_RESIDUE
or
REPAIR_RFC

EVIDENCE_CEILING:
<what this review does and does not establish>
```

---

## 7. Review ceiling

A favourable review does not validate THR.

An unfavourable review does not automatically invalidate the current four records.

This packet is testing the proposed **next architecture layer**.

```text
REVIEW != AUTHORITY
AGREEMENT != VALIDATION
DISAGREEMENT != FAILURE
GOOD ARCHITECTURE SHOULD SURVIVE ANSWER-BACK
```
