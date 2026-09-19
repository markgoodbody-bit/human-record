# The Human Record — fractal self-description microcase

Status: **EXPERIMENTAL MICROCASE / NOT REGISTRY SEMANTICS / NOT CANON**

Date: 19 September 2026

Machine fixture:

`examples/fractal-validator-run.experimental.json`

Target process:

GitHub Actions run:
`35463860339`

Workflow:
**Validate Human Record integrity**

This microcase tests one claim from `FRACTAL_ARCHITECTURE.md`:

> THR should eventually be able to describe material processes that produce or validate
> its own public state without pretending those process receipts establish truth.

No new shared `thr:process`, `thr:principal`, `thr:event`, `thr:attestation` or
`thr:anchor` registry type is introduced here.

The receipt uses a record-local experimental ID because cross-record identity has not yet
been earned.

---

## 1. Why this run was selected

The run is a real completed validator execution on draft PR #52.

It is useful because it contains:
- a trigger branch/head;
- a base;
- a synthetic PR merge checkout;
- a workflow definition;
- validator source versions;
- declared execution environment;
- multiple steps;
- warnings;
- rejection tests;
- a final job conclusion.

The process is under THR's operational control sufficiently to inspect, but the execution
service is external GitHub infrastructure.

That makes it a better first process specimen than inventing a fictional signing system.

---

## 2. The first important distinction

The run had three different repository identities.

### Trigger head

GitHub run metadata records:

`7cd55c24c145d8424256e72ae27b6cdff2669f12`

This is the branch commit that triggered run 124.

### Base

PR #52 was based on:

`1f5a5919938f385f43f1e2383bdfbb52807b206e`

### Executed checkout

The workflow checkout log shows that GitHub actually executed against synthetic merge
commit:

`3cced4453cf64b52a9a7364e0ba10b6a2ec28554`

with the log statement:

```text
Merge 7cd55c24c145d8424256e72ae27b6cdff2669f12 into
1f5a5919938f385f43f1e2383bdfbb52807b206e
```

The PR later advanced beyond the triggering head.

Therefore:

```text
CURRENT PR HEAD
!=
RUN TRIGGER HEAD
!=
EXECUTED CHECKOUT
```

A provenance system that stored only "PR #52 passed" would already have lost material
process identity.

---

## 3. Process-definition identity

The experimental receipt pins the Git blob identities of:

- `.github/workflows/validate-integrity.yml`;
- `tools/validate_all.py`;
- `tools/validate_integrity.py`;
- `tools/validate_operational.py`.

These identify the source bytes used by the synthetic merge checkout.

They do **not** prove:
- those programs are correct;
- GitHub executed them faithfully;
- the Python interpreter or runner image was uncompromised;
- the historical assertions are true.

```text
PROCESS SOURCE IDENTITY
!=
PROCESS EXECUTION INTEGRITY
!=
RESULT VALIDITY
```

The distinction is worth keeping even if later cryptographic/supply-chain attestations are
added.

---

## 4. Principal / authority pressure

The GitHub run metadata names:
- triggering actor account: `markgoodbody-bit`;
- execution platform: GitHub Actions;
- repository permission: contents read.

The microcase deliberately does **not** create a shared THR living-person principal from
the account.

The useful statement is only:

> This public account label triggered the workflow according to GitHub's run metadata.

Likewise, GitHub Actions executed the workflow but does not thereby receive:
- truth authority over THR records;
- policy authority over THR;
- authorship of the historical claims;
- independent evidentiary status for Camp Fire, flak, sieve/riddle or Hannibal.

This tests:

```text
EXECUTES PROCESS != GOVERNS RECORD
HOSTS RECEIPT != INDEPENDENT HISTORICAL WITNESS
ACCOUNT LABEL != PERSON DOSSIER
```

---

## 5. Result pressure

The run's structural/operational validation completed successfully.

The rejection suite ran:

`103 tests`

and returned:

`OK`

But the validator also emitted seven THR warnings:

- five open-vocabulary `referenced_by_record` observation outcomes;
- one `byte_identical_observed_copy` relation warning;
- one `byte_identical_observed_copy_of` relation warning.

Therefore a faithful process receipt cannot be one bit:

```text
PASS
```

It must preserve at least:

```text
PROCESS COMPLETED
VALIDATOR STAGES PASSED
REJECTION TESTS PASSED
WARNINGS = 7
WARNING TYPES = preserved
```

Candidate invariants:

```text
PROCESS SUCCESS != WARNING-FREE
PASS != NO RESIDUAL
WARNING_VISIBLE != DEFECT_RESOLVED
```

---

## 6. What the run actually establishes

It supports a bounded claim:

> The identified GitHub Actions job executed the identified validation commands against
> the identified synthetic checkout and reported the preserved results.

That is useful.

It does not establish:

```text
RECORD TRUE
SOURCE AUTHENTIC
IDENTITY MATCH TRUE
WARNING HARMLESS
GITHUB INDEPENDENT OF THR CLAIMS
PROCESS PERFECTLY REPRODUCIBLE
```

The current validators themselves already state:

```text
Warnings remain actionable; this is not a truth verdict.
```

The self-description layer should preserve that ceiling rather than replace it with a
higher-status "certification".

---

## 7. What this microcase teaches the RFC

### A. Process identity needs both definition and instance

```text
WORKFLOW / VALIDATOR SOURCE
!=
ONE EXECUTION OF THAT PROCESS
```

### B. Inputs can have several relevant identities

A process receipt may need:
- requested/trigger input;
- resolved/executed input;
- base or dependency input.

Do not call all of them `commit`.

### C. Output should preserve warnings, not just final status

A process result is structured evidence.

### D. External execution service is not automatically an independent witness

GitHub provides useful third-party operational evidence, but that does not make it an
independent witness to the historical proposition inside a THR record.

### E. Living-person anti-enumeration survives operational provenance

A public account can be referenced as an account without constructing a general person
identity.

### F. A local process ID is sufficient for this first case

No cross-record need currently requires a shared `thr:process` ID.

That is a successful use of the three-level addressability rule.

---

## 7.1 Independent microcase audit repair

A later bounded Codex audit re-read fresh GitHub run/job metadata and the logs for this
exact microcase.

It found no mismatch in the preserved run, job, trigger head, executed checkout, source
blob identities, 103-test result or seven THR-validator warnings.

It did find one forward currentness defect in the first receipt shape:

- GitHub metadata exposes `run_attempt = 1`;
- the first fixture preserved run number and run ID but not run attempt;
- a generic workflow-run URL can later represent a rerun attempt;
- the first fixture also did not preserve when that external metadata was re-observed.

The fixture now records the observed attempt and the audit observation timestamp as a
**later metadata re-observation**. It does not backfill an invented original receipt
creation time.

```text
RUN ID != RUN ATTEMPT
RUN NUMBER != RUN ATTEMPT
AUDIT OBSERVATION TIME != ORIGINAL RECEIPT CREATION TIME
LATER REOBSERVATION != ORIGINAL OBSERVATION
```

This is a narrow self-description repair. It does not earn a global process schema.

---

## 8. Hostile cases still unresolved

This microcase does not yet solve:

1. **tampered runner**
   - workflow source is correct but execution host is compromised;

2. **supply-chain substitution**
   - an external Action tag points to different code later;

3. **log mutation / deletion**
   - external service receipt disappears;

4. **key/signature semantics**
   - no cryptographic principal signing is tested;

5. **independent checkpoint**
   - no unrelated custodian has witnessed the exact run state;

6. **long-term reproducibility**
   - `ubuntu-latest` is not a permanent environment identity;

7. **restricted process evidence**
   - some future process inputs/logs may not be publishable;

8. **governance**
   - a valid process receipt says nothing about whether the process should have been run.

These remain pressure for later phases.

---

## 9. Microcase verdict

```text
SELF-DESCRIPTION USEFUL = YES
GLOBAL PROCESS REGISTRY = NOT YET EARNED
GLOBAL PRINCIPAL REGISTRY = NOT YET EARNED
ATTESTATION SCHEMA = NOT YET EARNED
CRYPTO / PKI = NOT YET EARNED
INDEPENDENT WITNESS TEST = NEXT LARGER PHASE, WHEN AN ACTUAL INDEPENDENT WITNESS EXISTS
```

The experimental receipt is useful because it exposes distinctions the current public
record model does not need to encode yet.

That is enough for this phase.

Do not turn the microcase into production architecture merely because it has a JSON file.
