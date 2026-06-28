from typing import Optional
from bs4 import BeautifulSoup


def parse_wikipedia_page(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    # ── 1. Judul artikel ──────────────────────────────────────────────
    title_tag = soup.find("h1", id="firstHeading")
    title = title_tag.get_text(strip=True) if title_tag else "Unknown"

    # ── 2. Paragraf pertama sebagai summary ───────────────────────────
    summary = _extract_summary(soup)

    # ── 3. Link internal ke artikel Wikipedia lain ────────────────────
    links = _extract_links(soup)

    # ── 4. Kategori artikel ───────────────────────────────────────────
    categories = _extract_categories(soup)

    return {
        "url": url,
        "title": title,
        "summary": summary,
        "categories": categories,
        "links": links,
    }

def _extract_summary(soup: BeautifulSoup) -> str:
    content_div = soup.find("div", id="mw-content-text")
    if not content_div:
        return ""

    for p in content_div.find_all("p"):
        # Hapus semua tag <sup> dari paragraf ini (nomor referensi)
        for sup in p.find_all("sup"):
            sup.decompose()

        teks = p.get_text(strip=True)

        # Paragraf valid: minimal 50 karakter dan bukan kosong
        if len(teks) > 50:
            return teks

    return ""


def _extract_links(soup: BeautifulSoup) -> list:
    content_div = soup.find("div", id="mw-content-text")
    if not content_div:
        return []

    # Prefiks yang harus dibuang — bukan artikel biasa
    Exluded_prefixes = (
        "/wiki/File:",
        "/wiki/Help:",
        "/wiki/Wikipedia:",
        "/wiki/Talk:",
        "/wiki/Special:",
        "/wiki/Portal:",
        "/wiki/Template:",
        "/wiki/Category:",
        "/wiki/Main_Page",
    )

    links = []
    seen = set()  # hindari duplikat dalam satu halaman

    for a_tag in content_div.find_all("a", href=True):
        href = a_tag["href"]

        # Harus diawali /wiki/ dan tidak mengandung tanda #
        if not href.startswith("/wiki/"):
            continue
        if "#" in href:
            continue

        # Buang link ke halaman khusus
        if any(href.startswith(prefix) for prefix in Exluded_prefixes):
            continue

        full_url = "https://en.wikipedia.org" + href

        if full_url not in seen:
            seen.add(full_url)
            links.append(full_url)

    return links


def _extract_categories(soup: BeautifulSoup) -> list:
    cat_div = soup.find("div", id="mw-normal-catlinks")
    if not cat_div:
        return []

    categories = []
    for a_tag in cat_div.find_all("a"):
        teks = a_tag.get_text(strip=True)
        # Skip link "Categories" itu sendiri
        if teks.lower() != "categories":
            categories.append(teks)

    return categories