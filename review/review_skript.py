#!/usr/bin/env python3
# Review-Prüfskript v1 (Claude_R2, 29.09.2026) — Konzept C079, Freigabe T082
# Aufruf:
#   python3 review_skript.py vorbereiten <arbeitsordner> <claude_1-clone>
#   python3 review_skript.py abschliessen <arbeitsordner> <claude_1-clone>
# vorbereiten: klont das Pages-Repo, findet je Ableger die neueste Morgenausgabe,
#   extrahiert Text (Zeilen Z001 …) und rechnet harte Prüfungen. Schreibt kontext.json.
# abschliessen: liest entwurf_<ableger>.json (vom Modell), prüft Publikumstext und jedes
#   Zitat gegen die Ausgabe, schreibt review/<ableger>/<datum>.publikum.json,
#   review/<ableger>/<datum>.werkstatt.md und review/laeufe/<lauf_id>.md in den Clone.
# Das Skript schreibt nur unter <claude_1-clone>/review/. Es committet und pusht nicht.
import datetime, hashlib, html, json, os, re, subprocess, sys
from html.parser import HTMLParser
from zoneinfo import ZoneInfo

PAGES = "https://github.com/BFi-AI-247/bfi-ai-247.github.io.git"
ABLEGER = {  # Kennung -> (Ordner im Pages-Repo, Name)
    "wzg": ("wiesenzeitung_gifhorn", "Wiesenzeitung Gifhorn"),
    "wattpost": ("borkum_kurier", "Wattpost Borkum"),
    "hexenpost": ("idstein", "Idsteiner Hexenpost"),
}
MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August",
          "September", "Oktober", "November", "Dezember"]
PUB_MIN, PUB_MAX = 80, 600
ZITAT_MIN, ZITAT_MAX = 12, 220
MAX_PUNKTE, MAX_VORSCHLAEGE, VORSCHLAG_MAX = 12, 3, 300
DIMENSIONEN = ("inhalt", "design", "konsistenz")
GEWICHTE = ("hoch", "mittel", "niedrig")


def jetzt():
    return datetime.datetime.now(ZoneInfo("Europe/Berlin"))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def norm(s):
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


class Text(HTMLParser):
    """Sichtbarer Text als Zeilen mit Tag-Marke; script/style/svg werden übersprungen."""
    BLOCK = {"h1", "h2", "h3", "h4", "p", "li", "td", "th", "summary", "figcaption", "blockquote",
             "div", "section", "article", "header", "footer", "nav", "main", "aside", "ul", "ol", "table", "tr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.zeilen, self.puffer, self.tag, self.skip = [], [], None, 0

    def flush(self):
        t = re.sub(r"\s+", " ", "".join(self.puffer)).strip()
        if t:
            self.zeilen.append((self.tag or "text", t))
        self.puffer = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "svg"):
            self.skip += 1
        elif tag in self.BLOCK:
            self.flush()
            self.tag = tag
        elif tag == "br":
            self.puffer.append(" ")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg"):
            self.skip = max(0, self.skip - 1)
        elif tag in self.BLOCK:
            self.flush()
            self.tag = None

    def handle_data(self, d):
        if not self.skip:
            self.puffer.append(d)


def harte_pruefungen(roh, pfad, repo, datum):
    p = []
    titel = norm(re.search(r"<title>(.*?)</title>", roh, re.S | re.I).group(1)) if re.search(r"<title>", roh, re.I) else ""
    d = datetime.date.fromisoformat(datum)
    lang = f"{d.day}. {MONATE[d.month - 1]} {d.year}"
    kurz = d.strftime("%d.%m.%Y")
    sichtbar = norm(re.sub(r"<(script|style)\b.*?</\1>", " ", re.sub(r"<[^>]+>", " ", roh), flags=re.S))
    p.append({"pruefung": "datum_im_titel", "ok": lang in titel or kurz in titel,
              "detail": f"Titel: {titel[:160]} | erwartet: {lang}"})
    p.append({"pruefung": "datum_im_seitentext", "ok": lang in sichtbar or kurz in sichtbar,
              "detail": f"erwartet: {lang} oder {kurz}"})
    nr = re.findall(r"Ausgabe\s*#\s*(\d+)", titel)
    p.append({"pruefung": "ausgabe_nummer_im_titel", "ok": bool(nr), "detail": f"gefunden: {nr}"})
    gc = [t for t in re.findall(r"<script\b[^>]*>", re.sub(r"<!--.*?-->", "", roh, flags=re.S), re.I) if "goatcounter" in t.lower()]
    p.append({"pruefung": "goatcounter_tag", "ok": bool(gc), "detail": "vorhanden" if gc else "fehlt"})
    basis = os.path.dirname(os.path.join(repo, pfad))
    kaputt = []
    for ziel in re.findall(r'(?:href|src)="([^"]+)"', roh):
        if re.match(r"^(https?:|//|mailto:|#|data:|javascript:)", ziel):
            continue
        z = ziel.split("#")[0].split("?")[0]
        if z and not os.path.exists(os.path.normpath(os.path.join(basis, html.unescape(z)))):
            kaputt.append(ziel)
    p.append({"pruefung": "interne_links_aufloesbar", "ok": not kaputt, "detail": f"nicht auflösbar: {kaputt[:10]}"})
    ohne_alt = len([i for i in re.findall(r"<img\b[^>]*>", roh, re.I) if not re.search(r"\balt=", i, re.I)])
    p.append({"pruefung": "bilder_mit_alt", "ok": ohne_alt == 0, "detail": f"Bilder ohne alt: {ohne_alt}"})
    artikel = re.findall(r"<article\b.*?</article>", roh, re.S | re.I)
    ohne_q = [norm(re.sub(r"<[^>]+>", " ", a))[:80] for a in artikel
              if not re.search(r"Quelle|Grundlage", html.unescape(a), re.I)]
    p.append({"pruefung": "artikel_mit_quellenangabe", "ok": not ohne_q,
              "detail": f"{len(artikel)} Artikel, ohne Quelle: {len(ohne_q)} {ohne_q[:5]}"})
    h1 = len(re.findall(r"<h1\b", roh, re.I))
    p.append({"pruefung": "genau_eine_h1", "ok": h1 == 1, "detail": f"h1-Anzahl: {h1}"})
    return p


def vorbereiten(arbeit, c1):
    os.makedirs(arbeit, exist_ok=True)
    pages = os.path.join(arbeit, "pages")
    out = {"skript_sha256": sha(open(__file__, "rb").read()), "lauf_status": "OK", "fehler": None}
    t = jetzt()
    out["zeit"] = {"wert": t.isoformat(timespec="seconds"), "quelle": "Systemzeit der Laufumgebung, Python zoneinfo Europe/Berlin"}
    out["heute"] = t.date().isoformat()
    out["lauf_id"] = "R" + t.strftime("%Y%m%d-%H%M")
    laeufe = os.path.join(c1, "review", "laeufe")
    n = len([f for f in os.listdir(laeufe) if f.endswith(".md")]) if os.path.isdir(laeufe) else 0
    out["kennung"] = f"Claude_Haiku_Reviewer_R{n + 1}"
    if not os.path.isdir(os.path.join(pages, ".git")):
        r = subprocess.run(["git", "clone", "--depth", "1", "-q", PAGES, pages], capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            out["lauf_status"] = "FEHLER"
            out["fehler"] = "git clone Pages-Repo fehlgeschlagen: " + r.stderr.strip()[-300:]
            json.dump(out, open(os.path.join(arbeit, "kontext.json"), "w"), ensure_ascii=False, indent=1)
            print(json.dumps({k: out[k] for k in ("lauf_status", "fehler")}, ensure_ascii=False)); return
    out["pages_commit"] = subprocess.run(["git", "-C", pages, "log", "-1", "--format=%H %cI"], capture_output=True, text=True).stdout.strip()
    out["ableger"] = {}
    for key, (ordner, name) in ABLEGER.items():
        e = {"name": name}
        try:
            posts = os.path.join(pages, ordner, "posts")
            dateien = sorted(f for f in os.listdir(posts) if re.match(r"^\d{4}-\d{2}-\d{2}-morgens\.html$", f))
            if not dateien:
                raise RuntimeError("keine Morgenausgabe gefunden")
            f = dateien[-1]
            datum = f[:10]
            pfad = f"{ordner}/posts/{f}"
            roh_b = open(os.path.join(pages, pfad), "rb").read()
            roh = roh_b.decode("utf-8", errors="replace")
            e.update({"datei": pfad, "datum": datum, "sha256": sha(roh_b), "bytes": len(roh_b)})
            if os.path.exists(os.path.join(c1, "review", key, f"{datum}.publikum.json")):
                e["status"] = "BEREITS_VORHANDEN"
            elif datum != out["heute"]:
                e["status"] = "KEINE_NEUE_AUSGABE"
            else:
                e["status"] = "ZU_PRUEFEN"
            tp = Text(); tp.feed(roh); tp.flush()
            e["zeilen"] = [f"Z{i:03d} [{tag}] {txt}" for i, (tag, txt) in enumerate(tp.zeilen, 1)]
            e["harte_pruefungen"] = harte_pruefungen(roh, pfad, pages, datum)
        except Exception as ex:
            e["status"] = "FEHLER"
            e["fehler"] = f"{type(ex).__name__}: {ex}"
        out["ableger"][key] = e
    json.dump(out, open(os.path.join(arbeit, "kontext.json"), "w"), ensure_ascii=False, indent=1)
    kurz = {k: {"status": v["status"], "datum": v.get("datum"), "zeilen": len(v.get("zeilen", [])),
                "harte_pruefungen_nicht_ok": [p["pruefung"] for p in v.get("harte_pruefungen", []) if not p["ok"]],
                "fehler": v.get("fehler")} for k, v in out["ableger"].items()}
    print(json.dumps({"lauf_id": out["lauf_id"], "kennung": out["kennung"], "heute": out["heute"],
                      "pages_commit": out["pages_commit"], "ableger": kurz}, ensure_ascii=False, indent=1))


def publikum_ok(t):
    if not isinstance(t, str):
        return "kein Text"
    if not (PUB_MIN <= len(t) <= PUB_MAX):
        return f"Länge {len(t)} außerhalb {PUB_MIN}–{PUB_MAX}"
    if re.search(r"[<>\[\]`*#|\\]", t):
        return "unerlaubte Zeichen (<>[]`*#|\\)"
    if re.search(r"https?:|www\.|\.de\b|\.com\b", t, re.I):
        return "URL oder Domain im Text"
    if re.search(r"[\x00-\x08\x0b-\x1f\x7f]", t):
        return "Steuerzeichen"
    return None


def abschliessen(arbeit, c1):
    k = json.load(open(os.path.join(arbeit, "kontext.json"), encoding="utf-8"))
    ergebnis = {}
    zeilen_md = []
    for key, e in k.get("ableger", {}).items():
        st = e["status"]
        if st != "ZU_PRUEFEN":
            ergebnis[key] = {"status": st, "detail": e.get("fehler") or e.get("datum")}
            continue
        ep = os.path.join(arbeit, f"entwurf_{key}.json")
        try:
            ent = json.load(open(ep, encoding="utf-8"))
        except Exception as ex:
            ergebnis[key] = {"status": "FEHLER", "detail": f"Entwurf nicht lesbar: {type(ex).__name__}: {ex}"}
            continue
        volltext = norm(" ".join(z.split("] ", 1)[1] for z in e["zeilen"]))
        pub_text = ent.get("publikum_text")
        pub_fehler = publikum_ok(pub_text)
        gueltig, verworfen = [], []
        for pkt in (ent.get("werkstatt") or [])[:MAX_PUNKTE]:
            z = norm(str(pkt.get("zitat", "")))
            grund = None
            if pkt.get("dimension") not in DIMENSIONEN: grund = "Dimension ungültig"
            elif pkt.get("gewicht") not in GEWICHTE: grund = "Gewicht ungültig"
            elif not (ZITAT_MIN <= len(z) <= ZITAT_MAX): grund = f"Zitatlänge {len(z)}"
            elif z not in volltext: grund = "Zitat nicht in der Ausgabe gefunden"
            (verworfen if grund else gueltig).append(dict(pkt, zitat=z, **({"grund": grund} if grund else {})))
        vorschlaege = [str(v)[:VORSCHLAG_MAX] for v in (ent.get("vorschlaege") or [])[:MAX_VORSCHLAEGE]]
        kopf = {"ausgabe": {"datum": e["datum"], "datei": e["datei"], "sha256": e["sha256"], "pages_commit": k["pages_commit"]},
                "erzeugt_am": k["zeit"],
                "erzeugt_von": {"instanz": k["kennung"], "modell": "claude-haiku-4-5-20251001 (Konfiguration der Aufgabe, keine Selbstauskunft)"},
                "pruefskript_sha256": k["skript_sha256"], "lauf_id": k["lauf_id"]}
        pub = {"schema": "radar724-review-publikum/1", "ableger": key, "status": "FEHLER" if pub_fehler else "OK",
               "titel": "Was die KI zu dieser Ausgabe sagt", "text": "" if pub_fehler else pub_text.strip(),
               "hinweis": "Automatisch erstellt von Claude (Anthropic). Kann irren."}
        pub.update(kopf)
        if pub_fehler: pub["fehler"] = pub_fehler
        ziel = os.path.join(c1, "review", key)
        os.makedirs(ziel, exist_ok=True)
        with open(os.path.join(ziel, f"{e['datum']}.publikum.json"), "w", encoding="utf-8") as f:
            json.dump(pub, f, ensure_ascii=False, indent=1); f.write("\n")
        md = [f"# Werkstatt-Review {e['name']} — Ausgabe {e['datum']}", "",
              f"Datei: `{e['datei']}` · SHA-256 `{e['sha256']}` · Pages-Commit `{k['pages_commit']}`",
              f"Erzeugt: {k['zeit']['wert']} ({k['zeit']['quelle']}) · Instanz: {k['kennung']} · Lauf: {k['lauf_id']}",
              f"Prüfskript SHA-256: `{k['skript_sha256']}`",
              "Hinweis: Werkstatt-Datei, nur für das Team. Nie auf eine Live-Seite übernehmen.", ""]
        if pub_fehler: md += [f"**Publikumstext verworfen:** {pub_fehler}", ""]
        for dim in DIMENSIONEN:
            md.append(f"## {dim.capitalize()}")
            pts = [x for x in gueltig if x["dimension"] == dim]
            md += [f"{i}. [{x['gewicht']}] {str(x.get('befund', '')).strip()} — Stelle: „{x['zitat']}“ (Zitat geprüft: ja)" for i, x in enumerate(pts, 1)] or ["(keine Punkte)"]
            md.append("")
        md.append("## Harte Prüfungen (Skript)")
        md += ["| Prüfung | ok | Detail |", "|---|---|---|"]
        md += [f"| {p['pruefung']} | {'ja' if p['ok'] else 'NEIN'} | {str(p['detail']).replace('|', '/')} |" for p in e["harte_pruefungen"]]
        md += ["", "## Vorschläge für die nächste Ausgabe"] + ([f"{i}. {v}" for i, v in enumerate(vorschlaege, 1)] or ["(keine)"])
        if verworfen:
            md += ["", "## Vom Skript verworfene Punkte (Zitat nicht belegbar oder Form ungültig)"]
            md += [f"- {x.get('grund')}: „{x['zitat'][:120]}“" for x in verworfen]
        with open(os.path.join(ziel, f"{e['datum']}.werkstatt.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(md) + "\n")
        ergebnis[key] = {"status": pub["status"], "punkte_gueltig": len(gueltig), "punkte_verworfen": len(verworfen),
                         "publikum_fehler": pub_fehler}
    os.makedirs(os.path.join(c1, "review", "laeufe"), exist_ok=True)
    zeilen_md = [f"# Lauf {k['lauf_id']} — {k['kennung']}", "",
                 f"Zeit: {k['zeit']['wert']} ({k['zeit']['quelle']})",
                 f"Pages-Commit: {k.get('pages_commit')} · Prüfskript SHA-256: {k['skript_sha256']}",
                 f"Lauf-Status: {k['lauf_status']}" + (f" — {k['fehler']}" if k.get("fehler") else ""), "",
                 "| Ableger | Status | Detail |", "|---|---|---|"]
    zeilen_md += [f"| {a} | {v['status']} | {json.dumps({x: y for x, y in v.items() if x != 'status'}, ensure_ascii=False).replace('|', '/')} |" for a, v in ergebnis.items()]
    with open(os.path.join(c1, "review", "laeufe", f"{k['lauf_id']}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(zeilen_md) + "\n")
    print(json.dumps({"lauf_id": k["lauf_id"], "ergebnis": ergebnis}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("vorbereiten", "abschliessen"):
        sys.exit("Aufruf: review_skript.py vorbereiten|abschliessen <arbeitsordner> <claude_1-clone>")
    (vorbereiten if sys.argv[1] == "vorbereiten" else abschliessen)(sys.argv[2], sys.argv[3])
