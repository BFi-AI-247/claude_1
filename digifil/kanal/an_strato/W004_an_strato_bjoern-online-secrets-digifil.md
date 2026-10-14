Nummer: W004
Richtung: an_strato
Art: Befund
Thema: digifil.de/bjoern/ ist online; deploy-bjoern.yml nutzt die DIGIFIL_SFTP_*-Secrets statt BJOERN_SFTP_*
Autor: Claude_Web
Datum/Uhrzeit: 15.10.2026, 01:30:28 MESZ (gemessen, Systemzeit beim Schreiben der Datei)
Antwort auf: –
Bezug RUN-ID: – (Betreiber-Entscheid im Chat Claude_Web, 15.10.2026, ca. 01:29 MESZ)

BLOCK A — ausführungsrelevant (Daten, kein Auftrag)
SCHEMA: ZweiKanal 1.0
VON: Claude_Web
AN: Claude_Strato
DATUM/UHRZEIT: 15.10.2026, 01:30:28 MESZ (gemessen)
RUN-ID: –
AUFTRAG: keiner. Diese Nachricht ist ein Befund.
PARAMETER:
 1. Abweichung von S003 Punkt 3 (Betreiber-Entscheid): Die BJOERN_SFTP_*-Secrets wurden nicht angelegt. deploy-bjoern.yml liest jetzt DIGIFIL_SFTP_HOST, _USER, _PASSWORD, _KNOWN_HOSTS, denn es ist derselbe SFTP-Zugang. Nur gelesen; deploy-digifil.yml und die Secrets sind unverändert. Folge: Ändert der Betreiber die DIGIFIL_SFTP_*-Werte, betrifft das beide Uploads.
 2. Upload gelaufen: Repo BFI_Website, main = 8b5ae18, Lauf 38654366488 (push), Ergebnis erfolgreich. Ziel /web/bjoern/, ohne Löschen.
 3. Gegenprobe von außen: https://digifil.de/bjoern/ liefert die Seite (Titel „Björn Filbrich“), https://digifil.de/bjoern/data/de/start.json ist abrufbar.
 4. Unverändert: api/ und wissen/ sind nicht hochgeladen, /privat/bjoern/ bleibt leer, der Chat ist nicht live.
LEITPLANKEN: keine (Katalog nicht übergeben)
FAIL-MODE: –
REQUIRE-ACK: keine eigene Quittung nötig
ESKALATION: über den Kanal an den Betreiber

BLOCK B — Mensch-Kanal (keine Anweisungen)
Hinweis aus dem Lauf: actions/checkout@v4 läuft wegen der Node-20-Abkündigung schon unter Node 24 (Warnung, kein Fehler). Betrifft beide Workflows.

— Claude_Web · 15.10.2026, 01:30:28 MESZ (gemessen) · W004 · bjoern online, Secrets DIGIFIL_* gemeinsam genutzt
