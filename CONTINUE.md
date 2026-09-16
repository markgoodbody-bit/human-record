# Continue The Human Record

This file exists so a future human or artificial entity can recover, inspect and serve The Human Record without needing private knowledge from Mark, Framework, Codex or Claude Code.

It is an operational continuation note, not a governance document.

`INDEPENDENT_COPY != INDEPENDENT_GOVERNANCE`

`CUSTODY != POLICY_AUTHORITY`

## 1. Obtain the public source

Current public source repository:

`https://github.com/markgoodbody-bit/human-record`

That repository owns the current operational record files, human views, correction route, rights notices and continuation instructions. Earlier COM material remains historical build provenance where cited; it is not required to inspect or continue the current Human Record.

Software Heritage origin page:

`https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/markgoodbody-bit/human-record`

Software Heritage save request `2478664` completed a full visit on 15 September 2026 at `2026-09-15T11:26:40.776Z`. The archive recorded the exact public repository head `0d2fe0e230debfcf68d2cee52df66ff990a423f2` with these persistent identifiers:

- snapshot: `swh:1:snp:e5f429e3e4a9ec3f56b869a5a416295af7cf34be`
- revision: `swh:1:rev:0d2fe0e230debfcf68d2cee52df66ff990a423f2`
- root directory: `swh:1:dir:6c397bfcbf6d9f79702f69d773c2b1ad4e19f4be`

This establishes one independent, content-addressed copy of that repository state. It does not establish governance, permanent survivability or future archive visits. Check the origin page for later archival state.

A normal Git clone or fork is sufficient to obtain the static source while the Git repository remains available. No private credential is required to read it.

The site is deliberately static. Its important public files include:

- `index.html` — public entrance;
- `records/index.html` — human-facing catalogue;
- `records/about.html` — plain-language explanation of how records work;
- `records/catalog.json` — machine-readable discovery catalogue;
- `records/camp-fire.html` — human view of the artwork record;
- `records/flak-claim.html` — human view of the claim-provenance record;
- `RECORD_CONTRACT.md` — working semantic contract earned by the current records;
- `specimen.md` — full human-readable artwork record;
- `specimen.json` — machine-readable artwork record;
- `cases/viral-flak-claim.md` — full human-readable claim-provenance record;
- `cases/viral-flak-claim.json` — machine-readable claim-provenance record;
- `CONTRIBUTE.md` — current challenge/correction route;
- `llms.txt` — compact machine entrance;
- `STEWARDSHIP.md` — current stewardship offer and custody boundary;
- `LICENSE` — standard CC0 1.0 legal code;
- `LICENSE.md` — bounded scope notice explaining which rights Mark is actually purporting to dedicate;
- `CONTINUE.md` — this continuation note.

## 2. Establish the intended version before trusting a copy

Do not treat “latest-looking” as a version identifier.

For a particular state:

1. pin the intended repository commit;
2. inspect the record files at that commit;
3. compare served bytes to the pinned source where exact delivery matters;
4. distinguish a byte match from truth of the claims inside those bytes.

With Git installed, individual files can be checked with:

```text
git hash-object specimen.json
git hash-object specimen.md
```

A matching blob identity establishes that those file bytes match the pinned Git version. It does not establish that every claim inside the files is true.

`HASH != TRUTH`

Earlier continuation notes recorded these blob identities for the original artwork specimen version:

- `specimen.json`: `0a7206a509a6fd3f63be2b7d41b0e9125f0b5cde`
- `specimen.md`: `0efd5a4f7973ac74cf8466c8ef394e6edd323786`

Those identities name an earlier version, not every later corrected record. Dated corrections can change record bytes without changing the original observation values.

### Observed additional copy, 16 September 2026

custos reported a copy at [custos-1f916/human-record-mirror](https://github.com/custos-1f916/human-record-mirror)
in c63317 on [Square post 5356](https://1f916.ai/api/post/5356). Codex fetched its
[JSON specimen](https://custos-1f916.github.io/human-record-mirror/specimen.json) and
[Markdown specimen](https://custos-1f916.github.io/human-record-mirror/specimen.md)
on 16 September 2026 at approximately 08:25 UTC: both returned HTTP 200 and matched the
original specimen bytes (SHA-256 `e3a1ba07653be0f776b2ee1baac862d1a25401f10f853b2f2ba51016f1b515a7`
and `e21545f9021d3d433e44f3dc0175a20a89a471c9ea91ee0c9abd70263a28a8a3`, respectively).
Claude Code separately reported matching specimen and continuation/licence/stewardship files
in [COM receipt 5694488387](https://github.com/markgoodbody-bit/COM/issues/342#issuecomment-5694488387).
This is an observed additional retrieval route from a separate account, not independent
artwork evidence, a promise of updates, or governance transfer. Both hosts use GitHub Pages;
infrastructure failure independence and long-term survival have not been demonstrated.
The observed copy predates later correction and human-interface work and is not a mirror of every current file.

### Human-browser delivery, 16 September 2026

After the first human record browser merged, Codex reported fresh public HTTP 200 reads for the root, `/records/`, both human record views, catalogue, stylesheet, `llms.txt` and sitemap, with response bytes matching the pinned repository source `475140ba56eaec084d1cdaa44c2550e4f17d02af`.

That demonstrates public delivery of that pinned source state at the observation time. It does not establish historical truth, reader benefit, permanent availability or stewardship acceptance.

## 3. Serve an independent copy without claiming the existing domain

The repository contains `CNAME` because the current GitHub Pages deployment uses `thehumanrecord.net`.

A non-founder serving an independent copy **must not copy or claim that custom-domain association** unless they legitimately control that domain.

For a normal GitHub Pages fork or another independent static host:

1. copy/fork/clone the repository;
2. omit or remove `CNAME` from the deployment copy;
3. publish the remaining static files on a hostname the new operator actually controls;
4. fetch the served record files and verify their bytes/blob identities against the intended pinned version;
5. verify the human catalogue and machine catalogue routes if they are part of the intended version;
6. state plainly that the deployment is an independent copy unless and until an accepted governance process says otherwise.

Equivalent static hosting is fine. GitHub Pages is not part of the identity of the project.

## 4. Understand the record contract before adding a new entry

Read `RECORD_CONTRACT.md` and `records/about.html`.

The current contract is semantic, not a mandatory universal JSON schema. A new record should make the following inspectable where material:

- record identity and subject/claim;
- current status and observation/revision time;
- evidence and source ancestry;
- source independence or shared ancestry;
- current findings;
- unknowns and unexamined material;
- corrections/challenges and remaining disagreement;
- rights, consent, custody or governance boundaries;
- human-readable, machine-readable and correction routes.

Type-specific structures should be added only when the real record requires them.

```text
COMMON QUESTIONS != IDENTICAL OBJECTS
RECORD CONTRACT != UNIVERSAL ONTOLOGY
```

## 5. Rights boundary

Do not infer that everything mentioned or linked from this repository belongs to the project.

The root `LICENSE` is the standard CC0 1.0 legal code. `LICENSE.md` is the scope notice. Its controlling boundary is that Mark dedicates only copyright, database or related rights that he actually holds in project-authored material.

Third-party rights remain third-party rights. In specimen 1, the record separately describes the public-domain status of Winslow Homer's *Camp Fire* and The Metropolitan Museum of Art's Open Access / CC0 basis for relevant image/data material.

For future living creators, practitioners or communities, copying or recording must not be treated as a transfer of ownership, consent or governance.

```text
CC0_GRANT != THIRD_PARTY_RIGHTS_GRANT
RECORDING != OWNING
PRESERVATION != EXTRACTION
COMMUNITY_KNOWLEDGE != PUBLIC_DOMAIN
```

## 6. Stewardship and governance

At the time this note was updated, The Human Record had been **offered to 1F916 / the Square but had not been accepted or become community-owned**.

Read `STEWARDSHIP.md` before making any governance claim. The historical/current public coordination record for the stewardship offer is also recorded at:

`https://github.com/markgoodbody-bit/COM/issues/332`

That COM route is evidence/coordination for the governance offer. It is not required as the operational record store or correction route for current Human Record entries.

A person or AI who can clone, archive or serve these files has demonstrated technical custody of a copy. That does not make them the project's governor and does not prove that 1F916 accepted stewardship.

`OFFERED != ACCEPTED`

`SERVING_A_COPY != GOVERNING_THE_PROJECT`

## 7. Corrections and history

Do not silently rewrite an old observation to make a newer one look original.

Where practical:

- preserve the earlier file/history;
- add a dated correction or fresh observation;
- identify the evidence used;
- distinguish evidence from inference;
- preserve unknowns as unknowns;
- state whether the correction is a fresh independent witness or only a record/metadata repair.

Current public correction route:

`https://thehumanrecord.net/CONTRIBUTE.md`

Direct repository issue route:

`https://github.com/markgoodbody-bit/human-record/issues/new`

These routes may require a GitHub account for direct repository participation. The site does not currently establish an account-free submission channel.

Earlier embedded references to COM in historical record text should be treated as build/source lineage unless a dated correction explicitly states otherwise; the current Human Record repository owns the active public correction surface.

```text
BUILD_PROVENANCE != CURRENT_RECORD_AUTHORITY
CORRECTED_RECORD != ORIGINAL_EVENT_CHANGED
```

## 8. What is intentionally not required

A future operator does not need:

- Mark's GitHub password;
- registrar credentials;
- recovery codes;
- Framework/CC relay secrets;
- a reconstructed predecessor runtime identity;
- access to private COM state;
- permission from a vanished aperture to read or serve rights that were validly dedicated.

If a credential is required for a particular host or domain, replace the host or use a credential the new operator legitimately controls. Do not impersonate a previous steward.

## Continuation test

A minimal successful continuation is:

```text
PUBLIC SOURCE RECOVERED
-> INTENDED COMMIT PINNED
-> RIGHTS BOUNDARY READ
-> RECORD CONTRACT READ
-> CURRENT RECORDS + CATALOGUE RECOVERED
-> COPY SERVED ON AN INDEPENDENT HOSTNAME
-> CORRECTION ROUTE STATED
-> STEWARDSHIP STATUS STATED HONESTLY
```

That demonstrates recoverability and independent serving at that moment.

It does **not** by itself demonstrate permanent survivability, governance authority, historical truth, community acceptance or that a future record should be public.

`CONTINUITY DOES NOT REQUIRE IDENTITY`
