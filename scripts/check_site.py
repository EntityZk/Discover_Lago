#!/usr/bin/env python3
"""Lightweight checks for Discover Lago's static HTML pages."""
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted(ROOT.glob("*.html"))
ERRORS = []

class PageParser(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.links = []
        self.title_count = 0
        self.lang = False
        self.viewport = False
        self.description = False
        self.in_title = False
        self.title_text = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html" and attrs.get("lang"):
            self.lang = True
        if tag == "title":
            self.title_count += 1
            self.in_title = True
        if tag == "meta":
            if attrs.get("name", "").lower() == "viewport":
                self.viewport = bool(attrs.get("content"))
            if attrs.get("name", "").lower() == "description":
                self.description = bool(attrs.get("content", "").strip())
        if attrs.get("id"):
            ident = attrs["id"]
            if ident in self.ids:
                ERRORS.append(f"{self.path.name}: ID duplicato: #{ident}")
            self.ids.add(ident)
        for key in ("href", "src"):
            value = attrs.get(key, "").strip()
            if value:
                self.links.append((key, value))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data.strip()

if not PAGES:
    print("ERRORE: nessun file HTML trovato nella root.")
    sys.exit(1)

for page in PAGES:
    parser = PageParser(page)
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        ERRORS.append(f"{page.name}: impossibile leggere il file ({exc})")
        continue

    if not parser.lang:
        ERRORS.append(f"{page.name}: manca lang nell'elemento html")
    if parser.title_count != 1 or not parser.title_text:
        ERRORS.append(f"{page.name}: deve avere un solo title non vuoto")
    if not parser.viewport:
        ERRORS.append(f"{page.name}: manca meta viewport")
    if not parser.description:
        ERRORS.append(f"{page.name}: manca meta description")

    for attr, raw_url in parser.links:
        parts = urlsplit(raw_url)
        if parts.scheme or raw_url.startswith("//") or not parts.path:
            continue
        target = (page.parent / unquote(parts.path)).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            ERRORS.append(f"{page.name}: percorso fuori dal progetto: {raw_url}")
            continue
        if not target.exists():
            ERRORS.append(f"{page.name}: {attr} punta a un file inesistente: {raw_url}")
            continue
        if parts.fragment and target.suffix.lower() in (".html", ".htm"):
            try:
                target_parser = PageParser(target)
                target_parser.feed(target.read_text(encoding="utf-8"))
                if parts.fragment not in target_parser.ids:
                    ERRORS.append(f"{page.name}: ancora inesistente: {raw_url}")
            except OSError:
                pass

if ERRORS:
    print("Controllo sito FALLITO:")
    for error in ERRORS:
        print(f" - {error}")
    sys.exit(1)

print(f"Controllo completato: {len(PAGES)} pagine HTML, metadati e link interni verificati.")
