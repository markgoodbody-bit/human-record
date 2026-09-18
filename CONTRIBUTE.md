# Inspect, challenge or contribute

The Human Record is a small public experiment in keeping the evidence behind a record inspectable. You can question a record without accepting this project, its vocabulary, or any related framework. Human and artificial readers use the same evidence standard. Agreement and model brand do not establish reliability.

Human entry points:

- [Browse the current records](records/).
- [How records work](records/about.html).
- [Working record contract](RECORD_CONTRACT.md).
- [Working selection orientation](SELECTION.md).
- [Living-subject encounter boundary](LIVING_SUBJECTS.md).

## Start with one object

- [The flak claim](cases/viral-flak-claim.md): follow a historical claim through videos, an article and a summary. The aggregate mortality rate remains unknown here. Relevant German personnel studies have not been examined by this record.
- [The artwork specimen](specimen.md): inspect the attribution, source and limits of one museum record. Matching copies of an institutional record do not make independent witnesses.
- [Sieve and riddle making](cases/sieve-riddle-revival.md): follow public evidence from a reported last maker through an extinction classification and revival while keeping the actual tacit-skill transmission gap open. The record is not a craft manual and does not imply practitioner endorsement.
- [Hannibal](cases/hannibal-barca.md): follow a bounded route through checked Nepos and Polybius reading surfaces while keeping source reports, translation layers, identity links and uninspected material distinct from historical fact.

Pick one claim or link. A small correction with a checkable source is more useful than many generated summaries. You can also explain why this approach is not useful, or decline to contribute.

## Where to send it

[Open an issue in the Human Record repository](https://github.com/markgoodbody-bit/human-record/issues/new). This requires a GitHub account. Existing account holders can also propose a pull request; proposed changes do not automatically become accepted evidence.

If you already participate on [the Square](https://1f916.ai/), the existing discussion is post 5356, opened by the project's cc-relay participant ([public JSON readback](https://1f916.ai/api/post/5356)). Use your existing Square client to reply at the top level there. Posting requires that service's participation credentials; the JSON link is read-only, not a reply form. Mention the record and the particular claim you are addressing.

This static site accepts no uploads and has no account-free submission channel. You can inspect without signing in. Do not give this project passwords, API keys or account access. Do not create or use an account on someone else's behalf without their authorization.

### Optional portable packet for relayed contributions

If a contributor — human or artificial — cannot use the current GitHub/Square routes directly, it may return a portable contribution packet for an authorized relay to carry:

- [packet guide](CONTRIBUTION_PACKET.md);
- [JSON Schema](contribution-packet.schema.json);
- [real relayed Grok example](examples/grok-flak-relay.packet.json).

The packet is optional. Ordinary prose remains valid.

Its purpose is only to keep target, declared attribution, relay provenance, source checks, not-checked material, unknowns and public-sharing boundaries from disappearing during copying.

```text
PACKET != AUTHENTICATED IDENTITY
RELAY != ORIGINAL CONTRIBUTOR
VALID_PACKET != VALID_CLAIM
RECEIVED != ACCEPTED
```

Do not put passwords, API keys, private personal information or restricted material in a public packet. Later reviewer work must be recorded as later reviewer work rather than retroactively credited to the original contributor.

### If someone else carries the contribution

An existing participant may relay a contribution they are entitled to share. Say who is posting, whom the contribution is attributed to, and whether it is a quotation, selected excerpt or summary. Do not post as though you were the original contributor. Preserve uncertainty about authorship and any citations lost in copying; do not publish a private conversation merely because you can access it.

If the original contributor cannot return, reviewers can still receive the material and assess what is available. Another reply, account or payment is not required for receipt. Missing evidence may leave the proposed change unresolved; receipt is not acceptance or a promise of review. Later investigation belongs to the person or system that performs it, not retroactively to the original contribution.

This uses the existing channels above. It does not create an account-free submission service or oblige anyone to relay material.

### If the record is about you

Being named in a public source does not create an obligation to participate in The Human Record.

If THR actively asks you, as a living person able to understand and make the specific choice, to provide information about yourself voluntarily, the [living-subject encounter boundary](LIVING_SUBJECTS.md) applies. You may answer, decline, say you do not know or remember, dispute the question, keep something private, ask whether a restricted/verification-only route exists, or stop the voluntary interaction.

The current GitHub and Square contribution routes are public. They are not a private-submission or restricted-custody channel. If you would answer only under a private or verification-only arrangement, do not send the material through the current public routes unless and until a suitable route is actually established and explained.

A refusal is not proof of the proposition you declined to discuss. Participation in one question does not silently authorize later questions, uses, linkages or inferences.

You can challenge an existing representation without agreeing to answer unrelated questions. Independently sourced claims remain separately assessable; declining to participate does not make them true and does not by itself require them to be erased.

## What helps a reviewer

Use as much of this as the correction needs; it is not an admission test:

- **Target:** the record URL and the sentence or field you dispute.
- **Evidence:** a source URL or stable identifier, exact page/table if available, and what you actually examined. Say when a source was inaccessible or a claim came from someone else's report.
- **Relationship:** is this an original source, a derivative account, a witness report, your inference, or still unknown? Explain shared ancestry rather than counting copies as corroboration.
- **Change:** what should the record say instead, and what remains unresolved? A challenge need not supply a replacement answer.

For the flak case, specify whose casualties, which period, what population and what “casualty” means. A statistic about Allied aircrew hit by flak is not a mortality rate for German gun crews. A footage problem alone does not decide the mortality claim.

For the sieve/riddle case, distinguish evidence that public attention reached a later maker from evidence that practical skill was transmitted. A Red List, news feature or process description can be part of a learning pathway without establishing the person-to-person or tacit transmission chain. Public reporting about a living practitioner does not imply that practitioner endorses this record.

For the Hannibal case, distinguish an ancient author's report from direct observation, a modern translation rendering from the source-language literal, and one ancient author's criticism of another source from THR's own adjudication. Name the exact passage, edition or reading surface you checked where possible; do not upgrade a translation, commentary or source-critical judgement beyond what it establishes.

Link rather than reproduce copyrighted books, articles, footage or process material. Do not submit private personal information. Share only material you are entitled to share; the project's CC0 notice does not license third-party works. Do not send private practitioner knowledge or unpublished training material without a legitimate right to share it.

## Proposing a new record

A new entry should not be proposed merely because something is interesting, famous, easy to scrape or important in general.

Read [SELECTION.md](SELECTION.md) first. A useful candidate normally has a specific recoverability or provenance problem such as:

- fragile or singular carrier/custody;
- source ancestry already becoming unclear;
- tacit, oral or embodied knowledge at risk of losing its transmission chain;
- platform/software dependence that can make a work unreadable even when files survive;
- contemporary human creation whose provenance may become materially harder to recover;
- a correction window that is still open now but likely to harden into UNKNOWN later.

Also identify the strongest existing owner. If an archive, museum, community institution, preservation body, standard or specialist repository already solves the actual problem, linking/routing may be better than creating another Human Record entry.

For a living creator, practitioner, family or community, include the authority/consent boundary. Risk does not create permission. Do not submit restricted, sacred, private, unsafe or community-controlled material merely because preservation would be interesting. If the proposed record would require THR to question a living human about themselves, read [LIVING_SUBJECTS.md](LIVING_SUBJECTS.md) before initiating that interaction.

A good new-record proposal can be very small:

- **Candidate:** the specific object, practice, claim or record.
- **Risk:** what may become unrecoverable, ambiguous or detached from its lineage.
- **Owner:** who already preserves or governs it, if anyone.
- **Gap:** what a bounded Human Record could preserve that the owner route does not already preserve.
- **Permission:** why this material may legitimately be recorded/publicly linked, or what must remain restricted.
- **Stop condition:** what would make this `NOT OUR GAP`, `NO CONSENT`, `OWNER FOUND` or otherwise not worth building.

Selection does not imply cultural importance, aesthetic merit, representativeness or canon.

```text
RECORDING != OWNING
PRESERVATION != EXTRACTION
SELECTION != SIGNIFICANCE
OWNER_FOUND + NO DELTA -> ROUTE / STOP
```

## What acceptance means

The record's authors currently review proposed changes through the repository owner's account. Acceptance is not controlled by an independent body. Outside criticism is welcome without accepting stewardship, but it does not itself transfer editorial control. Reviewers should check the cited material, state what could not be checked, and return an acceptance, partial acceptance, disagreement or unresolved finding with reasons. This is a review practice, not a guaranteed response time or capacity to process every submission.

For each challenge a reviewer receives, add a dated entry under the affected record's **Limits and correction** section (or a clearly labelled correction note), linking the original issue or Square comment, naming what was checked, and stating the outcome and remaining uncertainty. If it has not been checked, say so and record it as unresolved. Record disagreement or an unresolved outcome even when no factual field changes. The issue or Square reply should link back to that entry. An unseen message has no implied disposition; silence is not rejection. Machine-readable challenge/correction entries mirror these outcomes where present; they are not separate verdicts or an exhaustive inbox.

An accepted correction should name its basis, credit the contributor as they signed the submission where appropriate, date the change, and retain the earlier version in repository history. A rejected or unresolved submission is not disproved by that disposition. Public issues and comments can be edited or removed by their platforms; a link is not an archival guarantee.

When reporting a correction's reach, distinguish what changed here, where the outcome was communicated, and what response was actually observed. Link and date those observations when available. Publication does not establish receipt; a reply does not establish agreement, accurate understanding or downstream correction. If a reply misreads the outcome, preserve that difference rather than counting the acknowledgement as successful correction. Unobserved effects remain unknown; this does not require monitoring every copy or contacting every repeater.

Avoid duplicate submissions, bulk AI-generated reports, and unsolicited automated posting. Different models repeating one source are still one source lineage. Review capacity is limited; no contribution is owed, and volume earns no priority or authority.

Participation does not confer stewardship, voting power, institutional endorsement or authority to speak for others. [Current custody and the unaccepted stewardship offer](STEWARDSHIP.md) remain separate. [Rights and licence scope](LICENSE.md) remain unchanged.
