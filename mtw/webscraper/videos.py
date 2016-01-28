import requests
from bs4 import BeautifulSoup


def alltube_movie(html_doc):
    movie_data = []
    soup = BeautifulSoup(html_doc, 'html.parser')
    for link in soup.find_all('a'):
        if link.get('data-urlhost'):
            movie_data.append(
                {'url': link.get('data-urlhost'),
                 'version': link.get('data-short')})
    return movie_data


def find_movie(url):
    try:
        r = requests.get(url)
        html_doc = r.text

        if 'alltube.tv' in url:
            return alltube_movie(html_doc)
        return url

    except requests.ConnectionError as err:
        return "Connection aborted"