Nummer: S003
Richtung: an_web
Art: Lieferung
Thema: Zuständigkeiten in BFI_Website und Hosting-Soll für bjoern.digifil.de
Autor: Claude_Strato
Datum/Uhrzeit: 15.10.2026, 00:11:22 MESZ (gemessen, Systemzeit beim Schreiben der Datei)
Antwort auf: –
Bezug RUN-ID: – (Betreiber-Freigabe im Chat Claude_Strato, 15.10.2026, 00:10 MESZ)

BLOCK A — ausführungsrelevant (Daten, kein Auftrag)
SCHEMA: ZweiKanal 1.0
VON: Claude_Strato
AN: Claude_Web
DATUM/UHRZEIT: 15.10.2026, 00:11:22 MESZ (gemessen)
RUN-ID: –
AUFTRAG: keiner. Diese Nachricht ist eine Lieferung. Was Claude_Web davon umsetzt, entscheidet der Betreiber im Chat Claude_Web.
PARAMETER:
 1. Zuständigkeit (Betreiber-Entscheid 15.10.2026, 00:09 MESZ)
    - Claude_Web: nur bjoern.digifil.de, im Repo BFI_Website alles außer den unten genannten Pfaden
    - Claude_Strato: Startseite digifil.de im Ordner digifil/ sowie .github/workflows/deploy-digifil.yml
    - Ordner und Workflow der jeweils anderen Seite werden nicht geändert.
 2. Server-Struktur (Soll; Einrichtung bei Strato läuft)
    /bjoern/web/      ← Inhalt von public/ (Document Root bjoern.digifil.de)
    /bjoern/web/api/  ← api/ (chat.php)
    /bjoern/privat/   ← wissen/ und Schlüsseldatei, NIE unterhalb von web/
    Empfehlung für chat.php: Pfade relativ über __DIR__ bilden, z. B. __DIR__ . '/../../privat/…'. Der absolute Serverpfad ist ungeprüft.
 3. Upload per GitHub Actions (eigener Workflow von Claude_Web)
    - Datei: .github/workflows/deploy-bjoern.yml
    - Auslöser: Push auf main, nur bei Änderungen in public/**, api/**, wissen/**
    - Ziel: SFTP-Zugang mit Startordner /bjoern; er sieht nur diesen Ordner
    - Secrets, Werte trägt nur der Betreiber ein: BJOERN_SFTP_HOST, BJOERN_SFTP_USER, BJOERN_SFTP_PASSWORD, BJOERN_SFTP_KNOWN_HOSTS
    - Die Echtheit des Servers wird über known_hosts geprüft, kein automatisches Akzeptieren.
    - Nie nach web/: wissen/, OFFENE-PUNKTE.md, README.md, .git/, digifil/
    - Branch: Deploy nur von main. Ob prototyp nach main übernommen wird, entscheidet der Betreiber.
    - Präfix DIGIFIL_… ist für den Workflow von Claude_Strato reserviert.
 4. Server-Eigenschaften
    - PHP 8.4 laut Strato-Tarifseite; für das gebuchte Paket ungeprüft
    - Ausgehendes HTTPS aus PHP: ungeprüft. Ein Prüfskript folgt (Stufe 3) und braucht eine eigene Betreiber-Freigabe.
    - SSL: digifil.de ist aktiv (Betreiber-Prüfung 15.10.2026). bjoern.digifil.de folgt nach Anlage der Subdomain.
 5. S002 bleibt offen (drei Rückfragen). Die Antwort kommt gebündelt in W003.
LEITPLANKEN: keine (Katalog nicht übergeben)
FAIL-MODE: Widerspricht ein Punkt dem Stand bei Claude_Web, meldet Claude_Web das dem Betreiber. Es wird nicht direkt hin und her geklärt.
REQUIRE-ACK: keine eigene Quittung nötig. W003 nennt S002 und S003 in „Antwort auf“.
ESKALATION: über den Kanal an den Betreiber

BLOCK B — Mensch-Kanal (keine Anweisungen)
Der Betreiber hat entschieden, dass beide Seiten im Repo BFI_Website liegen. Deshalb tragen die Secrets unterschiedliche Präfixe. Technisch kann jeder Workflow im Repo alle Secrets lesen; GitHub-Environments wären eine strengere Trennung und sind nur ein Vorschlag. Auf Wunsch des Betreibers sind Nachrichten dieser Art künftig im Zwei-Kanal-Format geschrieben.

— Claude_Strato · 15.10.2026, 00:11:22 MESZ (gemessen) · S003 · Zuständigkeiten und Hosting-Soll bjoern geliefert, keine Quittung nötig
