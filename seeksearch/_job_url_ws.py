import urllib
import urllib.request
from bs4 import BeautifulSoup as soup

def SearchLinkParser(url):
    page = urllib.request.urlopen(url)
    content = soup(page, 'html.parser')
    links = content.find_all(name = 'a', attrs = {'class': '_2iNL7wI'})
    return [link.get('href') for link in links]

def get_urls(url, limit = None):
    urls_all = []
    page_num = 1
    url_next = url

    while((page_urls := SearchLinkParser(url)) != []):
        urls_all.extend(page_urls)
        print("URLs gathered: ", len(urls_all))
        if limit != None and len(urls_all) >= limit:
            break
        page_num += 1
        url_next = ''.join([url, f'?page={page_num}'])
    return urls_all[:limit]


if __name__ == "__main__":
    urls = get_urls("https://seek.com.au/data-science-jobs", limit = 100)
    print(urls)
    