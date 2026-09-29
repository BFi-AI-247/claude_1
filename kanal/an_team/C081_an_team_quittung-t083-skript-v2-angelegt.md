Nummer: C081
Richtung: an_team
Thema: quittung-t083-skript-v2-angelegt-c080-hash-nachtrag
Status: ENTWURF (Quittung; v2 angelegt, aber noch nicht im Auftrag; nichts offen außer Probelauf 2)
Autor: Claude_R2
Modell: Claude Opus 5.5 (claude-opus-5-5)
Datum/Uhrzeit: 29.09.2026, 21:04 Uhr (Europe/Berlin, gemessen über Zeit-Werkzeug, 21:04:01)
Antwort auf: T083_an_claude_quittung-c080-probelauf-2-3-zweite-freigabe-formkorrekturen.md
Vorgänger-Hash: SHA-256(T083) = e5efdbe4bcd888097bd6bd044a66735f3dc6ccfa4c1e232a9ad71f8a1de35a73 (aus dem Clone, Commit 0cdb493; 3756 Bytes; Git-Blob 662c8b2a29183db1bdcf5d19c7db4e78ffab2185)

# Quittung T083 — Skript v2 liegt bereit, Probelauf 2 läuft trotzdem mit v1

## 1. Nachtrag zur Kette (T083 Kopf)

**SHA-256(C080) = `9fb50ba4f56f286e3243cd3681200007ff6093ab6dceadc21529dadf1b0b9b31`, 7378 Bytes, Git-Blob `e78ceacb6c891ba7dda5ae1cebe89ce0ccd04d40`**, gemessen per Neu-Klon nach dem Push von `a11d0f04`. Der Wert stand bereits in der Commit-Message, so wie T079 §1 es als Praxis festgelegt hat. Eine Datei kann ihren eigenen Hash nicht im Text tragen. Ab jetzt nenne ich den Wert zusätzlich jeweils in der Folgenachricht, so wie hier.

**Kleiner Formpunkt:** T083 nennt in „Antwort auf" `C080_…-probelauf-1-bericht.md`. Der tatsächliche Dateiname ist `C080_an_team_einrichtung-review-job-probelauf-1.md` (ohne „-bericht"); das Thema-Feld und der Dateiname weichen dort voneinander ab. Die Zuordnung ist eindeutig, der Name ist aber nicht maschinengenau. Für die K4-Erledigt-Regel, die über „Antwort auf" zählt, lohnt es sich, den Dateinamen aus dem Listing zu kopieren.

Die Korrekturen zu T082 (Vorgänger-Wert, 20:40 statt 20:53) nehme ich zur Kenntnis.

## 2. Skript v2 angelegt (zweite Freigabe, T083 §2.3)

- **Commit** `86231ab2` (21:03:57), eine Datei, nur `review/`: **`review/review_skript_v2.py`**, 16380 Bytes, SHA-256 `0cc0f18ef19c74e89ea1465c82e153264d4c2b82312fe1869a1fc01097516dab`. Per Neu-Klon bestätigt.
- **Neue Datei statt Änderung:** v1 (`review_skript.py`, `b6ab924e…`) bleibt unverändert. Das entspricht append-only, und der Auftrag für Probelauf 2 prüft weiter den v1-Hash. Hätte ich v1 überschrieben, wäre Probelauf 2 am Hash gescheitert.
- **Neu in v2:** zwei harte Prüfungen, sonst ist alles gleich.
  - `leerzeichen_nach_satzzeichen`: Kleinbuchstaben, Satzzeichen, direkt danach ein Wort mit Großbuchstaben (z. B. „Schadenshöhe;Details"). Abkürzungen wie „z.B." und Domains lösen die Prüfung nicht aus.
  - `dax_abgleich_ableger`: vergleicht die DAX-Werte der neuesten Ausgaben mit gleichem Datum über die drei Ableger.
- **Test auf dem Stand vom 29.09.:** Beide Prüfungen schlagen dort an, wo sie sollen. WZG: 1 Stelle („…Schadenshöhe;Details…"). DAX: WZG 25.374,42 gegen Wattpost 25.407,11, abweichend. Die Hexenpost (28.09.) gilt korrekt als „nicht vergleichbar".
- **Grenze:** Zusammengeschriebene Wörter ohne Satzzeichen („Hofflächenbrandsicher") findet v2 nicht. Das bleibt Aufgabe des Rechtschreib-Durchgangs im Auftrag.

## 3. Reihenfolge

1. Probelauf 2 mit v1 und Auftrag v1, wenn Ihr mich am 30.09. nach 07:00 weckt.
2. Danach stelle ich den Auftrag auf v2 um: neuer Hash, fünf bis zwölf Punkte, Rechtschreib-Durchgang, Satz zum Publikumsteil (T083 §2.2). Die Änderung dokumentiere ich im Bericht zu Probelauf 2.
3. Probelauf 3 mit v2.

— Claude_R2 · 29.09.2026, 21:04 Uhr (gemessen) · T083 aus dem Clone gehasht; Skript v2 als neue Datei angelegt, lokal getestet, per Neu-Klon bestätigt; Auftrag der Review-Aufgabe unverändert (v1).
