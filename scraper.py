"""
scraper.py
----------
Logika utama scraping dengan sistem antrean (BFS).
Menggunakan Wikipedia Action API (json format) — lebih stabil dan
tidak mudah diblokir dibanding scraping HTML langsung.

Endpoint: https://en.wikipedia.org/w/api.php

Alur kerja:
  1. Mulai dari judul artikel pertama
  2. Fetch data lewat API → ambil summary + links
  3. Masukkan link baru ke antrean
  4. Ulangi sampai batas halaman tercapai
"""

import time
import requests
from typing import Optional


# ─────────────────────────────────────────────────────────────────────
# Wikipedia API endpoint
# ─────────────────────────────────────────────────────────────────────

api_URL = "https://en.wikipedia.org/w/api.php"

Headers = {
    "User-Agent": "WikipediaKnowledgeScraper/1.0 (educational project; contact@example.com)"
    # Wikipedia minta User-Agent yang deskriptif untuk API usage
}


# ─────────────────────────────────────────────────────────────────────
# Fungsi utama scraper
# ─────────────────────────────────────────────────────────────────────

def run_scraper(start_url: str, max_pages: int = 30, delay: float = 1.0) -> list:
    start_title = _url_to_title(start_url)

    # ── Inisialisasi tiga komponen utama ──────────────────────────────
    queue   = [start_title] 
    visited = set()  
    hasil   = [] 

    print(f"\n{'='*60}")
    print(f"  Wikipedia Scraper - BFS Queue")
    print(f"  Start : {start_title}")
    print(f"  Max   : {max_pages} halaman")
    print(f"  Delay : {delay}s per request")
    print(f"{'='*60}\n")

    # ── Loop utama ────────────────────────────────────────────────────
    while queue and len(hasil) < max_pages:

        title = queue.pop(0)

        if title in visited:
            continue

        data = _fetch_article(title)

        if data is None:
            visited.add(title)
            continue

        hasil.append(data)
        visited.add(title)

        print(
            f"  [{len(hasil):>3}/{max_pages}] ✓ {data['title'][:52]:<52} "
            f"| {len(data['links'])} links"
        )

        # Masukkan link baru ke antrean
        for link_title in data["links"]:
            if link_title not in visited:
                queue.append(link_title)

        time.sleep(delay)
    print(f"  Selesai! {len(hasil)} artikel terkumpul.")

    return hasil


def _fetch_article(title: str, retries: int = 3):

    for attempt in range(1, retries + 1):
        try:
            # ── Request 1: ambil extract (summary) + kategori ─────────
            params_extract = {
                "action":       "query",
                "format":       "json",
                "titles":       title,
                "prop":         "extracts|categories",
                "exintro":      True,       # hanya intro/paragraf pertama
                "explaintext":  True,       # teks polos tanpa HTML
                "exsentences":  3,          # max 3 kalimat
                "cllimit":      10,         # max 10 kategori
                "redirects":    1,
            }

            r1 = requests.get(api_URL, params=params_extract,
                              headers=Headers, timeout=10)
            r1.raise_for_status()
            data1 = r1.json()

            pages = data1.get("query", {}).get("pages", {})
            page  = next(iter(pages.values()))

            # Artikel tidak ditemukan
            if "missing" in page:
                return None

            real_title = page.get("title", title)
            extract    = page.get("extract", "").strip()
            categories = [
                c["title"].replace("Category:", "")
                for c in page.get("categories", [])
            ]

            if not extract:
                return None
            params_links = {
                "action":    "query",
                "format":    "json",
                "titles":    title,
                "prop":      "links",
                "pllimit":   30,        # ambil max 30 link per artikel
                "plnamespace": 0,       # namespace 0 = artikel biasa saja
                "redirects": 1,
            }

            r2 = requests.get(api_URL, params=params_links,
                              headers=Headers, timeout=10)
            r2.raise_for_status()
            data2 = r2.json()

            pages2 = data2.get("query", {}).get("pages", {})
            page2  = next(iter(pages2.values()))

            raw_links = page2.get("links", [])

            # Konversi judul link → URL lengkap
            link_titles = [lnk["title"] for lnk in raw_links]
            link_urls   = [
                f"https://en.wikipedia.org/wiki/{t.replace(' ', '_')}"
                for t in link_titles
            ]

            url = f"https://en.wikipedia.org/wiki/{real_title.replace(' ', '_')}"

            return {
                "url":        url,
                "title":      real_title,
                "summary":    extract,
                "categories": categories,
                "links":      link_urls,
                # Simpan juga judul link (dipakai scraper untuk antrean berikutnya)
                "_link_titles": link_titles,
            }

        except requests.Timeout:
            print(f"  [Attempt {attempt}/{retries}] Timeout: {title}")
            if attempt < retries:
                time.sleep(3)

        except requests.ConnectionError:
            print(f"  [Attempt {attempt}/{retries}] Koneksi gagal: {title}")
            if attempt < retries:
                time.sleep(5)

        except Exception as e:
            print(f"  [ERROR] {title}: {e}")
            return None

    return None


def run_scraper(start_url: str, max_pages: int = 30, delay: float = 1.0) -> list:
    """Versi final: antrean pakai JUDUL artikel, bukan URL."""

    start_title = _url_to_title(start_url)

    queue   = [start_title]
    visited = set()
    hasil   = []

    print(f"\n{'='*60}")
    print(f"  Wikipedia Scraper - BFS Queue (via API)")
    print(f"  Start : {start_title}")
    print(f"  Max   : {max_pages} halaman | Delay: {delay}s")
    print(f"{'='*60}\n")

    while queue and len(hasil) < max_pages:

        title = queue.pop(0)

        if title in visited:
            continue

        data = _fetch_article(title)

        if data is None:
            visited.add(title)
            continue

        hasil.append(data)
        visited.add(title)

        print(
            f"  [{len(hasil):>3}/{max_pages}] ✓ {data['title'][:52]:<52} "
            f"| {len(data['links'])} links"
        )

        # Gunakan _link_titles (judul) untuk antrean, bukan URL
        for link_title in data.get("_link_titles", []):
            if link_title not in visited:
                queue.append(link_title)

        time.sleep(delay)

    print(f"\n{'='*60}")
    print(f"  Selesai! {len(hasil)} artikel terkumpul.")
    print(f"{'='*60}\n")

    return hasil


def _url_to_title(url: str) -> str:

    if "/wiki/" in url:
        raw = url.split("/wiki/")[-1]
        return raw.replace("_", " ")
    return url