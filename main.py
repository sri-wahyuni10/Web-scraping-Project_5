import sys
import os
from storage import save_articles, save_graph, load_graph
from visualizer import visualize, print_top_articles
from mock_data import Mock_articles
from scraper import run_scraper

start_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
max_pages = 30
delay = 1.0

def main():
    demo_mode = "--demo" in sys.argv
    
    if demo_mode :
        print("Mode Demo On")
        
    else:
        print("mode Online on")
        
    if demo_mode:
        articles = Mock_articles
    else:
        try:
            articles = run_scraper(
                start_url = start_url,
                max_pages = max_pages,
                delay = delay
            )
        except Exception as e:
            print("Scraping error...")
            
            sys.exit(1)
            
        
    print("Start Saving data.....")
    
    save_articles(articles)
    save_graph(articles)
    
    print("Making visualisation graph...")
    
    graph_data = load_graph()
    print_top_articles(graph_data, top_n = 10)
    visualize(graph_data)
    
    print("Selesai!")
    
if __name__ =="__main__":
    main() 