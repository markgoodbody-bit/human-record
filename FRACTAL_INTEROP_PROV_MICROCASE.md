# The Human Record — W3C PROV interoperability microcase

Status: **EXPERIMENTAL INTEROPERABILITY TEST / NOT THR REGISTRY SEMANTICS / NOT CANON**

Date: 19 September 2026

Target stronger owner:
**W3C PROV**

Official specification:
`https://www.w3.org/TR/prov-o/`

THR source microcase:
- `FRACTAL_SELF_DESCRIPTION_MICROCASE.md`
- `examples/fractal-validator-run.experimental.json`

PROV mapping:
- `examples/fractal-validator-run.prov.ttl`

---

## 1. Question

Can the generic provenance part of the real THR validator self-description be expressed
using W3C PROV without inventing THR-native process/principal semantics?

The answer from this bounded case is:

```text
YES FOR THE GENERIC PROCESS GRAPH
NO FOR THE FULL THR EPISTEMIC MEANING
```

That is a useful result.

---

## 2. What PROV carries cleanly

The mapping uses:

```text
prov:Entity
prov:Activity
prov:SoftwareAgent
prov:used
prov:wasGeneratedBy
prov:wasDerivedFrom
prov:wasAssociatedWith
```

The real run maps naturally:

```text
trigger head -------+
                    |
base head ----------+--> executed synthetic checkout
                           |
workflow definition ------|
validator source ---------|
                           v
                    validation activity
                           |
                    associated with
                     GitHub Actions
                           |
                           v
                  GitHub run output
                           |
                      derived into
                           v
                later THR JSON receipt
```

No new THR-native universal process ontology is required for that graph.

---

## 3. Local fragments were enough

The PROV example deliberately uses document-local fragment identifiers:

```text
<#validation-run>
<#executed-checkout>
<#github-actions>
```

It does not mint:
- `thr:process:...`;
- `thr:principal:...`;
- `thr:event:...`.

That is an important success of the three-level addressability rule.

```text
INTEROPERABILITY OBJECT EXISTS
!=
SHARED THR ID EARNED
```

If a future record genuinely needs to refer to the same process or agent across records,
that can create later pressure for shared identity.

This microcase does not.

---

## 4. What PROV does not carry by itself

The repaired PROV graph represents that the validation activity used particular inputs
and software and generated bounded GitHub operational output.

The later THR JSON receipt is represented separately as a derived description of that
operational output. It is **not** represented as though the earlier validator run
generated the later hand-composed THR file.

It does not by itself preserve all the semantics THR cares about.

The experimental THR receipt still carries:

- seven warnings remained visible;
- warning categories/counts;
- 103 rejection tests returned `OK`;
- validator success is not a truth verdict;
- GitHub Actions is not an independent witness to the historical claims;
- the public GitHub account label must not become a living-person profile;
- successful process execution does not grant policy authority;
- current PR head differs from the historical run head.

Those are not failures of PROV.

They are THR-specific evidentiary and governance meanings around the provenance graph.

Therefore:

```text
PROV GRAPH
= GENERIC PROCESS ANCESTRY

THR RECEIPT
= BOUNDED EPISTEMIC / AUTHORITY / WARNING MEANING
```

The layers can coexist.

---

## 5. What THR should not do

This microcase removes the justification for a THR-native generic process graph such as:

```text
thr:process
thr:process-used
thr:process-generated
thr:process-agent
```

unless later pressure exposes a material requirement PROV cannot carry.

THR may still need its own:
- record-local receipt envelope;
- claim/evidence state;
- correction semantics;
- authority scope;
- privacy boundaries;
- warning / residual state.

But those should point into or map onto stronger provenance vocabulary where useful.

```text
THR RESIDUE
!=
REIMPLEMENT PROV
```

---

## 6. False-authority test

The mapping deliberately makes GitHub Actions a:

`prov:SoftwareAgent`

associated with the validation activity.

That relation means only that the software agent was associated with the activity.

It does **not** mean:

```text
GITHUB ACTIONS
-> TRUTH AUTHORITY
-> THR GOVERNOR
-> HISTORICAL WITNESS
```

This is important because a generic provenance relation can be semantically correct while
a consumer makes an invalid epistemic inference from it.

THR's surrounding record therefore still needs explicit ceilings.

---

## 7. False-independence test

The THR JSON receipt and PROV Turtle are later representations derived from the same
GitHub operational evidence.

It is not a new witness.

```text
GITHUB RUN OUTPUT
-> THR JSON RECEIPT
-> PROV MAPPING

MULTIPLE REPRESENTATIONS
!=
MULTIPLE INDEPENDENT OBSERVATIONS
```

Both derive from one operational event and one evidence source.

This is exactly the kind of multiplicity the fractal architecture must not count as
corroboration.

---

## 8. Time / later-description repair

A bounded Codex challenge found two semantic overclaims in the first PROV mapping.

First, the first Turtle graph called the later THR experimental JSON receipt an entity
generated by validator run 35463860339. Git history shows the JSON file was first
introduced in commit:

`0b74aea9c559ad29737057898f4accec23cac6ef`

at 2026-09-19T19:22:29Z, after GitHub's run metadata had already updated at
2026-09-19T19:17:07Z.

Therefore:

```text
GITHUB OPERATIONAL OUTPUT
!=
LATER THR DESCRIPTION OF THAT OUTPUT

PROCESS OUTPUT
!=
LATER PROVENANCE REPRESENTATION
```

The repaired mapping now has:

```text
VALIDATION ACTIVITY
-> GENERATES GITHUB RUN OUTPUT

LATER THR JSON RECEIPT
-> DERIVED FROM GITHUB RUN OUTPUT
-> FIRST INTRODUCED IN A LATER GIT COMMIT
```

Second, the first mapping treated GitHub run `updated_at` as
`prov:endedAtTime`. That upgrade was unsupported. The experimental receipt now states
explicitly that its `run_started_at` and `run_updated_at` values are GitHub metadata
fields, not asserted exact PROV activity start/end times.

The PROV Turtle therefore omits `prov:startedAtTime` and `prov:endedAtTime` for this
activity until a correctly scoped time source is deliberately mapped.

```text
RUN UPDATED_AT != ACTIVITY END TIME
JOB TIME != RUN TIME BY ASSUMPTION
TIMESTAMP != REPOSITORY STATE
```

This repair is useful precisely because syntactically valid provenance can still encode a
false relationship.

---

## 9. Interoperability result

```text
W3C PROV = SUFFICIENT OWNER FOR THE REPAIRED GENERIC PROCESS / DERIVATION GRAPH IN THIS MICROCASE

THR-NATIVE GLOBAL PROCESS TYPE = NOT EARNED

THR-NATIVE GLOBAL SOFTWARE-AGENT TYPE = NOT EARNED

THR-SPECIFIC RECEIPT / EPISTEMIC CEILINGS = STILL USEFUL
```

The current Turtle parses as 48 RDF triples.

That syntactic result does **not** establish that the mapping is semantically correct.
The Codex challenge is now preserved as evidence of that distinction.

```text
RDF PARSES != PROVENANCE CLAIM TRUE
```

This is the intended outcome of strongest-owner subtraction.

---

## 10. Next interoperability pressure

Do not immediately map every THR object into RDF.

A next interoperability case is earned only if it tests a distinct boundary, for example:

- C2PA manifest -> THR source/assertion without treating signature as truth;
- Memento archived version -> THR source observation without treating capture as complete context;
- SWHID -> THR software source without treating content identity as authorship/licence;
- in-toto/SLSA process attestation -> THR validator receipt without erasing warnings.

Choose a next case only when a current record or real external artifact supplies it.

```text
ONE INTEROP CASE PASSED
!=
RDF MIGRATION REQUIRED
```
