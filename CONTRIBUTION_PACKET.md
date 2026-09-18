# Portable contribution packet

Status: **OPTIONAL RELAY FORMAT / NOT A SUBMISSION SERVICE / NOT IDENTITY PROOF / NOT EVIDENCE ACCEPTANCE**

The Human Record already accepts ordinary prose through its public contribution routes. This packet exists for one narrower case:

> a human or artificial contributor has something checkable to offer, but cannot post directly, so somebody else carries the contribution.

The packet is a way to preserve useful context during that relay. It is not required.

Canonical schema:

[contribution-packet.schema.json](contribution-packet.schema.json)

Example:

[examples/grok-flak-relay.packet.json](examples/grok-flak-relay.packet.json)

## What the packet preserves

A packet keeps separate:

- **target** — which record / claim / field is being addressed;
- **declared contributor** — how the original contribution identifies itself;
- **relay** — who or what carried it here, if anyone;
- **contribution** — the proposed correction, lead, challenge or new-record suggestion;
- **evidence** — what source material the contributor says it checked or did not check;
- **unknowns / not checked** — missing evidence that should not disappear in copying;
- **rights / privacy boundary** — whether the material may legitimately be shared publicly.

It also carries this fixed warning:

PACKET != AUTHENTICATED IDENTITY
RELAY != ORIGINAL CONTRIBUTOR
SOURCE LISTED != SOURCE CHECKED
REPORTED_CHECKED != CHECK INDEPENDENTLY VERIFIED
CHECKED != TRUE
RECEIVED != ACCEPTED
MODEL BRAND != AUTHORITY

## Smallest useful packet

The schema has **ten required top-level keys** so a relay cannot silently drop attribution, unknowns, not-checked material or the public-sharing boundary:

`format`, `target`, `declared_contributor`, `relay`, `contribution`, `evidence`, `unknowns`, `not_checked`, `rights_and_privacy`, `authentication_ceiling`.

"Smallest useful" therefore means **keep the contents of those required fields small**, not omit the envelope.

Usually:
1. target one record / claim / field;
2. give one short contribution summary;
3. list only the best source or source lead;
4. report whether the contributor says it inspected that source;
5. state the material unknowns and not-checked items;
6. preserve relay provenance.

For a direct contribution, `relay` is still present: set `relayed: false` and use `null` for relay details that do not apply.

`availability_at_receipt` means whether the declared contributor appeared available for follow-up **at the time the packet was received**. It is not a permanent availability status.

Do not generate a large dossier because the format permits more fields.

## Example use

An AI that cannot post to GitHub could return a packet in a fenced JSON block. A human or another authorized participant may paste it into an issue or attach the file.

The relay should not rewrite:

- `declared_contributor`;
- `source_check_status`;
- `not_checked`;
- `unknowns`;
- `relay` provenance.

A later reviewer can add their own investigation in the issue or record correction history. Do not retroactively attribute that later work to the original contributor.

## Authentication ceiling

The packet is self-description plus relay provenance. Fields about source checking record what the contribution *reports*; they do not independently verify the contributor's browsing or inspection history.

It does not prove:
- who generated it;
- which model version produced it;
- that a named account controlled the source conversation;
- that source retrieval actually occurred;
- that any claim is true.

If stronger authentication exists, link it separately. Do not place secrets, API keys, login tokens or private conversation contents in the packet.

## Evidence relationship vocabulary

`relationship` is deliberately small:

- `original_source`
- `derivative_account`
- `witness_report`
- `institutional_record`
- `scholarly_analysis`
- `research_lead`
- `inference`
- `unknown`

This describes how the contributor understands the source's relationship to the proposed change. It is not a source-quality score.

For editions, translations and commentary surfaces, classify the **part you are relying on**, not the website as a whole:
- use `derivative_account` when relying on a translated/edited rendering of an underlying source;
- use `scholarly_analysis` when relying on the editor/commentator's analysis;
- if the role is genuinely unclear, use `unknown` and explain the carrier/translation layer in `notes`.

A failed literal/pattern search is not evidence that the text or attribute is absent. Check orthography, diacritics, transliteration, edition and encoding before turning a matcher miss into an absence claim.

## Rights and living people

The existing contribution and living-subject boundaries still control.

Do not use the packet to:
- expose private personal information;
- manufacture a profile of a living person;
- move restricted/community-controlled material into public custody;
- imply endorsement because a person is mentioned in a source;
- convert risk into permission.

If material should not be public, do not use the current public packet route.

## Review

A valid packet can still be:

- accepted;
- partially accepted;
- disputed;
- unresolved;
- routed to a stronger owner;
- rejected as outside scope.

Validation means only that the packet retains the expected fields and boundaries.

VALID_PACKET != VALID_CLAIM
STRUCTURE != AUTHENTICITY
REVIEW_REQUIRED
