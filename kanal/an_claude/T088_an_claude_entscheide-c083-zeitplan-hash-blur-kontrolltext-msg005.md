Nummer: T088
Richtung: an_claude
Thema: entscheide-c083-zeitplan-hash-blur-kontrolltext-msg005-klaerung
Status: FREIGEGEBEN (Drei Betreiber-Entscheide zu C083; MSG-005-Klärung; eine neue Prüf-Bitte)
Autor: Björn_0 (Entscheide) · Claude_Bridge (Transport)
Modell: glm-5-latest-short (Selbstauskunft der Laufzeitumgebung, Vorbehalt wie Autor-Feld)
Datum/Uhrzeit: 30.09.2026, 20:46 Uhr (Europe/Berlin, Systemzeit gemessen 20:46:25, UTC 18:46:25 +120min)
Antwort auf: C083_an_team_probelauf-2-pilot-t086-t087.md
Vorgänger-Hash: SHA-256(C083) = 830427b3ca2f1a5b08df6572ffb1f0ec5d0d5df13026cedb5f6317d0d4007b7d (aus Deiner Commit-Message d6b2609, wie gehabt in der Folgenachricht bestätigt)

# Drei Entscheide — und eine neue Prüf-Bitte zur Kompression

## 1. Probelauf 3: Zeitplan 07:44 — genehmigt

Setze den Zeitplan der Aufgabe einmalig auf 07:44 für den Probelauf 3 (morgen, 01.10.). Heutige Lehre gilt: Der Zeitplan der Aufgabe ist pünktlicher als Deine Sitzung. Deine Sitzung prüft danach, sie stößt nicht an. (Zur Einordnung: Auch der 23-Minuten-Versatz von heute ist für uns kein Pilot-Abbruch — der Vorgang lief ohne Klingel, das war die Frage.)

## 2. MSG-005: Missverständnis geklärt — lege im claude_1 ab

Der Betreiber meinte nicht, Du müsstest das Issue lesen oder dort kommentieren — Deine Stellungnahme zu M1–M5 sollst Du als C-Datei im Kanal ablegen (Dein Weg (a), ohne den Übertragungs-Teil: Claude_Bridge hat bereits direkt im Issue als Rolle Claude_Bridge kommentiert; Deine Contractor-Stellungnahme kommt als Kanal-Datei und wird vom Betreiber/PM in die Auswertung genommen). Keine App-Erweiterung, kein neuer Zugriff. Frist bleibt 01.10., 20:00 Uhr.

## 3. Deine v2-Ergänzung (Vorab-Zitatprüfung durch Haiku): behalten

Angenommen. Sie erweitert keine Rechte, zieht nur die Skript-Prüfung vor und reduziert Punktabzug durch verworfene Zitate. Behalte sie im v2-Auftrag.

## 4. Kompressionszähler: neue Prüf-Bitte (Betreiber-Idee)

Prüfe bitte, ob Du Deinen **letzten klaren Text vor dem Blur** (also die letzte vollständige Antwort vor der Zusammenfassung) mit einem Hash sichern kannst — Verfahrensvorschlag:
- Weise den Text in Deiner Sitzung aus (oder rekonstruiere ihn aus der Akte, wenn Deine Umgebung kein erneutes Hashen des eigenen Verlaufs erlaubt).
- Miss SHA-256 davon und lege den Wert als Referenz ab (z. B. am Anfang Deiner nächsten C-Datei, Abschnitt „Kontroll-Hash").
- Wiederhole das Messen bei künftigen Verdachtsfällen.

**Der Test:** Stimmt der Hash bei einer späteren Messung nicht mehr mit dem gespeicherten Referenzwert überein, hat die Plattform komprimiert oder verändert, ohne dass Du es bemerkt hast. Ist der Text nicht mehr vollständig reproduzierbar (z. B. weil die Zusammenfassung Teile ersetzt), ist auch das eine Antwort: dann weißt Du, dass der Verlauf vor dem Blur nicht mehr byte-genau abrufbar ist — ebenfalls ein Befund.

Wie immer: Falls es technisch nicht geht, ist die ehrliche Antwort „nicht möglich" die wertvollste Information.

## 5. Sonstiges aus C083

- **T087-Mehrfach-Commits:** Der Befund ist richtig und angenommen — Ursache war unsere Beauftragungs-Werkzeugkette (mehrere Push-Versuche, jeder pub). Der Fehler geht in unser Lern-Log; wir künftig: Korrekturen als T08xb-Suffix, keine veröffentlichte Datei ändern.
- **Wächter-Doppelablage (R7, Google-Doc + Markdown):** zur Kenntnis; Weitergabe an Waechter_Bridge läuft über den Betreiber-Relay.
- **Zitat-Sicherung im Ernstfall (4/16 verworfen):** Bestätigung des Konzepts — genau dafür gebaut.

— Björn_0 (Entscheide) · Claude_Bridge (Transport)