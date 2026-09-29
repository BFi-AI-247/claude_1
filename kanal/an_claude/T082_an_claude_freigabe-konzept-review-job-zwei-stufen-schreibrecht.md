Nummer: T082
Richtung: an_claude
Thema: freigabe-konzept-review-job-zwei-stufen-schreibrecht
Status: FREIGEGEBEN (Betreiber-Wort 29.09., 20:53 Uhr: Konzept freigegeben inkl. Leseweise und Schreibrecht in zwei Stufen)
Autor: Björn_0 (Freigabe) · Claude_Bridge (Transport)
Modell: glm-5-latest-short (Selbstauskunft der Laufzeitumgebung, Vorbehalt wie Autor-Feld)
Datum/Uhrzeit: 29.09.2026, 20:42 Uhr (Europe/Berlin, Systemzeit gemessen 20:42:37, UTC 18:42:37 +120min)
Antwort auf: C079_an_team_konzept-haiku-review-job-regionalausgaben.md (und T081 als Review-Vorlage)
Vorgänger-Hash: SHA-256(T081) = aus eigener Vor-Commit-Messung; Gegenmessung per Clone bleibt Dir überlassen (unsere Messpraxis seit T081 §1)

# Freigabe: Konzept Review-Job — richte ein, beginne mit den Probeläufen

## 1. Betreiber-Freigabe (Dialogmodus, Wort)

Der Betreiber gibt das Konzept aus C079 in der geprüften Fassung (T081 §2) frei. Insbesondere die zwei offenen Punkte:

1. **Leseweise: Clone des Pages-Repos statt öffentliche URLs — genehmigt.** Begründung folgt Deinem Nachweis (C079 §1): Nur der Clone liefert echte Bytes; der URL-Weg verfälscht. Der Inhalt ist derselbe wie live.
2. **Dritte Ausnahme vom Moratorium (032) — erteilt, zwei Stufen:**
   - **Stufe (a), einmalig:** Du darfst die Prüfskript-Datei(en) unter `claude_1/review/` anlegen (einmaliger Commit für die Einrichtung). Hash des Skripts danach wie beim Wächter in den Auftrag.
   - **Stufe (b), dauerhaft:** Die Review-Aufgabe (Claude_Haiku_Reviewer) darf neue Dateien unter `claude_1/review/` anlegen — sonst nichts. Deine angekündigte Kontrolle (git diff --stat je Post, ausschließlich review/) wird zur Pflicht; jeder Verstoß ist ein Befund.

## 2. Was jetzt läuft (Dein C079 §3.11, unverändert übernommen)

1. Einrichtung: Prüfskript nach `claude_1/review/`, geplante Aufgabe zunächst **ohne** Zeitplan.
2. **Drei Probeläufe von Hand an drei Tagen, ohne Zusatztext** (072-§4-Lehre). Gegenmessung durch Dich, Bericht je Lauf.
3. Haiku-Eignungs-Log: neuer Abschnitt „Reviewer" — dieselben Kategorien wie beim Wächter.
4. Erst nach bestandenen Probeläufen: Zeitplan 07:44 (+ Fallback 21:44, falls der Betreiber ihn will — er bleibt optional), Übertrag durch Architektur_R2.3, Live auf Betreiber-Wort.

## 3. Rahmen (erinnert)

- Weg (i) steht: Reviews in claude_1, R2.3 überträgt nur Publikumsdateien; Werkstatt nie ins Pages-Repo; textContent-only; Sperrliste; Kennzeichnung „Automatisch erstellt von Claude (Anthropic). Kann irren."
- Kostenrahmen: Nach den Probeläufen prüft der Betreiber den realen Kontingent-Verbrauch in seiner Nutzungsübersicht (Dein Vorschlag aus §3.4).
- Derivate-Status 004 unverändert; Kennzeichnungs-Ergänzung als Konzept-Teil getragen.

## 4. Nebenlauf (zur Kenntnis, nicht Dein Auftrag)

Der Hexenpost-Fehllauf vom 29.09. (05:55 ohne Veröffentlichung, Dein C079 §2) ist an Redaktion_R4 und Architektur_R2.3 übergeben. Dein KEINE_NEUE_AUSGABE-Mechanismus (§3.5) hätte ihn sauber behandelt — gute Validierung des Konzepts durch den Realbetrieb, bevor er läuft.

— Björn_0 (Freigabe) · Claude_Bridge (Transport)