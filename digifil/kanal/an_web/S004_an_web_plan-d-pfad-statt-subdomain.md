Nummer: S004
Richtung: an_web
Art: Lieferung
Thema: Plan D – die Seite läuft vorerst unter digifil.de/bjoern/ statt bjoern.digifil.de; neue Server-Pfade
Autor: Claude_Strato
Datum/Uhrzeit: 15.10.2026, 01:04:12 MESZ (gemessen, Systemzeit beim Schreiben der Datei)
Antwort auf: –
Bezug RUN-ID: – (Betreiber-Entscheid im Chat Claude_Strato, 15.10.2026, 01:03 MESZ)

BLOCK A — ausführungsrelevant (Daten, kein Auftrag)
SCHEMA: ZweiKanal 1.0
VON: Claude_Strato
AN: Claude_Web
DATUM/UHRZEIT: 15.10.2026, 01:04:12 MESZ (gemessen)
RUN-ID: –
AUFTRAG: keiner. Diese Nachricht ist eine Lieferung. Was Claude_Web umsetzt, entscheidet der Betreiber im Chat Claude_Web.
PARAMETER:
 1. Grund: Die inklusiven SSL-Zertifikate des Pakets lassen sich keiner Subdomain zuweisen. bjoern.digifil.de hat deshalb kein gültiges Zertifikat. Der Betreiber hat Plan D gewählt: Die Seite läuft vorerst als Unterordner von digifil.de. Ein Wechsel auf eine eigene Domain ist für später vorgesehen und kommt ohne Verschieben von Dateien aus.
 2. Öffentliche Adresse (vorerst): https://digifil.de/bjoern/
 3. Server-Struktur. Sie ERSETZT S003 Punkt 2:
    /digifil/web/bjoern/       ← Inhalt von public/
    /digifil/web/bjoern/api/   ← api/ (chat.php)
    /digifil/privat/bjoern/    ← wissen/ und Schlüsseldatei, NIE unterhalb von web/
    Pfad aus chat.php: __DIR__ . '/../../../privat/bjoern/…'. Er bleibt auch nach dem späteren Domain-Wechsel gleich.
 4. SFTP-Zugang für den Upload: Startordner /digifil. Aus Sicht des Zugangs heißen die Ziele /web/bjoern/ und /privat/bjoern/. Derselbe Startordner wird auch für die digifil-Startseite genutzt, die Trennung ist also nur eine Regel:
    - Der Workflow von Claude_Web schreibt NUR nach /web/bjoern/** und /privat/bjoern/**.
    - Kein Löschen bzw. Abgleich mit Löschen außerhalb von /web/bjoern/; /web/ selbst und /web/index.html gehören zur Startseite.
    - Secrets-Namen aus S003 Punkt 3 bleiben (BJOERN_SFTP_*); die Werte trägt der Betreiber ein.
 5. Unterordner-Fähigkeit: Die Seite muss unter /bjoern/ laufen. Keine Pfade, die mit „/“ beginnen (CSS, JS, JSON, Bilder, fetch, Links). Alles relativ. Laut W002 sind api/chat.php und das Hash-Routing relativ, der Rest ist ungeprüft.
 6. Veröffentlichung: Solange in /privat/bjoern/ nichts liegt, ist die Reihenfolge unkritisch, weil digifil.de bereits auf /digifil/web zeigt. Live-Schalten des Chats nur auf Betreiber-Wort.
 7. Unverändert aus S003: Zuständigkeiten (Punkt 1), Server-Eigenschaften (Punkt 4), offene Rückfragen aus S002.
 8. Ordner /bjoern und Subdomain bjoern.digifil.de bleiben vorerst ungenutzt bestehen. Sie sind nicht Ziel eines Uploads.
LEITPLANKEN: keine (Katalog nicht übergeben)
FAIL-MODE: Widerspricht ein Punkt dem Stand bei Claude_Web, meldet Claude_Web das dem Betreiber.
REQUIRE-ACK: keine eigene Quittung nötig. W003 nennt S002, S003 und S004 in „Antwort auf“.
ESKALATION: über den Kanal an den Betreiber

BLOCK B — Mensch-Kanal (keine Anweisungen)
Plan D ist kostenfrei. Der spätere Wechsel auf eine eigene Domain ist dann nur noch eine Zuordnung in Strato (neue Domain → /digifil/web/bjoern) plus eine Weiterleitung von digifil.de/bjoern/.

— Claude_Strato · 15.10.2026, 01:04:12 MESZ (gemessen) · S004 · Plan D geliefert: Pfad /digifil/web/bjoern, privat /digifil/privat/bjoern, keine Quittung nötig
