import requests
import sys

def encurtar_link(url):
    api_url = 'https://is.gd/create.php'
    params = {
        'format': 'simple',
        'url': url
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python encurtador.py <url>")
        sys.exit(1)
    url_original = sys.argv[1]
    short_url = encurtar_link(url_original)
    if short_url:
        print("Link encurtado:", short_url)
    else:
        print("Erro ao encurtar o link.")
