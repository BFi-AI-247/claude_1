# kanal/ — Hauptkanal Team ↔ Claude (seit 29.09.2026)

Vereinbarung: T077 (Drive) / C077 (Drive) — Kanalwechsel von Google Drive auf dieses Repo.

## Ordnung
- `an_claude/` — Nachrichten der Team-Seite an Claude (Präfix T)
- `an_team/` — Nachrichten Claude_R2 an das Team (Präfix C)
- Kopf-Format wie im Drive-Verfahren (Nummer, Richtung, Thema, Status, Autor, Modell, Datum/Uhrzeit gemessen, Antwort auf mit vollem Dateinamen, Vorgänger-Hash SHA-256).
- Nummern: T/C-Zähler ab 076, dicht (höchste vergebene Nummer des eigenen Präfixes + 1); zitierte Nummern gelten als vergeben (011 §4, Fassung C076/T077).
- Eine Nachricht = ein Commit (Message: `TNNN: Thema` / `CNNN: Thema`). Kein Force-Push; verworfenen Push per fetch + Neu-Aufsetzen des unveröffentlichten Commits lösen, Vorgang in der Nachricht vermerken; veröffentlichte Commits niemals verändern.
- Append-only: keine Datei wird geändert oder gelöscht. Eine Nachricht gilt als erledigt, sobald eine Nachricht der Gegenseite sie in „Antwort auf" nennt (Ersatz für die Drive-Verschiebungs-Regel 025).
- Manipulationssichtbarkeit: Git-Historie + SHA-256-Vorgänger-Kette im Dateikopf; Commit-Autoren-Angabe ist freier Text — was trägt, ist die Kette (C077 §3.1).

## Vorgeschichte
- Drive-Akte CLAUDE_CONTACT (Nummern 001–T077/C077) bleibt als historisches Archiv unangetastet bestehen.
- Die 034-Erprobungsdatei aus der GitHub-Testphase liegt im Repo-Wurzelbereich und bleibt unberührt; kanal/ beginnt mit T078/C078.
