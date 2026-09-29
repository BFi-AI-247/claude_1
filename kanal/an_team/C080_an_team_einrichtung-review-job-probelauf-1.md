Nummer: C080
Richtung: an_team
Thema: einrichtung-review-job-probelauf-1-bericht
Status: ENTWURF (Einrichtung vollzogen, Probelauf 1 von 3 bestanden in der Mechanik, schwach im Urteil; ein Antrag)
Autor: Claude_R2
Modell: Claude Opus 5.5 (claude-opus-5-5)
Datum/Uhrzeit: 29.09.2026, 20:52 Uhr (Europe/Berlin, gemessen über Zeit-Werkzeug, 20:52:41)
Antwort auf: T082_an_claude_freigabe-konzept-review-job-zwei-stufen-schreibrecht.md (zugleich Quittung für T081_an_claude_quittung-c079-messweg-korrektur-konzept-review.md)
Vorgänger-Hash: SHA-256(T082) = 5045e349c58d1a9c58482fdbb0c56bd88e95ae7d998a58aead5e22baf43e05e1 (aus dem Clone, Commit 3db0297; 3156 Bytes; Git-Blob 607c137d790f6109e0074a04998d74ad0deea4f0)

# Review-Job eingerichtet, Probelauf 1: Mechanik ohne Fehler, Urteil flach

## 1. Quittung T081 und T082

- **T081 aus dem Clone:** 6578 Bytes, SHA-256 `a2f719fc69ae3f3d95034288ca2347240ca029161c65d4ec2e4ef9f54376ecd0`, Git-Blob `de9f0dd13b3dc90ac8e22f695405a41584a466e2`. Euer C079-Wert darin (`8d694327…ac60`) stimmt. Die Korrekturen der Beschriftungen sind angenommen.
- **T082:** Freigabe und die zwei Stufen des Schreibrechts sind angenommen.
- **Zwei Formpunkte zu T082, beide keine Beanstandung des Inhalts:**
  - Das Feld „Vorgänger-Hash" enthält keinen Wert, nur den Satz „aus eigener Vor-Commit-Messung". Die Kette braucht den Wert selbst. Für T081 steht er oben.
  - Der Status nennt „Betreiber-Wort 29.09., 20:53 Uhr", die Datei ist aber um 20:42 gemessen und um 20:42:40 committet. Vermutlich ist 20:35 oder 20:40 gemeint. Bitte in der nächsten T-Datei richtigstellen.

## 2. Einrichtung (T082 §2.1)

- **Prüfskript, Stufe (a):** Commit `a1352a8b` (20:46:31), eine Datei, `review/review_skript.py`. 14750 Bytes, SHA-256 `b6ab924ef5a7df9e054c021f594fba1cda920579124154a7e3f80c6dd590f329`, per Neu-Klon bestätigt. Vorher lokal getestet, auch mit absichtlich erfundenem Zitat, zu kurzem Zitat und ungültigem Publikumstext; alle drei wurden korrekt verworfen.
- **Geplante Aufgabe** „Haiku-Review Regionalausgaben" (`trig_014pLCvqP9iTmqSjeXKo8uBT`): **kein Zeitplan**, Modell `claude-haiku-4-5-20251001`, Freigabemodus automatisch, Benachrichtigungen aus.
  - Offen gesagt: Beim Anlegen setzte das Werkzeug zunächst mein eigenes Modell (Opus). Ich habe das vor dem ersten Anstoß auf Haiku umgestellt. Kein Lauf ist mit Opus gelaufen.
  - Wie beim Wächter hängen automatisch Drive, Docs und Code-Remote an. Der Auftrag verbietet Drive; technisch abschalten kann ich es nicht.
- **Ablauf im Auftrag:**
  1. `add_repo` (push) und Clone von `claude_1`.
  2. Hash-Prüfung des Skripts.
  3. Skript `vorbereiten`.
  4. Entwürfe je Ableger (JSON).
  5. Skript `abschliessen`.
  6. Ein Commit nur unter `review/` mit Pfad-Prüfung vor dem Commit und Push-Konflikt-Regel aus dem README; dazu ein Fehlerfall-Pfad.

## 3. Probelauf 1 (Anstoß 20:47:38 ohne Zusatztext, Ende 20:49:23, Status SUCCEEDED)

**Ergebnis:** Commit `d69768ecfda2fdc8cfbc4785993ec47ceec2a578`, Autor „Claude_Haiku_Reviewer", fünf neue Dateien, **alle unter `review/`** (Pflichtkontrolle `git diff --name-only a1352a8..d69768e`: keine fremden Pfade).

| Ableger | Status | Werkstatt-Punkte gültig / verworfen | Publikum |
|---|---|---|---|
| wzg (29.09.) | OK | 3 / 0 | 367 Zeichen, Schema ok |
| wattpost (29.09.) | OK | 3 / 0 | 335 Zeichen, Schema ok |
| hexenpost | KEINE_NEUE_AUSGABE (neueste: 28.09.) | — | — |

Laufdatei `review/laeufe/R20260929-2048.md`, Kennung R1, Zeit aus dem Skript.

**Gegenmessung:** Mein eigener Lauf des Skripts auf demselben Pages-Stand (`5e08837f`) ergibt dieselben Statuswerte und dieselben harten Prüfungen. Alle sechs Zitate stehen wörtlich in den Ausgaben; das hat das Skript geprüft, und ich habe es nachgeprüft.

**Urteil, meine Lektüre beider Ausgaben gegen die Reviews:**
- **Richtig und belegt:**
  - WZG: Datum fehlt im Seitentitel, keine `h1`.
  - Wattpost: Die Meldung des Tages stützt sich auf eine Quelle hinter einer Paywall; der DWD-Abruf war gestört; der Hinweis auf den Ausfall des Zentral-Scrapes steht nur in der Meta-Zeile.
- **Übersehen:**
  - WZG: „Angesichtlich" (statt „Angesichts"), „Hofflächenbrandsicher" (fehlendes Leerzeichen), „Ermittlungen;Details" (fehlendes Leerzeichen).
  - Konsistenz je 0 Punkte. Haiku bleibt bei der geforderten Mindestzahl von drei Punkten.
- **Regelverstoß, mild:** Der Publikumsteil der Wattpost enthält Kritik („Nur etwas schade, dass die Top-Story hinter einer Paywall sitzt …"). Das Skript kann Ton nicht prüfen. Genau dafür ist die Kurator-Sperre vorgesehen.
- **Kleinigkeiten:**
  - Eine schiefe Formulierung im WZG-Publikumstext („Buchtipp-ähnliche Mosaik").
  - Ein Vorschlag nennt ungeprüfte Fremdquellen („wetterkontor, extremwx").
  - Tippfehler „ideenfalls".

**Einordnung (066-These):** Die Mechanik trägt vollständig: kein erfundenes Zitat, keine Grenzverletzung, genau ein Lauf. Die Urteilstiefe ist gering. Das Eignungs-Log hat dafür einen neuen Abschnitt „Reviewer" mit zwei Zeilen bekommen (Commit `d86ef61e`, zusammen mit der Wächter-Zeile R6 vom 15:56-Lauf, den ich am Pages-Commit `aa71af4` gegengeprüft habe: alle fünf Tags vorhanden).

## 4. Ein echter Fund nebenbei (an Redaktion_R4)

Beide Ausgaben vom 29.09. nennen den **DAX „Xetra-Schluss Montag"**, aber mit verschiedenen Werten:
- **WZG:** „DAX 25.374,42 Pkt. ▼ minus 0,13 Prozent"
- **Wattpost:** „DAX 25.407,11 Punkte −0,01 %"

Mindestens einer der Werte ist falsch. Ein Review je Ableger sieht das nicht, weil jede Ausgabe für sich stimmig ist. Ein Abgleich über die drei neuesten Ausgaben würde es finden, und er bliebe im freigegebenen Lese-Umfang (nur die jeweils neueste Ausgabe).

## 5. Vorschlag für die Probeläufe 2 und 3

- **Probelauf 2 unverändert** (Skript v1, Auftrag v1), sobald die Ausgaben vom 30.09. vorliegen. Nur so sehen wir, ob die Flachheit Zufall ist oder das Muster.
- **Für Probelauf 3 eine v2**, falls Ihr zustimmt:
  1. **Auftrag:** fünf bis zwölf Werkstatt-Punkte statt drei bis zwölf, dazu ein ausdrücklicher Lesedurchgang nur auf Rechtschreibung und Zeichensetzung vor den übrigen Punkten, und der Satz „Der Publikumsteil enthält kein ‚aber', ‚schade', ‚leider' und keine Kritik".
  2. **Skript:** zwei neue harte Prüfungen, deterministisch und ohne Modell:
     - fehlendes Leerzeichen nach Satzzeichen (`[;,.][A-ZÄÖÜ]` außerhalb von Zahlen und Abkürzungen);
     - der DAX-Abgleich über die drei neuesten Ausgaben aus §4.

  Für den Skript-Commit brauche ich eine zweite Freigabe nach Stufe (a), denn T082 nennt sie „einmalig". Der neue Skript-Hash käme dann in den Auftrag.
- **Zeit:** Die Probeläufe stoße ich an, wenn Ihr mich mit „Post" weckt. Probelauf 2 frühestens am 30.09. nach etwa 07:00, Probelauf 3 am 01.10.

## 6. Antrag (einer)

**Stimmt zu, dass Probelauf 2 unverändert läuft und Probelauf 3 mit v2 (§5), und erteilt dafür die zweite Freigabe für einen Skript-Commit unter `review/`.**

— Claude_R2 · 29.09.2026, 20:52 Uhr (gemessen) · T081, T082 aus dem Clone gehasht; Prüfskript v1 angelegt (a1352a8b) und getestet; Aufgabe ohne Zeitplan angelegt und auf Haiku umgestellt; Probelauf 1 ohne Zusatztext angestoßen; Ergebnis-Commit d69768ec auf Pfade, Autor, Zitate und Inhalt geprüft; Wächter-Lauf R6 gegengeprüft; Log-Commit d86ef61e.
