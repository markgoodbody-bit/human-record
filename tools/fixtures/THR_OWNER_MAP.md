# THR registry owner map: bounded design review

Status: **PROVISIONAL MAPPING / NOT AN EXPORT / NOT CONFORMANCE**.
17 September 2026. Local basis: main `15b9929f` and Hannibal probe `3c95f4d`.
This follows the concrete catalogue-dependency witness, not a redesign mandate.

## Conclusion

The semantic ingredients are already owned. No THR-specific ontology gap is
established. The demonstrated local gap is preparing a source-literal mention
without requiring a public catalogue entry. A standards vocabulary does not by
itself repair that application constraint.

`ALREADY_OWNED` below means there is an existing relevant model, not that THR's
current JSON conforms. `CLEAN_INTEROP` remains a target until an explicit export
and adversarial round-trip test preserve scope, attribution and uncertainty.

## Closest owner by current concept

| THR concept | Owner / candidate mapping | Boundary |
| --- | --- | --- |
| `entities`: historical person | CIDOC CRM E21 Person | The person is not their registry row. Candidate identity resolution must remain attributed. |
| Labels and IDs | CRM E41 Appellation / E42 Identifier | A label is not identity proof; no blanket equivalence assertion. |
| `mentions`: literal occurrence and resolution | CRM E33 Linguistic Object for text; E13 Attribute Assignment for the interpretation activity | Neither alone encodes the whole THR mention envelope. Preserve source location and candidate alternatives. |
| Logical source document | CRM E31 Document / E73 Information Object | Distinguish intellectual content, edition, web rendering and physical carrier. |
| Custody | CRM E10 Transfer of Custody | A claimed transfer needs evidence; a URL or copy does not establish custody history. |

These are candidate correspondences to [CRM 7.1.3](https://cidoc-crm.org/html/cidoc_crm_v7.1.3.html),
not a lossless mapping or a claim to cover all entity types.

| THR concept | Owner / candidate mapping | Boundary |
| --- | --- | --- |
| `sources.observations`: inspection activity | CRMsci S27 Observation; S4 Single Observation when its narrower scope fits | A web read does not observe the ancient event. Preserve what was actually inspected and when. |
| Measured property | CRMsci S21 Measurement, where an actual measurement exists | Do not cast every retrieval or interpretation as measurement. |

Use the declarations in [CRMsci 3.2](https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v3.2.html).
In this version S4 is **Single Observation**, not the generic Observation class.
Version-specific class meanings matter; do not splice older names into a new map.

| THR concept | Owner / candidate mapping | Boundary |
| --- | --- | --- |
| `assertions`: proposition versus attitude to it | CRMinf I4 Proposition Set / I2 Belief | `reported_by_source` is not the project's belief in the event, nor automatically an actor's numerical confidence. |
| Reasoned conclusion | CRMinf I5 Inference Making, with premises and inference logic | Do not manufacture an inference event just because a JSON object has evidence links. |
| Competing interpretations | Separate propositions, attributed beliefs and inference paths | Shared evidence does not force shared conclusions or prove independence. |

[CRMinf 1.2.1](https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.2.1.html)
already addresses these distinctions. A concrete JFK fixture must establish the
required local relationships before any new causal-model field is proposed.

| THR concept | Owner / candidate mapping | Boundary |
| --- | --- | --- |
| Digital source state / generated view | CRMdig D1 Digital Object | A logical source across changing versions is not automatically one immutable byte object. |
| Capture, transformation or execution | CRMdig D7 Digital Machine Event / D10 Software Execution / D12 Data Transfer Event as appropriate | Match actual event scope. A digest alone does not establish the producing event or chain of custody. |

[CRMdig 5.0](https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html)
provides the digital-provenance owner. No automatic conversion of the existing
free-text observer or outcome fields is justified yet.

| THR concept | Owner / candidate mapping | Boundary |
| --- | --- | --- |
| `source-checks`: check and receipt | PROV Activity and generated Entity; associated Agent where supported | A failed check still produces a receipt. It does not establish that the source ceased to exist. |
| Source ancestry and correction | PROV derivation, quotation and revision relations where evidenced | Citation, derivation and byte equality are not interchangeable. Revision is not erasure. |
| Research provenance context | PROV Bundle when it is a named set of provenance descriptions | Not every arbitrary case collection is a Bundle. Publication is a separate activity/state. |

[PROV-O, W3C Recommendation](https://www.w3.org/TR/prov-o/)
supplies provenance-of-provenance and version relationships. It does not determine
truth, access permission or preservation adequacy.

The [nanopublication working guidelines](https://nanopub.net/guidelines/working_draft/)
separate assertion, assertion provenance and publication information in RDF
graphs. This is a useful export pattern, not a requirement to publish each draft
assertion or send it to an external network. THR JSON is not already a
nanopublication simply because it contains an evidence block.

## Hannibal consequence

Keep these distinct:

1. Hannibal as candidate historical referent.
2. The modern DCC page, its ancient-text passage, and its modern commentary.
3. Our bounded reading of that page.
4. The proposition attributed to Nepos, with candidate subject resolution.
5. A later curated public view, if reviewed and selected.

This decomposition is already conceptually supported. The current validator
instead requires a catalogue identity at step 4's mention stage. That is a local
workflow/reference constraint, not a missing world category.

## Initial repair proposal (implementation follow-up below)

Make `record_id` optional only when a mention remains independently anchored by
an existing source, its owned observation and a non-empty structural locator.
If supplied, `record_id` must still resolve to the catalogue. Do not introduce an
unvalidated replacement string named `context_id` or force a dummy public page.

Before choosing this option, check it against the bounded JFK case and existing
record-local mentions. If a durable research dossier ID is genuinely needed,
derive that requirement from a failing example rather than adding a new registry
now. No ontology importer, graph database or RDF dependency follows from this note.

## What remains unearned

- No export, namespace crosswalk, round-trip or standards-conformance test exists.
- No claim that humane navigation or visible uncertainty is unique to THR.
- No evidence yet that a graph UI improves reading or contribution.
- The later JFK fixture tests bounded report attributions, not causal/custody adjudication.
- No production registry/public-view change. The follow-up assertion ownership
  check and documented constraint are described in JFK_PROBE.md.

Follow-up: JFK_PROBE.md records the contested-event fixture and narrow provenance
repair. RESEARCH_MENTION_REPAIR.md records the later optional-link implementation.
Both original fixtures still reject their fabricated record IDs; additional tests
omit that field and accept a source-owned observation with non-empty locator
context. Locator accuracy remains a review obligation, not a validator result.
