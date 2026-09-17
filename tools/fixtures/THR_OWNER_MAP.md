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
context in explicitly enabled in-memory research mode. Default/public validation
still requires a catalogue link following CC's publication-boundary review.
Locator accuracy remains a review obligation, not a validator result.

## Review of the owner-subtraction review

17 September follow-up to CC's PR28 comment 5721039060. These are narrower
interpretations and unresolved design questions, not additional project primitives.

### Wikibase belongs in the comparison; avoid a false contrast

[Wikidata ranking guidance](https://www.wikidata.org/wiki/Help:Ranking) assigns
normal rank by default and permits multiple values at the same rank, including
preferred. It also supports a reason for deprecation and warns that private
personal information is not made acceptable by marking it deprecated. This
weakens both the claimed mandatory single-winner contrast and the claimed
absence of existing correction-reason machinery.

[Wikibase RDF documentation](https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format#Truthy_statements)
distinguishes best-rank direct/truthy properties from full statement nodes with
qualifiers and references. A consumer choosing the former can hide alternatives;
it is not a limitation of every query or the stored representation. THR should
make selection visible, not claim a unique ability to retain disagreement.
No deployment or migration to Wikibase is proposed here.

### Reading and rejecting is not automatically quotation

[PROV-O](https://www.w3.org/TR/prov-o/#wasQuotedFrom) uses quotation for repeated
content. Merely reading and rejecting a source does not establish quotation or
primary-source status. Separate the evidenced relationship from its evaluative
stance; map each only when its semantics fit. Generic provenance links alone
do not encode rejection. An edge labelled independent also needs evidence and
scope; its presence is not proof of independence.

### Minimal graph is a practice, not a universal existence axiom

CC proposes no entity without an assertion and no assertion without an observed
source. The aim of preventing decorative graph growth is useful. The absolute
rule is not yet earned: research questions, failed checks and explicit unknowns
must remain representable without manufacturing positive support. Existing THR
assertion states include unknown and unsupported-in-sources-checked. Prefer
documented investigative/evidential need over pretending every retained object
is a positively supported historical proposition. No new validator rule follows.

### Correction trace is not compulsory retention of all content

CC's never-deletion rule conflicts if read as retaining withdrawn sensitive
material indefinitely. LIVING_SUBJECTS.md section 5 already requires stopping
controlled withdrawn uses and permits a minimal non-sensitive correction trace.
Preserve the reason and accountable change where appropriate, not automatically
the withdrawn payload. No deletion, retention-policy change or new collection
is made by this note. Nor has anyone established that this practice is unique.

### JFK coverage remains deliberately incomplete

The current fixture already avoids official-versus-conspiracy classes: it holds
two official report attributions without assigning a winner. It does not model
the later acoustic reassessment, reconstruct full causal premises, or test an
actual restricted-evidence access attempt. Holding two conclusion strings is not
proof of complete causal-model representation. These gaps remain open, not
completed by the passing reference tests.

### Integration recommendation

Keep the concrete reference repairs. Shrink broad novelty and owner-deficiency
claims. Do not adopt an absolute graph-existence or never-deletion rule from relay
agreement. A usable, carefully curated application can be worthwhile without a
new ontology or a demonstrated unique data layer.
