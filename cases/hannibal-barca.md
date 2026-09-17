# The Human Record — Hannibal Barca: a historical person reached through surviving evidence

Status: **WORKING RECORD CANDIDATE / PUBLIC-SOURCE HISTORICAL-PERSON STRESS CASE / NOT BIOGRAPHICAL CANON / NOT VALIDATION**

Recorded: 17 September 2026.

## What this record is about

This record tests how The Human Record handles a particular human being rather than an artwork, a travelling claim, or a living practice.

The subject is the historical person conventionally called **Hannibal Barca**, the Carthaginian commander associated with the Second Punic War and the crossing of the Alps into Italy.

The record does not attempt to write the definitive biography of Hannibal. Its narrower question is:

> What is the smallest inspectable chain of evidence by which this particular human being remains reachable to a reader more than two millennia later?

```text
ENTITY != BIOGRAPHY
NAME != ENTITY
MENTION != ENTITY
ENTITY != CLAIMS ABOUT ENTITY
REPRESENTATION_OF_ENTITY != EVIDENCE_OF_ENTITY_APPEARANCE
SURVIVING_RECORD != COMPLETE_LIFE
```

## Why this case was selected

The three existing Human Record entries stress artefact provenance, claim/source ancestry, and living-knowledge transmission. Hannibal introduces a different problem: a deceased human subject whose life is not directly inspectable and whose surviving record is distributed across later textual traditions, material evidence, copies, translations, scholarship and representations.

It therefore pressures the current identity model directly. `IDENTITY_MODEL.md` already uses “Hannibal” as an example of why a name is not a safe identity key. This case asks whether the rest of the record architecture can actually carry that distinction in a real historical-person record.

## Current bounded finding

A strong public-source route establishes that ancient literary traditions identify a Carthaginian commander Hannibal, son of Hamilcar, and describe his campaign from Iberia into Italy across the Alps.

Polybius, *Histories* Book 3, is especially important to this first pass. In the surviving text he describes Hannibal's preparations for entering Italy, explicitly discusses the Alpine crossing, says that he questioned people involved in the events, and says that he personally inspected the country and traversed the Alpine pass in order to investigate the account. He also reports figures that he attributes to a column erected by Hannibal at Lacinium.

Livy, *History of Rome* Book 21, supplies a later Roman literary route into the same war and preserves, among other material, the famous childhood-oath tradition. Polybius also preserves an oath account, framed as something Hannibal later said while at the court of Antiochus.

This is enough to establish a useful historical-person record candidate. It is not enough to establish every familiar statement about Hannibal, his motives, exact route, appearance, birth year, inner experience, or the reliability of every surviving story.

## Entity anchor

Working subject:

```text
preferred display label: Hannibal Barca
entity kind: historical human / person
life: ancient; exact birth/death claims remain assertions requiring sources
principal context in this record: Carthaginian command / Second Punic War / Alpine campaign
identity status: resolved for this bounded record to the historical commander described by the checked Polybius/Livy passages
```

A future machine record should use an opaque `thr:entity:<uuid>` identifier. It must not encode `hannibal`, `barca`, a birth date, nationality or other correctable assertion into the key.

The labels “Hannibal”, “Hannibal Barca”, translated/transliterated forms, titles and source-literal descriptions remain labels or mentions. They are not the entity itself.

## First evidence walk

### Polybius — *Histories*, Book 3

Public route checked through the Perseus Digital Library English text.

Material observations in this first pass:

- Book 3.34 describes Hannibal preparing to carry the war into Italy and coordinating with Celts around and beyond the Alps.
- The Book 3 narrative explicitly states that Hannibal crossed the mountains from the Rhone valley into Italy.
- Polybius criticises sensationalised accounts of the Alpine passage and states that he questioned people involved in the events and inspected/traversed the Alpine country himself.
- Book 3.50 continues the ascent narrative.
- Book 3.56 says the actual passage of the Alps took fifteen days and reports surviving troop numbers which Polybius says Hannibal himself recorded on a column at Lacinium.

Evidence role:

```text
ANCIENT NARRATIVE SOURCE
+ AUTHOR CLAIMS INVESTIGATION / INTERVIEWS / SITE INSPECTION
!= CONTEMPORARY TRANSCRIPT OF EVERY EVENT
!= HANNIBAL'S OWN SURVIVING ACCOUNT
```

### Polybius — Hannibal's oath tradition

Book 3.11 preserves an account in which Hannibal, later at Antiochus's court, describes his father Hamilcar making him swear hostility to Rome as a child.

This is evidence that the oath story existed in the Polybian tradition and is presented there as Hannibal's own later account. It does not turn the surviving English web text into a direct recording of the childhood event.

```text
ANCIENT AUTHOR REPORTS HANNIBAL'S LATER STATEMENT
!= CHILDHOOD EVENT DIRECTLY OBSERVED BY CURRENT READER
```

### Livy — *History of Rome*, Book 21 and Book 35

Public route checked through Perseus English texts.

Book 21 opens the Second Punic War narrative and preserves the childhood-oath story. Book 35 later gives a speech attributed to Hannibal at Antiochus's court in which the oath is again invoked.

Livy is therefore a separate surviving textual route, but this first record does **not** yet establish source independence for each proposition merely because Polybius and Livy are two author names or two web pages.

```text
TWO ANCIENT TEXTUAL ROUTES != TWO INDEPENDENT WITNESSES TO EACH EVENT
```

## Claims kept separate from the entity

The following are examples of claims that must not be baked into Hannibal's identity key:

- Hannibal crossed the Alps with an army.
- Elephants accompanied the campaign.
- Hannibal was born in 247 BCE.
- Hannibal was nine when Hamilcar required an oath concerning Rome.
- Hannibal personally maintained lifelong hatred of Rome because of that oath.
- a particular Alpine pass was the exact route used.
- a particular ancient or later portrait accurately depicts Hannibal's appearance.
- Hannibal was a “great”, “brilliant”, “evil”, “heroic” or otherwise evaluatively ranked commander.

Each proposition needs its own evidence and status if it becomes material to this record.

## The missing Carthaginian aperture

This first pass is dominated by surviving Greek/Roman literary routes available through modern transmission and digitisation.

That fact must remain visible.

The record has **not** established what Carthaginian archival, literary, commemorative, oral or administrative material once existed, what was lost, what survives indirectly, or how the destruction and later history of Carthage shaped the surviving evidence base.

Therefore:

```text
NO CARTHAGINIAN SOURCE CHECKED HERE != CARTHAGINIANS LEFT NO RECORD
SURVIVING HOSTILE / OUTSIDE TRADITION != COMPLETE SUBJECT VIEW
ARCHIVAL LOSS != NEGATIVE EVIDENCE ABOUT THE LOST CONTENT
```

A later pass should identify the strongest scholarly owners for Punic/Carthaginian source survival before THR makes any stronger statement about that loss.

## Representations are their own records

A bust, coin, painting, film still, game model or generated image labelled “Hannibal” may be evidence about how later people represented Hannibal. It is not automatically evidence of Hannibal's physical appearance.

If THR later records a representation, preserve separately:

```text
REPRESENTED SUBJECT
CREATOR / DATE / CARRIER
CLAIMED BASIS FOR LIKENESS
PROVENANCE OF THAT BASIS
UNCERTAINTY
```

Do not let a familiar image silently become a portrait witness.

## Death and answer-back

Hannibal cannot answer this record, consent to it, correct it, withdraw participation or explain what surviving sources got wrong.

That does not create unlimited authority for THR.

The living-subject encounter mechanics in `LIVING_SUBJECTS.md` do not apply mechanically to a deceased ancient person. The underlying discipline still matters: do not convert inability to answer into permission to invent, flatten uncertainty or claim ownership of the subject's life.

```text
DEAD != UNPROTECTED
NO SUBJECT ANSWER-BACK != RECORD INFALLIBLE
INABILITY_TO_REFUSE != PERMISSION_TO_INVENT
```

Correction must therefore come through evidence, scholarship, source criticism and later challengers rather than subject reply.

## Unknowns / not checked in this first pass

This record has not yet checked:

- the original Greek/Latin text against the English translations used here;
- modern critical editions of Polybius or Livy;
- the strongest current Hannibal biographies or specialist Punic-War scholarship;
- archaeological evidence bearing on Hannibal as an individual;
- Punic inscriptions or other Carthaginian evidence bearing on the person;
- the full textual dependency relationship among Polybius, Livy and other ancient authors;
- Cornelius Nepos, Appian, Plutarch or other ancient Hannibal traditions;
- the exact Alpine pass question;
- the elephant evidence in detail;
- birth and death chronology in detail;
- ancient coin/bust/portrait attribution;
- what Hannibal himself wrote, dictated, commissioned or caused to be inscribed beyond the reported Lacinium column route;
- the survival/destruction pathway by which the present evidence corpus became asymmetric.

These are research routes, not missing fields that must all be filled before this bounded record can exist.

## What this case adds to THR architecture

The current record contract survives, but historical people expose several type-specific needs:

```text
ENTITY ANCHOR
+ SOURCE-LITERAL MENTIONS
+ CLAIMS ABOUT ENTITY
+ SOURCE / TRADITION ANCESTRY
+ REPRESENTATIONS OF ENTITY
+ LOST / UNAVAILABLE APERTURES
+ SUBJECT ANSWER-BACK STATUS
```

No new universal schema is earned yet.

The most important pressure is that THR must not turn an entity registry into a biography database. Identity should remain sparse; claims remain evidence-bearing objects around the entity.

## Current status ceiling

```text
HISTORICAL_PERSON_RECORD != DEFINITIVE_BIOGRAPHY
ANCIENT_TEXT_SURVIVES != EVENT DIRECTLY OBSERVED
TWO SOURCES != INDEPENDENT WITNESSES
TRADITION != FACT
REPRESENTATION != LIKENESS EVIDENCE
ENTITY_RESOLVED_FOR_THIS_RECORD != EVERY_MENTION_RESOLVED
UNKNOWN != ABSENT
DEAD != FREE_FOR_ALL
```

## Public source routes used for this first candidate

- Perseus Digital Library, Polybius, *Histories*, Book 3, including chapters 11, 34, 50 and 56.
- Perseus Digital Library, Livy, *History of Rome*, Book 21 and Book 35 chapter 19.

These public web routes are retrieval surfaces for the checked translations. They are not claimed to be the ancient source objects themselves, and live availability is not preservation.

## Correction rule

A challenge may target identity resolution, translation, source ancestry, chronology, source independence, interpretation, omitted stronger scholarship, or any other claim. Preserve the challenge and resulting correction without pretending the earlier record state never existed.

```text
CORRECTION_OF_RECORD != CHANGE_TO_HANNIBAL'S LIFE
```
