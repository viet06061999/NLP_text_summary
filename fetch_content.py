import bs4 as BeaurifulSoup
import urllib.request

#'https://en.wikipedia.org/wiki/20th_century'

def fetch_data(url):
    # featch content URL
    fetched_data = urllib.request.urlopen(url)

    article_read = fetched_data.read()
    
    #parsing content URL

    article_parsed = BeaurifulSoup.BeautifulSoup(article_read, 'html.parser')

    #return <p></> tag
    paragraphs = article_parsed.find_all('p')

    article_content = ''

    for p in paragraphs:
        article_content += p.text 
    return article_content    