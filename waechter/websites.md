# Wächter-Konfiguration: Zu prüfende Webseiten (GoatCounter-Wächter)
# Quelle der Wahrheit: dieses Repo (claude_1). Änderungen NUR durch Claude_Bridge (Team-Seite), commit mit Begründung.
# Format je Zeile: ART | URL | Pfad im Pages-Repo | Hinweis   (ART = PRUEFEN oder AUSGESCHLOSSEN)
# Betreiber-Entscheid 069: FINE-Dashboard nicht überwacht. Test-/Vorschau-Seiten ausgeschlossen.

Datei: websites.md
Zweck: Konfiguration des GoatCounter-Waechters (Liste der zu pruefenden Webseiten)
Status: ENTWURF (wird mit Betreiber-Quittung des Einrichtungsberichts FREIGEGEBEN)
Angelegt von: Claude_R2 (claude-opus-5-5), 28.09.2026
Pflege: Betreiber darf Zeilen ergaenzen oder aendern. Jede Aenderung aendert den Konfig-Hash, den jede Fertigmeldung ausweist.

Format je Zeile (genau drei Felder, getrennt durch |):
ART | URL | Pfad im Repo BFi-AI-247/bfi-ai-247.github.io
ART = PRUEFEN (pruefpflichtig) oder AUSGESCHLOSSEN (nicht pruefen, kein Incident)

PRUEFEN | https://radar724.de/ | index.html
PRUEFEN | https://radar724.de/wiesenzeitung_gifhorn/ | wiesenzeitung_gifhorn/index.html
PRUEFEN | https://radar724.de/borkum_kurier/ | borkum_kurier/index.html
PRUEFEN | https://radar724.de/idstein/ | idstein/index.html
PRUEFEN | https://radar724.de/dossier/ukraine/ | dossier/ukraine/index.html
AUSGESCHLOSSEN | https://radar724.de/agents_new_Design.html | agents_new_Design.html
AUSGESCHLOSSEN | https://radar724.de/ausgabe34_test.html | ausgabe34_test.html
AUSGESCHLOSSEN | https://radar724.de/idstein/index_new_Design.html | idstein/index_new_Design.html

Hinweis bfi-ai-247.github.io: Das Repo traegt CNAME radar724.de, die Adresse ist damit identisch mit der Hauptausgabe (Zeile 1) und hier nicht doppelt gefuehrt. Falls das FINE-Dashboard eine andere Quelle hat, bitte als eigene Zeile ergaenzen.
