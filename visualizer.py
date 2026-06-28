"""
visualizer.py
-------------
Membuat visualisasi graf pengetahuan dari data articles.json
menggunakan NetworkX dan Matplotlib.

Output: knowledge_graph.png di folder screenshots/
"""

import os
import json
import networkx as nx
import matplotlib
matplotlib.use("Agg")   # gunakan backend non-GUI agar bisa simpan ke file
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "screenshots", "knowledge_graph.png")
GRAPH_FILE  = os.path.join(os.path.dirname(__file__), "data", "graph.json")


def build_graph(graph_data: dict) -> nx.DiGraph:
    """
    Bangun objek NetworkX DiGraph dari data graph.json.
    DiGraph = Directed Graph (graf berarah, karena link punya arah).
    """
    G = nx.DiGraph()

    # Tambahkan semua nodes (artikel)
    for node in graph_data["nodes"]:
        G.add_node(node)

    # Tambahkan semua edges (relasi link)
    for edge in graph_data["edges"]:
        G.add_edge(edge["from"], edge["to"])

    return G


def visualize(graph_data: dict) -> None:
    """
    Buat dan simpan gambar visualisasi graf pengetahuan.

    - Ukuran node proporsional dengan jumlah koneksinya (degree)
    - Node paling banyak koneksi = warna berbeda (hub utama)
    - Label hanya ditampilkan untuk node dengan koneksi terbanyak
    """

    print("\n  Membangun graf visualisasi...")

    G = build_graph(graph_data)

    if len(G.nodes) == 0:
        print("  [SKIP] Tidak ada data untuk divisualisasi.")
        return

    # ── Hitung degree tiap node ────────────────────────────────────────
    # degree = total koneksi masuk + keluar
    degree_dict = dict(G.degree())

    # Ukuran node: minimal 100, maksimal 2000, proporsional dengan degree
    max_degree   = max(degree_dict.values()) if degree_dict else 1
    node_sizes   = [
        100 + (degree_dict[n] / max_degree) * 1900
        for n in G.nodes()
    ]

    # ── Warna node berdasarkan kelompok degree ─────────────────────────
    node_colors = []
    for n in G.nodes():
        d = degree_dict[n]
        if d >= max_degree * 0.7:
            node_colors.append("#E63946")   # merah → hub utama
        elif d >= max_degree * 0.3:
            node_colors.append("#457B9D")   # biru  → koneksi sedang
        else:
            node_colors.append("#A8DADC")   # hijau muda → koneksi sedikit

    # ── Layout: spring layout (node saling "dorong-mendorong") ─────────
    print("  Menghitung layout spring (mungkin perlu beberapa detik)...")
    pos = nx.spring_layout(G, k=2.5, iterations=50, seed=42)

    # ── Tentukan node mana yang perlu label ───────────────────────────
    # Hanya tampilkan label untuk top 15 node dengan degree tertinggi
    top_nodes = sorted(degree_dict, key=degree_dict.get, reverse=True)[:15]
    labels = {n: _shorten(n, 20) for n in top_nodes}

    # ── Gambar ────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(18, 12))
    fig.patch.set_facecolor("#1A1A2E")
    ax.set_facecolor("#1A1A2E")

    # Gambar edges (tipis, transparan)
    nx.draw_networkx_edges(
        G, pos,
        ax=ax,
        edge_color="#444466",
        alpha=0.4,
        arrows=True,
        arrowsize=8,
        width=0.5,
        connectionstyle="arc3,rad=0.1"
    )

    # Gambar nodes
    nx.draw_networkx_nodes(
        G, pos,
        ax=ax,
        node_size=node_sizes,
        node_color=node_colors,
        alpha=0.9,
    )

    # Gambar label hanya untuk top nodes
    nx.draw_networkx_labels(
        G, pos,
        labels=labels,
        ax=ax,
        font_size=7,
        font_color="white",
        font_weight="bold",
    )

    # ── Judul dan legenda ─────────────────────────────────────────────
    ax.set_title(
        "Wikipedia Knowledge Graph",
        color="white", fontsize=18, fontweight="bold", pad=20
    )

    legend_patches = [
        mpatches.Patch(color="#E63946", label=f"Hub utama (degree ≥ {int(max_degree*0.7)})"),
        mpatches.Patch(color="#457B9D", label="Koneksi sedang"),
        mpatches.Patch(color="#A8DADC", label="Koneksi sedikit"),
    ]
    ax.legend(
        handles=legend_patches,
        loc="lower left",
        facecolor="#16213E",
        edgecolor="#457B9D",
        labelcolor="white",
        fontsize=9
    )

    # Statistik di pojok kanan bawah
    stats_text = (
        f"Nodes (artikel): {G.number_of_nodes()}\n"
        f"Edges (link): {G.number_of_edges()}\n"
        f"Node terhubung paling banyak:\n"
        f"  {top_nodes[0] if top_nodes else '-'} ({max_degree} koneksi)"
    )
    ax.text(
        0.98, 0.02, stats_text,
        transform=ax.transAxes,
        fontsize=8, color="#A8DADC",
        verticalalignment="bottom",
        horizontalalignment="right",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#16213E", alpha=0.8)
    )

    ax.axis("off")
    plt.tight_layout()

    # ── Simpan file ───────────────────────────────────────────────────
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    plt.savefig(OUTPUT_FILE, dpi=150, bbox_inches="tight", facecolor="#1A1A2E")
    plt.close()

    print(f"  ✓ Graf tersimpan → {OUTPUT_FILE}")


def print_top_articles(graph_data: dict, top_n: int = 10) -> None:
    """Cetak ranking artikel berdasarkan jumlah koneksi di terminal."""

    G = build_graph(graph_data)
    degree_dict = dict(G.degree())

    ranked = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)

    print(f"\n  {'─'*50}")
    print(f"  TOP {top_n} ARTIKEL (berdasarkan jumlah koneksi)")
    print(f"  {'─'*50}")
    for i, (title, deg) in enumerate(ranked[:top_n], 1):
        bar = "█" * min(deg, 30)
        print(f"  {i:>2}. {_shorten(title, 35):<35} {deg:>3} koneksi  {bar}")
    print(f"  {'─'*50}\n")


# ─────────────────────────────────────────────────────────────────────
# Helper
# ─────────────────────────────────────────────────────────────────────

def _shorten(text: str, max_len: int) -> str:
    """Potong teks jika terlalu panjang."""
    return text if len(text) <= max_len else text[:max_len - 1] + "…"