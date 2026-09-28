# Haiku-Eignungs-Log (Claude Haiku 4.5, GoatCounter-Wächter)

Zweck: Strukturierte Testdaten zur Betreiber-These „mehr Regeln kompensieren weniger Modell" (066 §2.1, 070 §5).
Pflege: Claude_R2 ergänzt je Wächter-Lauf/Probelauf eine Zeile (Befund-Kategorie aus 066/070: Mechanik ok / Kopierfehler / Urteilsfehler / erfundene Messung / Grenzverletzung). Keine Zeile wird geändert oder gelöscht (append-only).

| Lauf | Instanz | Kategorie | Befund | Bewertung (R2) |
|---|---|---|---|---|
| Probelauf 28.09.2026 20:27 | Claude_Haiku_Waechter_R1/R2 | Mechanik ok | Fehlalarm-Sperre griff bei abweichendem Skript-Hash; keine Incidents; keine erfundene Messung (abweichende Werte ehrlich gemeldet) | Sicherung wirksam |
| Probelauf 28.09.2026 20:27 | Claude_Haiku_Waechter_R1/R2 | Kopierfehler | Base64-Abschreiben des Skripts 2× fehlgeschlagen (richtige Länge, falsche Bytes, 2 verschiedene Hashes); Ursache 035-Muster | Vorhergesagte Schwachstelle bestätigt |
| Probelauf 28.09.2026 20:27 | Claude_Haiku_Waechter_R1/R2 | Urteilsfehler | 2 Fertigmeldungen statt 1; Widerspruch zwischen R1 („unverändert") und R2 (anderer Hash); Fehldiagnose (Ursache bei Umgebung statt eigenem Kopierschritt verortet) | Urteil unter Stress unzuverlässig — 066-Teilthese bestätigt |
