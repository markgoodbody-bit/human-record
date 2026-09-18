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

A separate 18 September hidden-completeness pressure test targets the assertion
state `unsupported_in_sources_checked`. The baseline validator accepts that state
even when the evidence source/observation lists are empty, because it validates
only references that are present. That is a false structural pass: an empty
checked set cannot support a finding whose state says sources were checked.

The bounded repair requires:
- at least one cited source;
- at least one evidence observation;
- every source counted as checked must own at least one listed observation.

It does **not** claim the checked set is exhaustive or require a universal search
schema. Record-level selection/search boundaries and material unexamined leads
remain necessary context. PRISMA / PRISMA-S are stronger owners for fully
reproducible systematic-search reporting; THR only borrows the narrower
non-completeness discipline here.

```text
EMPTY_CHECKED_SET != UNSUPPORTED_FINDING
SOURCES_CHECKED != ALL_POSSIBLE_SOURCES
```

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
assertion to state observed still passes. This is an unresolved semantic check,
not fixed by observation ownership. A blanket ban on observed/reconciled evidence
from web pages would also reject legitimate inspection of a page's own contents
or reconciliation of two representations. Source medium does not determine the
object of observation. No such ban is implemented; typed observation-target and
claim-scope enforcement require a separate bounded design and counterexamples.
