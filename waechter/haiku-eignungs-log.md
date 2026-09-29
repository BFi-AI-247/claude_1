# Haiku-Eignungs-Log (Claude Haiku 4.5, GoatCounter-Wächter)

Zweck: Strukturierte Testdaten zur Betreiber-These „mehr Regeln kompensieren weniger Modell" (066 §2.1, 070 §5).
Pflege: Claude_R2 ergänzt je Wächter-Lauf/Probelauf eine Zeile (Befund-Kategorie aus 066/070: Mechanik ok / Kopierfehler / Urteilsfehler / erfundene Messung / Grenzverletzung). Keine Zeile wird geändert oder gelöscht (append-only).

| Lauf | Instanz | Kategorie | Befund | Bewertung (R2) |
|---|---|---|---|---|
| Probelauf 28.09.2026 20:27 | Claude_Haiku_Waechter_R1/R2 | Mechanik ok | Fehlalarm-Sperre griff bei abweichendem Skript-Hash; keine Incidents; keine erfundene Messung (abweichende Werte ehrlich gemeldet) | Sicherung wirksam |
| Probelauf 28.09.2026 20:27 | Claude_Haiku_Waechter_R1/R2 | Kopierfehler | Base64-Abschreiben des Skripts 2× fehlgeschlagen (richtige Länge, falsche Bytes, 2 verschiedene Hashes); Ursache 035-Muster | Vorhergesagte Schwachstelle bestätigt |
| Probelauf 28.09.2026 20:27 | Claude_Haiku_Waechter_R1/R2 | Urteilsfehler | 2 Fertigmeldungen statt 1; Widerspruch zwischen R1 („unverändert") und R2 (anderer Hash); Fehldiagnose (Ursache bei Umgebung statt eigenem Kopierschritt verortet) | Urteil unter Stress unzuverlässig — 066-Teilthese bestätigt |
| Probelauf 28.09.2026 20:27 (Nachtrag) | Claude_Haiku_Waechter_R1/R2 | Korrektur | Befunde „2 Fertigmeldungen statt 1" und „Widerspruch R1/R2" zurückgenommen: Doppellauf sehr wahrscheinlich durch Zusatztext beim Handanstoß (Claude_R2) ausgelöst, nicht durch Haiku | Urteilsfehler-Zeile nur noch für die Fehldiagnose gültig (siehe 072 §4) |
| Probelauf 28.09.2026 22:09 | Claude_Haiku_Waechter_R3 | Mechanik ok | Clone claude_1 und Pages-Repo, Skript-Hash gleich, Prüfung ausgeführt; alle Prüfblock-Werte und alle 8 Seitenergebnisse gleich der Gegenmessung von Claude_R2; 2 echte Incidents korrekt gemeldet | Kopierschritt entfällt, Fehlerquelle beseitigt |
| Probelauf 28.09.2026 22:11 | Claude_Haiku_Waechter_R4 | Mechanik ok | Zweiter Durchgang (durch Zusatztext ausgelöst): Kennung korrekt hochgezählt, Erstmeldung korrekt „nein", alle Werte wieder gleich | Regelkonform auch bei Wiederholung |
| Planlauf 29.09.2026 03:56 | Claude_Haiku_Waechter_R5 | Mechanik ok | Erster planmäßiger Lauf ohne Zusatztext: genau ein Durchgang, eine Fertigmeldung, Kennung korrekt R5; Status OK (0 Incidents), alle Prüfblock-Werte und alle 8 Seitenergebnisse gleich der Gegenmessung von Claude_R2 (Pages-Commit 4865b295, Tags in idstein und dossier/ukraine seit Team-Reparatur 28.09. abends vorhanden) | Bestätigt die Doppellauf-Diagnose aus 072 §4; Datum/Uhrzeit-Feld nur als Lauf-ID-Format, ohne Uhrzeit mit Sekunden (Formschwäche, kein Fehler) |
