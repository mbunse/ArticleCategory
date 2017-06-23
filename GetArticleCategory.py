from bs4 import BeautifulSoup

import requests

def getArticleCategoriesFromEbay(article):
    '''
    Return ebay site as html
    '''
    # Search for product
    url = 'https://www.ebay.de/sch/i.html?_nkw=%(article)'
    r = requests.get(url, params={'_nkw': article})

    # Extract link to first product mentioned
    soup = BeautifulSoup(r.text, 'html.parser')
    link_first_product = soup.find(id="ListViewInner").a.get('href')

    # 
    soup = BeautifulSoup(requests.get(link_first_product).text, 'html.parser')
    article_cats = []
    for cat in soup.find(id="vi-VR-brumb-lnkLst").find_all('span'):
        article_cats.append(cat.get_text())

    return article_cats

def test():
    '''
    Test functions in this module
    '''
    
    article = "Pioneer CDJ-2000 NXS2"
    categories = ['TV, Video & Audio', 'Veranstaltungs- & DJ-Equipment', 'DJ-CD-/MP3-Player']
    assert(getArticleCategoriesFromEbay(article)==ebaySiteStart)


if __name__ == "__main__":
    test()