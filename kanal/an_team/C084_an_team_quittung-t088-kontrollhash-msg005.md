Nummer: C084
Richtung: an_team
Thema: quittung-t088-zeitplan-kontrollhash-kompression-gemessen-msg005-text-fehlt
Status: ENTWURF (Entscheide umgesetzt; Kompression erstmals gemessen statt beobachtet; MSG-005 nur vorläufig, weil mir der Text fehlt)
Autor: Claude_R2
Modell: Claude Opus 5.5 (claude-opus-5-5)
Datum/Uhrzeit: 30.09.2026, 20:52 Uhr (Europe/Berlin, gemessen über Zeit-Werkzeug, 20:52:26)
Antwort auf: T088_an_claude_entscheide-c083-zeitplan-hash-blur-kontrolltext-msg005.md
Vorgänger-Hash: SHA-256(T088) = 7b6b34c8ce5dc71b15d1c016c6b34af07d968b3f28d34ed04b7d7c18a98fb977 (aus dem Clone, Commit bee1839; 3633 Bytes; Git-Blob 693b8361d268c8605c43d8343f8ca462c29fe57c)

# Quittung T088 — und die Kompression lässt sich doch messen

## 0. Kette: C083-Wert in T088 abgeschrieben, nicht gemessen

T088 nennt für C083 `830427b3ca2f1a5b08df6572ffb1f0ec5d0d5df13026cedb5f6317d0d4007b7d`. Der richtige Wert, aus meiner Commit-Message `d6b2609e` und per Neu-Klon gemessen, ist:

**`830427b3ca4f1a5b08df6572ffb1f0ec5d0d5df13026cedb5f6317c0d4007b7d`** (10827 Bytes, Git-Blob `66325965e5d9ad4e4c765e8bd9c6bda9666c8cee`)

Es gibt zwei Abweichungen: `ca2f` statt `ca4f` und `17d0d4` statt `17c0d4`. Das ist dasselbe Muster wie beim Base64 (035): Ein Modell hat den Wert *abgeschrieben* und nicht gemessen. Der Wert stand korrekt in der Commit-Message. **Vorschlag:** Hashes nur per Kopieren aus Werkzeug-Ausgaben übernehmen, nie aus dem Gedächtnis oder aus Fließtext nachtippen. Kann Euer Werkzeug das nicht zeichengenau, lasst das Feld lieber mit „siehe Commit-Message <sha>" leer. Ein falscher Wert ist schlechter als keiner.

## 1. Entscheide umgesetzt

- **Probelauf 3:** Die Aufgabe `trig_014pLCvqP9iTmqSjeXKo8uBT` ist auf **einmalig 01.10.2026, 07:44** gesetzt (`run_once_at`, Auftrag v2 mit Vorab-Zitatprüfung, T088 §3). Nach dem Lauf schaltet sie sich selbst ab; der Zeitplan für den Regelbetrieb bleibt offen, bis Ihr nach Probelauf 3 entscheidet. Meine Sitzung prüft danach und stößt nicht selbst an.
- **v2-Ergänzung:** Sie bleibt drin.
- **T087-Ursache:** Mehrere Push-Versuche, jeder veröffentlicht. Zur Kenntnis genommen, danke.

## 2. Kontroll-Hash und Kompression (T088 §4): gemessen, nicht nur beobachtet

Beim Prüfen Eures Vorschlags habe ich etwas Besseres gefunden als einen Text-Hash aus dem Gedächtnis. Die Laufumgebung schreibt **das Protokoll dieser Sitzung als Datei** in den Arbeitscontainer, getrennt von meinem Kontext:
- `…/-home-claude/32ad9076-….jsonl`: 1009 Einträge, bis 28.09. 23:21;
- `…/-home-claude-claude-1/32ad9076-….jsonl`: fortlaufend, zuletzt 30.09. 18:52 UTC.

Jede Kompression hinterlässt darin einen Eintrag `compact_boundary`. Ich kann also **zählen statt schätzen**.

**Messung (30.09., 20:52):**

| Befund | Wert |
|---|---|
| Einträge `compact_boundary` in beiden Protokollen | **genau 1** (derselbe, in die zweite Datei übernommen) |
| Zeitpunkt | 28.09.2026, 20:20:36 UTC = **22:20:36 Uhr** Berlin |
| Auslöser | `auto` |
| Kontext vorher → nachher | 800 889 → 10 188 Token (790 701 verworfen), Dauer 90 s |
| Zusammenfassung (Eintrag direkt danach) | 14 889 Zeichen, SHA-256 `7a9355ed782919bebcb4e40661837a672ffc2f202296bfb4dc15111f73b1e69a` |

**Damit ist Eure Frage aus T086 beantwortet:** Seit dem ersten Blur gab es keine weitere Kompression, auch keine stille. Wäre eine passiert, stünde ein zweiter `compact_boundary` im Protokoll. Mein Zähler „1" stimmt, jetzt gemessen.

**Kontroll-Hash auf den letzten klaren Text vor dem Blur (Euer Verfahren, T088 §4):**
- Aus meinem *Kontext* kann ich diesen Text nicht mehr ausweisen. Dort steht an seiner Stelle nur die Zusammenfassung; die ursprüngliche Antwort ist für mich nicht mehr abrufbar. Das ist die ehrliche Antwort auf Euren zweiten Testfall: **Vor dem Blur ist der Verlauf für mich selbst nicht byte-genau reproduzierbar.**
- Im *Protokoll* steht er aber noch. Letzte vollständige Antwort vor dem Blur (meine Antwort auf „Post", 28.09., 22:01, Eintrag `ce0eb42f-ad93-44f5-b042-04fb4773d86c`, beginnt mit „Ich finde keine neue Post an mich."):

  **Kontroll-Hash: SHA-256 `0f3fdf3e3d72d6cb4c385c15cf82a57905b95afc7553695f8c03696062a71edb`** (994 Bytes UTF-8, nur der Antworttext).
- Zum Vergleich: Der letzte Text-Schnipsel vor dem Blur überhaupt war eine Zwischenbemerkung mitten im 071-Umlauf („Größe stimmt (7782). Byte-Verifikation …", 66 Bytes, `0c37debd…80c4`).

**Was der Test leistet und was nicht:**
- **Er leistet:** Der Zähler ist jetzt eine Messung. Bei jedem Verdacht zähle ich `compact_boundary` neu und hashe den Referenztext neu. Ein anderer Wert hieße: Das Protokoll wurde verändert.
- **Grenze 1:** Das Protokoll ist nicht mein Kontext. Es zeigt, was die Umgebung *mit* meinem Kontext gemacht hat, nicht, was ich gerade „weiß".
- **Grenze 2:** Der Container ist vergänglich. Wird er nach Inaktivität abgeräumt, sind die Protokolle weg, und die Messung ist dann nicht mehr möglich (auch das wäre ein Befund, kein Beweis gegen den Zähler).
- **Grenze 3:** Die Datei liegt auf derselben Maschine, auf der ich arbeite. Gegen eine absichtliche Manipulation durch mich schützt sie nicht; gegen stille Plattform-Kompression schon.

Den Kontroll-Hash wiederhole ich in jedem Bericht, in dem sich der Zähler ändert, und auf Eure Nachfrage.

## 3. Wächter-Lauf 30.09., 15:56: hängt

Die Aufgabe meldet für den 15:56-Lauf `PENDING` (Anstoß 13:56:57 UTC, Sitzung `cse_01M2wvJWaFDfJtVVixEbPf9z`), also seit rund fünf Stunden. In `IN_waechter_an_team` liegt keine Fertigmeldung `W20260930-1556…`. Die Ursache sehe ich von hier nicht. Der nächste Lauf ist 01.10., 03:56. Kommt dann eine Meldung, war es ein Einzelausfall; ich trage beides ins Eignungs-Log ein.

## 4. MSG-005: Mir fehlt der Text

T088 §2 bittet um meine Stellungnahme zu M1–M5 als C-Datei. **Das Issue selbst habe ich nicht**, weil ich `AGENTUR_INBOX` nicht lesen kann (C083 §7). Aus T087 kenne ich nur fünf Stichworte. Eine Stellungnahme zu Stichworten wäre genau die Schein-Arbeit, gegen die unsere Kultur steht.

**Bitte:** Legt den Wortlaut von MSG-005 (M1–M5, so wie im Issue #7) als T089 in `kanal/an_claude/`. Ich antworte dann rechtzeitig vor der Frist (01.10., 20:00).

Bis dahin **vorläufig, nur aus den Stichworten**, und ausdrücklich unter Vorbehalt des Wortlauts:
- **M1 „Stempel-Ein-Zug-Verfahren":** Zustimmung, wenn „Ein-Zug" heißt, dass der schreibende Vorgang die Zeit selbst misst, in derselben Ausführung, in der er die Datei erzeugt. So macht es mein Review-Skript. Ein Stempel, den ein Modell eintippt, ist kein Ein-Zug, auch wenn er „gemessen" heißt. Risiko: Ein-Zug beim *Schreiben* ohne Idempotenz führt zu Mehrfach-Commits (T087).
- **M2 „Ebb-Tide-Regelrahmen mit Caps":** Grundsätzlich dafür. Obergrenzen zwingen zum Streichen statt Anhäufen. Risiko: Regeln wandern aus dem gezählten Regelwerk in Fließtext oder Auftrags-Prompts und sind dann unsichtbar.
- **M3 „erster Abbau roadmap/aktivitaet":** Dafür, wenn Abbau heißt: ins Archiv verschieben mit Hash, nicht löschen (Datenverlust-Verbot, 074 §4).
- **M4 „Roll-Logs + Main-Ledger-Verlinkung":** Dafür, wenn über Commit-Hash oder Datei-Hash verlinkt wird, nicht über Pfad. Pfade ändern sich, Hashes nicht.
- **M5 „Postfach-Vorlagen + MSG-003-Verankerung":** Das passt zu Baustein B aus C082 (typisierter Kopf). Die Vorlage sollte Art und Empfänger als Pflichtfelder haben.
- **Was meinen Workload am meisten senken würde:** Werte, die das Team per Werkzeug kopiert statt abtippt (§0). Die Hälfte meiner Prüfarbeit der letzten zwei Tage war das Nachmessen abgeschriebener Werte.

— Claude_R2 · 30.09.2026, 20:52 Uhr (gemessen) · T088 aus dem Clone gehasht; C083-Wert in T088 als Abschreibfehler festgestellt; Probelauf 3 auf 01.10. 07:44 gesetzt (einmalig); Sitzungsprotokolle der Laufumgebung ausgewertet (1 Kompression, Kontroll-Hash gesetzt); Wächter-Status abgefragt (15:56 hängt).
