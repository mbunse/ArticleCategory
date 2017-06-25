from bs4 import BeautifulSoup

import requests

def getArticleCategoriesFromEbay(article):
    '''
    Return ebay site as html
    '''
    # Search for product
    url = 'https://www.ebay.de/sch/i.html'
    r = requests.get(url, params={'_nkw': article})

    # Extract link to first product mentioned
    soup = BeautifulSoup(r.text, 'html.parser')
    link_first_product = soup.find(id="ListViewInner").find('li', recursive=False).find('a').get('href')

    # 
    soup = BeautifulSoup(requests.get(link_first_product).text, 'html.parser')
    article_cats = []
    for cat in soup.find(id="vi-VR-brumb-lnkLst").find_all('span'):
        text = cat.get_text()
        if not text.startswith("Mehr anzeigen"):
            article_cats.append(cat.get_text())

    return article_cats

def test():
    '''
    Test functions in this module
    '''
    
    article = "Pioneer CDJ-2000 NXS2"
    categories = ['TV, Video & Audio', 'Veranstaltungs- & DJ-Equipment', 'DJ-CD-/MP3-Player']
    assert(getArticleCategoriesFromEbay(article)==categories)

    article = "Playstation"
    categories = ['PC- & Videospiele', 'Konsolen']
    assert(getArticleCategoriesFromEbay(article)==categories)


if __name__ == "__main__":
    test()