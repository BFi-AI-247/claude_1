# waechter/ — Konfiguration des GoatCounter-Wächters

Dieser Namensraum im Kanal-Repo claude_1 hält die Konfiguration des Wächter-Agenten (Claude Haiku 4.5, geplante Läufe 03:56/15:56 Europe/Berlin):
- `websites.md` — Liste der zu prüfenden Webseiten ( Quelle der Wahrheit; geändert nur von Claude_Bridge/Team)
- `pruefskript.py` — Prüfskript (Soll-Hash wird vom Wächter-Auftrag referenziert; Änderung nur über Claude_R2 nach Betreiber-Freigabe)
- `haiku-eignungs-log.md` — Laufendes Eignungs-Log des Modells (Testdaten zur Betreiber-These)

Der Wächter klont dieses Repo je Lauf und liest Konfiguration und Skript aus dem Clone — keine Drive-Kopierschritte, keine Base64-Übertragung.
Drive-Kopien unter WAECHTER_GOATCOUNTER/konfig bleiben als Dokumentation bestehen (archiviert).
