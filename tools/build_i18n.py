#!/usr/bin/env python3
"""
Générateur i18n du portfolio (statique, sans dépendance).

Principe :
- Le FR reste la source canonique (fichiers à la racine / dans pages/).
- Les éléments traduisibles portent un attribut data-i18n="<clé>".
- Les traductions vivent dans i18n/<lang>.json  { "<clé>": "<html traduit>" }.
- Pour chaque langue cible (en/ru/zh/es), on clone chaque page FR dans /<lang>/,
  en remplaçant le contenu des éléments taggués, en réécrivant les chemins
  d'assets partagés en absolu, en fixant <html lang>, et en injectant hreflang +
  sélecteur de langue (+ police CJK pour zh).
- Pour 'fr' (in place), on n'injecte QUE le sélecteur de langue et les hreflang
  (aucune traduction, chemins relatifs conservés).

Usage : python tools/build_i18n.py
Idempotent : peut être relancé sans effet cumulatif (blocs délimités par marqueurs).
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N_DIR = ROOT / "i18n"
SITE = "https://portfolio.stephanemuraro.fr"

# Pages activées pour la génération i18n (chemins relatifs à la racine du dépôt).
# On ajoute une page ici une fois qu'elle est annotée (data-i18n) ET traduite
# dans i18n/<lang>.json. Les 23 pages du site sont couvertes.
PAGES = [
    "index.html",
    "pages/about.html",
    "pages/vm302-station-dev-ia.html",
    "pages/second-cerveau-opencode.html",
    "pages/architecture.html",
    "pages/infrastructure.html",
    "pages/proxmox.html",
    "pages/reverse_proxy.html",
    "pages/gpu_passthrough.html",
    "pages/storage_zfs.html",
    "pages/os.html",
    "pages/network.html",
    "pages/ia_llm.html",
    "pages/rag.html",
    "pages/ia_image.html",
    "pages/speech_ai.html",
    "pages/vm301-hermes-opencode.html",
    "pages/docker.html",
    "pages/nextcloud.html",
    "pages/n8n.html",
    "pages/python.html",
    "pages/git.html",
    "pages/obsidian.html",
    "pages/devops.html",
]

# fr en premier (traité in place), puis les langues générées.
# LANGS = langues construites localement (préviennent le poste de Stéphane).
# PUBLIC_LANGS = langues annoncées au public : sélecteur de langue + hreflang.
# ru reste dans LANGS (généré et entretenu en local) mais hors PUBLIC_LANGS
# (jamais de lien vers /ru/ ni de hreflang dans les pages publiées) ; le
# dossier /ru/ et i18n/ru.json sont en outre exclus du dépôt via .gitignore.
LANGS = ["fr", "en", "ru", "es"]
PUBLIC_LANGS = ["fr", "en", "es"]
LANG_LABEL = {"fr": "FR", "en": "EN", "ru": "RU", "es": "ES"}
HTML_LANG = {"fr": "fr", "en": "en", "ru": "ru", "es": "es"}

SW_START, SW_END = "<!--LANG_SWITCHER_START-->", "<!--LANG_SWITCHER_END-->"
HL_START, HL_END = "<!--HREFLANG_START-->", "<!--HREFLANG_END-->"
CJK_START, CJK_END = "<!--CJK_FONT_START-->", "<!--CJK_FONT_END-->"


def load_dict(lang: str) -> dict:
    p = I18N_DIR / f"{lang}.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def esc_attr(s: str) -> str:
    return s.replace("&", "&amp;").replace('"', "&quot;")


def apply_translation(html: str, key: str, val: str) -> str:
    """Remplace le contenu de TOUS les éléments taggués data-i18n="key" par val.

    Hypothèse (respectée par nos annotations) : un bloc taggué ne contient
    jamais un élément de même nom → le premier </tag> ferme bien le bloc.
    Pour <meta>, on remplace l'attribut content. Pour <title>/autres, le inner.
    Les occurrences sont traitées de droite à gauche pour ne pas décaler les
    positions restantes.
    """
    open_re = re.compile(r'<([a-zA-Z0-9]+)((?:[^>]*?)\sdata-i18n="' + re.escape(key) + r'")([^>]*)>')
    matches = list(open_re.finditer(html))
    for m in reversed(matches):
        tag = m.group(1).lower()
        if tag == "meta":
            open_tag = m.group(0)
            if 'content="' in open_tag:
                new_tag = re.sub(r'content="(?:.*?)"', 'content="' + esc_attr(val) + '"', open_tag, count=1)
            else:
                new_tag = open_tag[:-1] + ' content="' + esc_attr(val) + '">'
            html = html[:m.start()] + new_tag + html[m.end():]
            continue
        start = m.end()
        close = re.search(r'</' + re.escape(tag) + r'\s*>', html[start:], re.IGNORECASE)
        if not close:
            continue
        end = start + close.start()
        html = html[:start] + val + html[end:]
    return html


def switcher_block(cur_lang: str, rel: str) -> str:
    codes = list(PUBLIC_LANGS)
    if cur_lang not in codes:
        codes.append(cur_lang)  # ex. ru : visible seulement quand on navigue déjà en local dedans
    items = []
    for code in codes:
        href = "/" + rel if code == "fr" else "/" + code + "/" + rel
        cls = ' class="active"' if code == cur_lang else ""
        items.append(f'<a href="{href}"{cls}>{LANG_LABEL[code]}</a>')
    menu = "".join(items)
    return (
        SW_START
        + '<div class="nav-dd nav-lang"><button class="nav-dd-toggle" type="button">\U0001F310 '
        + LANG_LABEL[cur_lang]
        + ' ▾</button><div class="nav-dd-menu">'
        + menu
        + "</div></div>"
        + SW_END
    )


def hreflang_block(rel: str) -> str:
    lines = [HL_START]
    for code in PUBLIC_LANGS:
        href = f"{SITE}/{rel}" if code == "fr" else f"{SITE}/{code}/{rel}"
        lines.append(f'<link rel="alternate" hreflang="{code}" href="{href}"/>')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}/{rel}"/>')
    lines.append(HL_END)
    return "\n".join(lines)


def cjk_font_block() -> str:
    return (
        CJK_START
        + '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet"/>'
        + '<style>body{font-family:\'Inter\',\'Noto Sans SC\',\'Segoe UI\',system-ui,sans-serif;}</style>'
        + CJK_END
    )


def upsert_between(html: str, start_mark: str, end_mark: str, block: str, anchor_before: str) -> str:
    """Insère/remplace un bloc délimité. Si les marqueurs existent, on remplace ;
    sinon on insère juste avant `anchor_before` (ex. '</head>')."""
    pat = re.compile(re.escape(start_mark) + r".*?" + re.escape(end_mark), re.DOTALL)
    if pat.search(html):
        return pat.sub(lambda _: block, html, count=1)
    return html.replace(anchor_before, block + "\n" + anchor_before, 1)


def rewrite_assets(html: str) -> str:
    # ../css/ ../js/ ../assets/  ET  css/ js/ assets/  ->  /css/ /js/ /assets/
    return re.sub(r'(href|src)="(?:\.\./)?(css|js|assets)/', r'\1="/\2/', html)


def process(rel: str, lang: str, dic: dict) -> None:
    src = ROOT / rel
    html = src.read_text(encoding="utf-8")

    if lang != "fr":
        # traductions
        for key, val in dic.items():
            html = apply_translation(html, key, val)
        # chemins d'assets en absolu
        html = rewrite_assets(html)
        # attribut lang
        html = re.sub(r'<html\s+lang="fr">', f'<html lang="{HTML_LANG[lang]}">', html, count=1)
        # police CJK pour le chinois
        if lang == "zh":
            html = upsert_between(html, CJK_START, CJK_END, cjk_font_block(), "</head>")

    # sélecteur de langue (toutes langues, fr inclus)
    html = re.sub(re.escape(SW_START) + r".*?" + re.escape(SW_END),
                  lambda _: switcher_block(lang, rel), html, count=1, flags=re.DOTALL)
    # hreflang (toutes langues)
    html = upsert_between(html, HL_START, HL_END, hreflang_block(rel), "</head>")

    if lang == "fr":
        out = src
    else:
        out = ROOT / lang / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  [{lang}] {out.relative_to(ROOT)}")


def main() -> None:
    dicts = {lang: load_dict(lang) for lang in LANGS}
    for lang in LANGS:
        print(f"== {lang} ==")
        for rel in PAGES:
            process(rel, lang, dicts.get(lang, {}))
    print("OK")


if __name__ == "__main__":
    main()
