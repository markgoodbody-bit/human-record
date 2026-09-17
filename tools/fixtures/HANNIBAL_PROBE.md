# Hannibal candidate: existing-registry probe

Basis: human-record main `15b9929f685627644fcfc33cbb113b34876ecf59`.
Research fixture only. Repository visibility is not public catalogue promotion.

This is the first bounded return to Framework's task on PR28 comment
5720957538. It is not completion of the owner mapping or JFK fixture.

## Before / after

Before: Hannibal existed as competing Markdown candidates, without an executable
registry example. After: one candidate person, one source-literal mention, one
bounded web-text observation and one source-attributed relationship can be passed
through the existing validators in memory. Production registries, catalogue,
public views, validators and model documents are unchanged.

The source is [Nepos, Hannibal 13.3 on Dickinson College Commentaries](https://dcc.dickinson.edu/nepos-hannibal/chapter-13).
The assertion records Nepos's report of Sosylus as Hannibal's Greek teacher, not
independent confirmation of that historical relationship. Candidate resolution
is retained; no manuscript inspection, byte preservation or complete source
ancestry is claimed. This does not establish that all of PR28 fits the model.

## Earned result

The existing integrity checks accept the added entity, source/observation and
source-reported assertion alongside the unchanged production objects. No new
type or assertion-state vocabulary is needed for this bounded claim.

The existing operational validator rejects the mention with:

```text
unknown record_id 'hannibal-candidate-not-published'
```

This is an expected failure captured by the test, not a green validation of the
candidate. `validate_operational.validate()` takes allowed record IDs only from
`records/catalog.json`. A research mention cannot currently be validated without
a catalogue identity. There is no attempt to borrow another record ID or insert
a fake public entry to get a pass.

## Provisional repair direction

Separate research-context existence from public-view availability. The smallest
change should let a mention reference a checked, non-catalogued candidate context
while continuing to reject dangling references. It need not replace the source,
entity or assertion model or adopt a universal graph schema.

Whether that is an optional record link, an explicit candidate-context reference,
or another existing owner's pattern remains open until the owner mapping. Merely
allowing arbitrary strings or disabling the reference check is not the repair.

Human-view consequence: a curator could prepare and challenge an attributed claim
without manufacturing a public record page first. No website change is made here.

## Reproduction

```text
python -B -m unittest discover -s tools -p test_validate_hannibal_candidate.py -v
python -B tools/validate_all.py
python -B -m unittest discover -s tools -p 'test_validate*.py'
```

Three probe tests cover structure accepted, catalogue dependency exposed, and
candidate/source-report status retained. Existing eleven vocabulary warnings
remain unrelated and unresolved. Structural acceptance is not historical truth,
identity certainty, preservation adequacy or standards interoperability.

Later follow-up: RESEARCH_MENTION_REPAIR.md documents the optional record-link
repair. The original fabricated-link rejection remains tested; a separate test
omits that link and accepts the source-anchored candidate without publication.
