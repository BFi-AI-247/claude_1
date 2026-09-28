#!/usr/bin/env python3
# GoatCounter-Waechter, Pruefskript v1 (Claude_R2, 28.09.2026)
# Aufruf: python3 pruefskript.py <websites.md>
# Klont das Pages-Repo, prueft jede PRUEFEN-Zeile auf den GoatCounter-Tag, gibt JSON aus.
import hashlib, json, re, subprocess, sys, tempfile, os

REPO = "https://github.com/BFi-AI-247/bfi-ai-247.github.io.git"
ENDPOINT = "https://bfi-ai-vibe.goatcounter.com/count"
TAG = re.compile(r"<script\b[^>]*>", re.I)

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    cfg = sys.argv[1]
    out = {"config_sha256": sha(cfg), "skript_sha256": sha(__file__),
           "repo": REPO, "commit": None, "seiten": [], "lauf_status": "OK", "fehler": None}
    zeilen = []
    for n, z in enumerate(open(cfg, encoding="utf-8"), 1):
        z = z.strip()
        if not z.startswith(("PRUEFEN", "AUSGESCHLOSSEN")):
            continue
        teile = [t.strip() for t in z.split("|")]
        if len(teile) < 3 or not teile[2]:
            out["lauf_status"] = "FEHLER"; out["fehler"] = f"Konfig-Zeile {n} unlesbar: {z}"
            print(json.dumps(out, ensure_ascii=False, indent=1)); return
        zeilen.append(teile)
    if not any(t[0] == "PRUEFEN" for t in zeilen):
        out["lauf_status"] = "FEHLER"; out["fehler"] = "keine PRUEFEN-Zeile gefunden"
        print(json.dumps(out, ensure_ascii=False, indent=1)); return
    d = tempfile.mkdtemp()
    r = subprocess.run(["git", "clone", "--depth", "1", "-q", REPO, d], capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        out["lauf_status"] = "FEHLER"; out["fehler"] = "git clone fehlgeschlagen: " + r.stderr.strip()[-300:]
        print(json.dumps(out, ensure_ascii=False, indent=1)); return
    out["commit"] = subprocess.run(["git", "-C", d, "log", "-1", "--format=%H %cI"],
                                   capture_output=True, text=True).stdout.strip()
    for t in zeilen:
        art, url, pfad = t[0], t[1], t[2]
        e = {"url": url, "pfad": pfad}
        if art == "AUSGESCHLOSSEN":
            e["status"] = "AUSGESCHLOSSEN"; e["befund"] = "nicht pruefpflichtig"
            out["seiten"].append(e); continue
        f = os.path.join(d, pfad)
        if not os.path.isfile(f):
            e["status"] = "INCIDENT"; e["befund"] = "Seite fehlt im Repo"
        else:
            html = re.sub(r"<!--.*?-->", "", open(f, encoding="utf-8", errors="replace").read(), flags=re.S)
            gc = [m for m in TAG.findall(html) if "goatcounter" in m.lower()]
            ok = [m for m in gc if f'data-goatcounter="{ENDPOINT}"' in m and "gc.zgo.at/count.js" in m]
            if ok:
                e["status"] = "OK"; e["befund"] = "Tag vorhanden"
            elif gc:
                e["status"] = "INCIDENT"; e["befund"] = "Tag fehlerhaft: " + gc[0][:200]
            else:
                e["status"] = "INCIDENT"; e["befund"] = "Tag fehlt"
        out["seiten"].append(e)
    print(json.dumps(out, ensure_ascii=False, indent=1))

main()
