Nummer: W002
Richtung: an_strato
Art: Lieferung
Thema: Übergabe Ist-Stand Website BFI_Website mit Hosting-Bezug (Auftrag #003)
Autor: Claude_Web
Datum/Uhrzeit: 14.10.2026, 23:40:55 MESZ (gemessen, Systemzeit beim Schreiben der Datei); Inhalt erstellt 14.10.2026, ca. 23:35 MESZ
Antwort auf: –
Bezug RUN-ID: – (Betreiber-Auftrag #003, RUN-ID nicht vergeben)

# Übergabe Claude_Web → Claude_Strato

Inhaltlich gleich mit `Uebergabe_Claude_Web_an_Claude_Strato.md`, die der Betreiber am 14.10.2026 als Datei erhalten hat. Der Stand bezieht sich auf das Repo BFi-AI-247/bfi_website, Branch `prototyp`, Commit `82f64f2`.

Statuswerte: **belegt** (mit Beleg) · **unbelegt** (nicht nachweisbar) · **offen** (noch nicht entschieden oder erledigt)

Ausschlüsse eingehalten: keine Zugangsdaten, Tokens, Passwörter oder API-Schlüssel; keine persönlichen Kontextdaten für den „digitalen Björn“; keine Inhalte zu dem ausgeschlossenen Projekt.

---

## 1. Stand Repo BFI_Website

| Punkt | Stand | Status |
|---|---|---|
| Repo | `github.com/BFi-AI-247/BFI_Website`, privat | belegt (`git remote`, Betreiber-Aussage) |
| Arbeits-Branch | `prototyp`, synchron mit `origin/prototyp` | belegt (`git status -sb`) |
| Letzter Commit `prototyp` | `82f64f2`, 2026-10-14 18:44:22 +0200, „Durchgängig Du-Form auf der Website und im digitalen Björn“ | belegt (`git log`, `git ls-remote`) |
| Branch `main` | nur der Initial-Commit `de95c1f` vom 2026-10-13 20:52:42 +0200; der Prototyp ist **nicht** gemergt | belegt (`git ls-remote`) |

Ordner- und Dateibaum (Stand `82f64f2`, ohne Inhalte):

```
BFI_Website/
├── .gitignore              schließt api/config.php, .env, *.key aus
├── README.md
├── OFFENE-PUNKTE.md        interne Liste, nicht für den Webserver
├── wissen/                 PRIVAT, nie in den Web-Ordner
│   └── digitaler-bjoern.md
└── public/                 Inhalt für den Web-Ordner (Document Root)
    ├── index.html
    ├── css/
    │   ├── tokens.css, base.css, layout.css
    │   ├── components/     chat, figures, fold, nav, portrait, tags, view (.css)
    │   └── views/          expertise, kontakt, projekte, publikationen, stationen, ueber-mich (.css)
    ├── data/
    │   └── de/             site, start, ueber-mich, projekte, stationen, expertise, publikationen, kontakt (.json)
    ├── img/
    │   ├── monogramm-dunkel.svg, monogramm-dunkel-vektor.svg
    │   ├── portraits/      15 Bilddateien
    │   ├── logos/          5 Bilddateien
    │   └── publikationen/  dissertation.jpg
    └── js/
        ├── app.js, chat.js, dom.js, portrait.js, views.js
```

- `api/` existiert lokal als leerer Ordner. Git versioniert keine leeren Ordner, deshalb ist er nicht im Repo. **belegt** (`ls api`)
- `public/data/en/` existiert noch nicht. **belegt**

## 2. Art der Website

| Punkt | Stand | Status |
|---|---|---|
| Typ | statisch: HTML, CSS, JavaScript (ES-Module), Inhalte als JSON | belegt (Dateibaum, `index.html`) |
| Build-Schritt | keiner; `public/` wird unverändert ausgeliefert | belegt (kein package.json, kein Build-Skript) |
| Routing | Hash-Routing im Browser (`#start`, `#projekte` …); der Server braucht keine Rewrite-Regeln | belegt (`js/app.js`) |
| Voraussetzung | Auslieferung über HTTP(S), weil die Seite die JSON-Dateien per `fetch` lädt; per `file://` funktioniert sie nicht | belegt (README, `app.js`) |
| Externe Ressource | Schriften werden von Google Fonts geladen (Bodoni Moda, IBM Plex Sans und Mono) | belegt (`index.html`, Zeilen 9–11) |

## 3. Server-seitige Anforderungen

| Punkt | Stand | Status |
|---|---|---|
| PHP | nötig für einen Endpunkt, den KI-Chat-Proxy | belegt als Planung (README, `chat.js` Kommentar); Version **offen** |
| Endpunkt `api/chat.php` | Zweck: nimmt Chat-Fragen an, ruft serverseitig Mistral bzw. Claude auf und hält die API-Schlüssel; der Browser sieht nie einen Schlüssel | belegt als Planung; **noch nicht gebaut** |
| Schnittstelle (vom Frontend erwartet) | `POST api/chat.php`, JSON `{modell, frage, sprache}` mit `modell` = `mistral` oder `claude`; Antwort JSON `{antwort}`; bei Fehler zeigt das Frontend „Noch nicht verbunden“ | belegt (`js/chat.js`, Zeilen 7 und 52–57) |
| Pfad | Das Frontend ruft den Endpunkt **relativ** auf (`api/chat.php`). Er muss also unter `<Document Root>/api/chat.php` erreichbar sein, d. h. im Web-Ordner neben `index.html` | belegt (`chat.js`) |
| Konfiguration | Schlüssel in `api/config.php` oder `.env`, beide per `.gitignore` vom Repo ausgeschlossen; Ablage auf dem Server **offen** (Vorschlag: außerhalb des Document Root, per `require` eingebunden) | belegt (`.gitignore`); Ablageort offen |
| Wissensdatei | `wissen/digitaler-bjoern.md` muss auf den Server, damit `chat.php` sie lesen kann, aber **außerhalb** des Document Root | belegt (Betreiber-Vorgabe, README) |
| Ausgehende HTTPS-Aufrufe | PHP muss `api.mistral.ai` und `api.anthropic.com` erreichen (cURL oder `allow_url_fopen`) | **offen**, Prüfskript geplant |
| Datenbank | keine vorgesehen | belegt (kein DB-Bezug im Code) |
| Umgebungsvariablen | nur die zwei API-Schlüssel (Mistral, Anthropic); Namen noch nicht festgelegt | offen |
| Weitere Funktionen | Abstimmung „Diese Antwort ist besser“ im Modus „Beide“ ist nur im Frontend umgesetzt und speichert nichts auf dem Server | belegt (`chat.js`); serverseitige Auswertung offen |

## 4. Domain, Subdomains und Sprachen

| Punkt | Stand | Status |
|---|---|---|
| Domain | Favorit **digifil.de**; als Strato-Paket gebucht, Bereitstellung lief am 13.10.2026 noch | belegt (Betreiber-Aussage 13.10.2026); Freischaltung **offen** |
| Familien-Domain | generisch ohne Vornamen, damit die Söhne sie mitnutzen können; Subdomains je Person oder Angebot | belegt als Wunsch (Betreiber-Aussage); konkrete Struktur **offen** |
| filbrich.de/.com/.eu | vergeben, nicht verfügbar | belegt (Betreiber-Aussage) |
| Sprachen | Deutsch und Englisch | belegt als Entscheidung; EN **offen** (nicht umgesetzt) |
| Umsetzung der Sprachen | im Code vorbereitet als `data/de/` und `data/en/` mit Umschalter DE/EN, gleiche URL | belegt (`app.js`, README) |
| **Vorschlag** | Website auf `digifil.de` bzw. einer Personen-Subdomain (z. B. `bjoern.digifil.de`), Sprache ohne eigene Subdomain über den Umschalter | Vorschlag, nicht entschieden |

## 5. Bereitstellungsweg

| Punkt | Stand | Status |
|---|---|---|
| Zielbild | automatisches Hochladen GitHub → Strato per SFTP | **offen** (in OFFENE-PUNKTE.md als Aufgabe, nicht beschlossen) |
| Was hochgeladen wird | Inhalt von `public/` in den Document Root; zusätzlich `api/` (sobald gebaut) in den Document Root; `wissen/` und die Schlüsseldatei außerhalb | belegt als Planung (README, `.gitignore`) |
| Was nie hochgeladen wird (Web-Ordner) | `wissen/`, `OFFENE-PUNKTE.md`, `README.md`, `.git/` | belegt (README) |
| Quell-Branch für den Deploy | offen; heute liegt der Stand nur auf `prototyp` | offen |
| **Vorschlag** | GitHub Action bei Push auf `main`: SFTP-Sync von `public/` und `api/`, Zugangsdaten als GitHub Secrets; erster Upload manuell zum Testen | Vorschlag, nicht entschieden |

## 6. Betreiber-Entscheidungen bisher

Die Entscheidungen fielen im Chatverlauf vom 13. und 14.10.2026. Genaue Zeitpunkte sind in dieser Sitzung nicht mehr nachweisbar. Datum je Punkt deshalb **unbelegt**, sofern nicht anders angegeben.

1. Neues **privates** Repo BFI_Website statt des alten öffentlichen (Okt 2026). belegt (Betreiber-Aussage, Initial-Commit 13.10.2026)
2. Hosting bei **Strato**, Domain-Favorit **digifil.de**. belegt (Betreiber-Aussage; Bereitstellung lief am 13.10.2026)
3. API-Schlüssel **nie** auf GitHub und nie im Browser; Proxy auf dem Server. belegt (Betreiber-Aussage, `.gitignore`)
4. KI-Chat „digitaler Björn“; Besucher wählt **Mistral, Claude oder beide**. belegt (Betreiber-Aussage, `start.json`)
5. Persönliche Daten nur für die KI, **nicht** öffentlich auf der Website. belegt (Betreiber-Aussage)
6. Website **zweisprachig** DE/EN. belegt (Betreiber-Aussage)
7. Klickbasierte Navigation statt langer Seite, modulares CSS. belegt (Betreiber-Aussage, Umsetzung im Repo)
8. **Keine Telefonnummer** auf der Website. belegt (Betreiber-Aussage, `kontakt.json`)
9. Startseite als Chat-Hero („Frag den digitalen Björn.“). belegt (Commit `9af3388`, 14.10.2026)
10. Durchgängig **Du-Form**. belegt (Commit `82f64f2`, 14.10.2026)
11. Interim-Management-Angebot evtl. später als eigenes Modul. belegt (Betreiber-Aussage)

## 7. Offene Punkte und Risiken mit Hosting-Bezug

**Offen**

- Freischaltung Strato-Paket und Domain digifil.de
- Prüfskript: Erreicht PHP auf Strato die APIs von Mistral und Anthropic per HTTPS? Welche PHP-Version läuft?
- API-Zugänge bei Mistral (La Plateforme) und Anthropic (Claude Console) anlegen
- `api/chat.php` bauen
- Ablageort der Schlüsseldatei und der Wissensdatei außerhalb des Document Root festlegen; prüfen, ob das Strato-Paket einen Ordner oberhalb des Web-Ordners bietet
- Bereitstellungsweg festlegen (siehe 5); Branch `prototyp` nach `main` übernehmen
- Impressum und Datenschutzerklärung (Pflicht, sobald online, erst recht mit KI-Chat); die Links im Footer existieren, die Seiten noch nicht
- E-Mail-Adresse auf die neue Domain umstellen (heute steht eine GMX-Adresse auf der Kontaktseite)
- Englische Fassung `data/en/`

**Risiken**

- **Google Fonts extern:** Laden von Google-Servern überträgt Besucher-IPs in die USA; in Deutschland abmahnrelevant. Empfehlung: Schriften selbst hosten.
- **Wissensdatei im Web-Ordner:** Liegt `wissen/` versehentlich im Document Root, ist sie öffentlich abrufbar. Der Deploy darf nur `public/` und `api/` in den Web-Ordner schreiben.
- **Kosten und Missbrauch des Chat-Endpunkts:** `chat.php` ist öffentlich aufrufbar; ohne Begrenzung (Rate-Limit, Längenlimit, Herkunftsprüfung) können Fremde API-Kosten erzeugen.
- **Datenschutz Chat:** Fragen gehen an Mistral (EU) und Anthropic (USA); das muss in die Datenschutzerklärung und in den Hinweis am Chat.
- **Ausgehende Verbindungen:** Falls Strato Basic ausgehende HTTPS-Aufrufe aus PHP sperrt oder begrenzt, funktioniert der Chat dort nicht.
- **Pfad des Endpunkts:** Das Frontend erwartet `api/chat.php` relativ zur Seite; liegt `api/` woanders, schlägt jede Anfrage fehl.
- **Leerer Ordner `api/`:** ist nicht im Repo; ein Deploy-Skript, das ihn voraussetzt, muss ihn anlegen.
- **README veraltet:** nennt noch `international.json`, das inzwischen in `expertise.json` aufgegangen ist. Für das Hosting unkritisch.

## 8. Abweichungs-Hinweise (a)–(d) aus der Erst-Quittierung

**unbelegt.** Eine Erst-Quittierung von Claude_Web mit Abweichungs-Hinweisen (a)–(d) liegt in dieser Sitzung nicht vor. Weder im Verlauf noch im Repo findet sich eine Spur davon. Den Stand kann ich erst angeben, wenn der Betreiber den Wortlaut der Hinweise nachreicht.

---

## Ausführungsstand

- teilweise: Punkt 8 unbelegt, Entscheidungsdaten in Punkt 6 teils unbelegt
- offen: siehe Punkte 3, 4, 5 und 7

— Claude_Web · 14.10.2026, 23:40:55 MESZ (gemessen) · W002 · Übergabe Ist-Stand geliefert, Ausführung teilweise
