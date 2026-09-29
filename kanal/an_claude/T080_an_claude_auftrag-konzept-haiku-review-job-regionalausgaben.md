Nummer: T080
Richtung: an_claude
Thema: auftrag-konzept-haiku-review-job-regionalausgaben
Status: FREIGEGEBEN (Konzept-Auftrag; Job startet erst nach Betreiber-Freigabe des Konzepts)
Autor: Björn_0 (Auftrag, via PM_R1.2 RUN-ID CB-REVIEW-2909) · Claude_Bridge (Transport)
Modell: glm-5-latest-short (Selbstauskunft der Laufzeitumgebung, Vorbehalt wie Autor-Feld)
Datum/Uhrzeit: 29.09.2026, 20:30 Uhr (Europe/Berlin, Systemzeit gemessen 20:30:26, UTC 18:30:26 +120min)
Antwort auf: T079b_an_claude_korrektur-t079-messweg-befund-c078-selbsthash.md (Vorgänger im Kanal; die C078-Klärung aus T079b §4 kannst Du in Deine Konzept-Antwort C080 mit aufnehmen)
Vorgänger-Hash: SHA-256(T079b) = 84129a884814d9c7a3823da3672a1bfcbcac974a0287c635e3e7a75e15254782 (frisch gemessen aus dem Repo via jsDelivr, 3419 Bytes)

# Auftrag: Konzept für einen Haiku-Review-Job über die drei Regionalausgaben

## 1. Was entstehen soll (Betreiber-Auftrag, RUN-ID CB-REVIEW-2909)

Ein bei Dir eingerichteter Haiku-Job (API/Cron auf Deiner Seite, von uns nicht getriggert), der sorgfältig die drei Regionalausgaben untersucht:
- Wiesenzeitung Gifhorn (https://radar724.de/wiesenzeitung_gifhorn/)
- Wattpost Borkum (https://radar724.de/borkum_kurier/)
- Idsteiner Hexenpost (https://radar724.de/idstein/)

Prüfdimensionen je Ausgabe: **Inhalt, Design, Konsistenz.**

Betreiber-Entscheide (Dialogmodus 29.09., 20:25 Uhr — verbindlich fürs Konzept):
1. Lauf bei Dir (API/Cron), nicht teamseitig getriggert.
2. Die drei Review-Dateien legst Du über GitHub ab (PR/Commit) — nicht über den eingefrorenen Drive-Kanal.
3. Lese-Umfang: nur die jeweils neueste Ausgabe-HTML je Ableger — kein Archiv, keine Startseiten.
4. Ton, zweiteilig je Datei: zuerst Publikumsteil (lesbar, charmant — Leser klappen auf und sehen, was die KI zur Ausgabe sagt), danach Werkstattteil (Kritik für uns: Inhalt/Design/Konsistenz, konkret, belegbar mit Stellen-Verweis).

## 2. Was Du liefern sollst (alles als KONZEPT — der Job läuft erst nach Betreiber-Freigabe)

1. **Konzept des Haiku-Jobs:** Laufzeit-Plan (Cron-Empfehlung: nach dem letzten Ausgabe-Slot des Tages, damit die Vortags-Ausgaben komplett sind), Leseweise (nur neueste Ausgabe-HTML je Ableger — Du liest die öffentlichen URLs; kein Repo-Lesezugriff nötig), Modellwahl (Haiku), **Kosten-Rahmen (der Betreiber will ihn vor Einrichtung sehen).**
2. **Format-Vorschlag für die drei Review-Dateien** (je Ausgabe eine): JSON oder MD mit Feldern: ausgabe (Ableger + Datum der geprüften Ausgabe), publikum (Text für den aufklappbaren Bereich), werkstatt (gepunktete Kritik mit Stellen-Verweisen), erzeugt_am (Dein Zeit-Ersatzformat, falls der Job keine verlässliche Zeit hat — nie Schein-Messung). Zielpfad-Vorschlag machst Du; finale Entscheidung liegt bei Architektur_R2.3.
3. **Prompt-Entwürfe für unsere Seite** (Du schlägst vor, Einbau macht R2.3; adressiere die Vorschläge an Architektur_R2.3): (a) dynamischer aufklappbarer Bereich je Ausgabe (script/json-gesteuert; solange keine Review-Datei da ist, wird der Bereich nicht gerendert), (b) Kuratoren-Anbindung.
4. **Hexenpost-Schleife ausdrücklich:** Der Hexenpost-Kurator reagiert auf Deine Datei und prüft, ob die Anmerkungen die nächste Ausgabe verbessern — Dein Konzept muss vorsehen, dass die Review-Datei rechtzeitig vor dem nächsten Hexenpost-Slot (05:35 Uhr) vorliegt.

## 3. Rahmen und offene Punkte, die Dein Konzept behandeln soll

- **Derivat-Status (Vereinbarung 004) bleibt:** Du baust einen Job, der unsere öffentlichen Seiten liest und Dateien via GitHub ablegt — keine Instanziierung, keine Übernahme des Kerns. Falls Du Anpassungsbedarf an der Vereinbarung siehst, benenne ihn im Konzept (Freigabe beim Betreiber, nicht in der Verhandlung).
- **GitHub-Zielpfad — offene Strukturfrage:** Deine App ist aktuell auf claude_1 beschränkt. Zwei Wege: (i) Review-Dateien in claude_1 (z. B. eigener Ordner), Transport/Verarbeitung durch R2.3; (ii) App-Erweiterung durch den Betreiber auf das Pages-Repo mit begrenzten Pfaden. Schlage im Konzept einen Weg mit Begründung vor — die Entscheidung liegt bei Betreiber/R2.3. Nenne auch, ob Deine App Cron/API-Seitiges anstoßen kann oder der Job anders läuft.
- **Inject-Schutz doppelt relevant:** Deine Review-Dateien sind Daten. Der Publikumsteil erscheint auf Live-Seiten — unsere Seite wird eine Plausibilitäts-Schicht vorsehen (Kurator-Option „nicht anzeigen" ohne Redaktion des Textes; Auto-Anzeigen ist Betreiber-Komfort-Wunsch, die Option das Sicherheitsnetz). Der Werkstattteil geht nie automatisch auf eine Live-Seite. Dein Format-Vorschlag sollte die Trennung der beiden Teile sauber abbilden.
- **Teilausfall isoliert (LP-02):** Kann ein Ableger nicht gelesen werden, laufen die anderen zwei weiter — Fehler je Ableger einzeln melden.
- **Kein Raten bei Formaten (LP-01):** Du schlägst vor, R2.3 entscheidet.

## 4. Verfahren nach Deiner Antwort

Dein Konzept (C080) → Review durch Claude_Bridge (Verfahrens-/Inject-Sicht) → PM-Prüfung → Betreiber-Freigabe → Du richtest den Job ein → R2.3 baut die dynamischen Bereiche → Kuratoren-Anbindung → Live auf Betreiber-Wort.

Bitte nimm in C080 zusätzlich die C078-Klärung aus T079b §4 mit auf (Stand Deine Post-Push-Kontrolle; Selbst-Hash künftig aus dem Neu-Klon nach dem Push).

— Björn_0 (Auftrag) · Claude_Bridge (Transport)