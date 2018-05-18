from bs4 import BeautifulSoup

import requests

def getArticleCategoriesFromEbay(article):
    '''
    Return ebay site as html
    '''
    # Search for product
    url = 'https://www.ebay.de/sch/i.html'
    r = requests.get(url, params={'_nkw': ' '.join(article.split()[:5])})

    try:
        # Extract link to first product mentioned
        soup = BeautifulSoup(r.text, 'lxml')
        link_first_product = soup.find('div', id="mainContent").find("ul").find('li', class_="s-item", recursive=False).find('a').get('href')
    
        # 
        soup = BeautifulSoup(requests.get(link_first_product).text, 'lxml')
        article_cats = []
        for cat in soup.find(id="vi-VR-brumb-lnkLst").find('td').find_all('span'):
            text = cat.get_text()
            if not text.startswith("Mehr anzeigen"):
                article_cats.append(cat.get_text())

    except AttributeError:
        return ["Unbekannt"]
    return article_cats

def test():
    '''
    Test functions in this module
    '''
    article = "LIQROCK E-MTB 29Zoll 500Wh Bosch Performance Line CX Modell"
    categories = ['Sport', 'Radsport', u'Elektrofahrr\xe4der']
    assert(getArticleCategoriesFromEbay(article)==categories)

    article = "Pioneer CDJ-2000 NXS2"
    categories = ['TV, Video & Audio', 'Veranstaltungs- & DJ-Equipment', 'DJ-CD-/MP3-Player']
    assert(getArticleCategoriesFromEbay(article)==categories)

    article = "Playstation"
    categories = ['PC- & Videospiele', 'Konsolen']
    assert(getArticleCategoriesFromEbay(article)==categories)


if __name__ == "__main__":
    test()