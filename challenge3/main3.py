import requests
from bs4 import BeautifulSoup
from googlesearch import search
import json

def scrape_google(query, num_results=10):
    results = []
    for url in search(query, num_results=num_results, stop=num_results):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.title.string.strip() if soup.title else None
        description = soup.find('meta', attrs={'name': 'description'})
        description = description['content'].strip() if description else None
        result = {
            'title': title,
            'url': url,
            'description': description
        }
        results.append(result)
    return results

if __name__ == "__main__":
    query = input("Enter search query: ")
    results = scrape_google(query, num_results=10)
    with open('google_results.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Results saved to google results.json")