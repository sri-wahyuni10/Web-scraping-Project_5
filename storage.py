import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "data")
article_file = os.path.join(data_dir, "articles.json")
graph_file = os.path.join(data_dir, "graph.json")

def ensure_data_dir():
    os.makedirs(data_dir, exist_ok= True)
    
def save_articles(articles:list):
    ensure_data_dir()
    
    with open(article_file, 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent = 2, ensure_ascii = False)
        
        print(f"[storage] saved {len(articles)} on {article_file}")
        
def save_graph(articles:list):
    ensure_data_dir()
    url_to_title = {art['url']: art['title'] for art in articles}
    
    nodes = list(url_to_title.values())
    
    edges = []
    for art in articles:
        source_title = art["title"]
        for link_url in art["links"]:
            if link_url in url_to_title:
                target_title = url_to_title[link_url]
                if source_title != target_title:
                    edges.append({
                        "from" : source_title,
                        "to" : target_title
                    })
    graph_data = {
        "nodes": nodes,
        "edges": edges
    }
    
    with open( graph_file, "w", encoding ="utf-8") as f :
        json.dump(graph_data, f, indent = 2, ensure_ascii = False)
        
    print (f"[storage] graph saved  {len(nodes)} nodes, {len(edges)} edges on {graph_file} ")
    
def load_articles():
    if not os.path.exists(articles_file):
        return []
    with open(articles_file, "r", encoding="utf-8") as f :
        return json.load(f)
    
    
def load_graph() -> dict:
    if not os.path.exists(graph_file):
        return {"nodes": [], "edges": []}
    with open(graph_file, "r", encoding="utf-8") as f:
        return json.load(f)