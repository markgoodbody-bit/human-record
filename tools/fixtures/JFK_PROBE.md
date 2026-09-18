# JFK: bounded contested-event probe

Research fixture only, 17 September 2026. No public record, historical verdict,
complete causal model, standards conformance or evidence-custody verification.

## Before / after

Before: the owner map proposed a contested-event check. After: an executable
fixture holds one event referent, two different source-attributed conclusions,
a shared film referent, and a source-reported custody transfer. Four bounded
report-page observations are kept separate from the uninspected underlying film
and recordings. Production registries and catalogue remain unchanged.

## Source basis

- [Warren Commission chapter 1](https://www.archives.gov/research/jfk/warren-commission-report/chapter-1), Conclusions: attributed sole-actor finding.
- [Warren Commission chapter 3](https://www.archives.gov/research/jfk/warren-commission-report/chapter-3.html), Films and Tests, page 97: film used in its reconstruction.
- [HSCA summary](https://www.archives.gov/research/jfk/select-committee-report/summary.html), I.2-I.3: attributed probable-conspiracy finding, including its limits.
- [HSCA I.B](https://www.archives.gov/research/jfk/select-committee-report/part-1b.html), pages 67 and 79: reported dispatch-material custody and film correlation.

These selections test representation, not current historical consensus. Later
acoustic reassessments are outside this probe. The two findings are not assigned
equal credibility, nor does THR endorse either by storing an attribution.

## Earned results

1. Existing envelopes accept these bounded attributions without a new registry
   or closed vocabulary. Acceptance does not mean the validator checks their
   meaning, full inference dependencies or report authorship.
2. Two report uses can point to one candidate film referent without fabricating
   a film observation. This does not establish identical carriers or bytes,
   independent analyses, or a complete shared-evidence graph.
3. A reported custody transfer fits an assertion. Current custody and access
   remain unestablished, not absent. No invented failed retrieval or preservation
   event is added.
4. The unpublished mention fails with unknown record_id, as in Hannibal. A person
   literal is deliberately not resolved to the event entity to force a fit.
5. A synthetic mutation pairs a Warren-only source citation with an HSCA
   observation. The baseline validator accepts both because it checks existence
   separately, not ownership. The initial regression preserves this unsafe
   acceptance as a witness; it must not be reported as a successful safety check.

## Smallest justified next changes

Fix the assertion source/observation ownership defect first. An observation named
as evidence must belong to a source explicitly named in that evidence block.
Multiple cited sources remain valid; no one-to-one mapping is required. This
narrows structural acceptance, not historical interpretation.

The optional record-link proposal in THR_OWNER_MAP.md survives both examples as
a candidate workflow repair. It still needs an explicit source-owned observation
and locator contract, and adversarial tests. It was not implemented in this probe's
initial commit; the later implementation is recorded in RESEARCH_MENTION_REPAIR.md.
No new causal ontology or database layer is justified by these examples.

## Reproduce

Run `python -B -m unittest discover -s tools -p test_validate_jfk_candidate.py -v`.
The initial three tests distinguish representable content, catalogue rejection,
and unsafe provenance acceptance. No source data is fetched during testing.

## Repair follow-up

The baseline witness is preserved in commit `7834bb7`. The follow-up changes the
unsafe-acceptance test to require rejection and adds missing-owner, multi-source
and source-only cases. Before the validator repair, the first two negative cases
fail. The repair derives observation ownership from the source registry and
requires that owner among the assertion's cited sources. The assertion model
now states this constraint explicitly. The catalogue failure remains expected;
no historical assertion or production registry is changed.

CC review 5721371947 additionally demonstrated that changing a reported custody
assertion to state observed still passed at PR30 head 341d598 / 7618bc0. This was
a real semantic acceptance gap, not fixed by observation ownership.

The 18 September follow-up takes the smallest fail-closed route instead of adding
a speculative target ontology. Current source observations are retrieval /
inspection events and do not type the observed entity/situation/proposition.
Accordingly, cross-record assertion states `observed` and `reconciled` are
rejected until an earned typed observation/reconciliation relation exists.

This is deliberately **not** a ban based on source medium. A web page can
legitimately be directly observed *as a page*. The missing information is what
the observation was of. CRMsci 3.2 is the stronger owner for that semantic
relation. The one-word custody mutation and a parallel `reconciled` mutation
are now red-before / green-after regression cases.

```text
SOURCE_MEDIUM != OBSERVED_OBJECT
FAIL_CLOSED_NOW != PERMANENT_SCHEMA_DECISION
```
