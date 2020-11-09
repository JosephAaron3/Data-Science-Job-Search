import urllib
import urllib.request
from html.parser import HTMLParser

class SearchLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._recording = 0
        self._in_url = 0
        self._urls = []

    def handle_starttag(self, tag, attr):
        if tag == 'a' and ('class', '_2iNL7wI') in attr:
            self._urls.extend([link for tag, link in attr if tag == 'href'])
    
    def get_urls(self):
        return self._urls

def get_urls(url, limit = None):
    urls_all = []
    page_num = 1
    
    f = urllib.request.urlopen(url)
    text = f.read()
    f.close()
    parser = SearchLinkParser()
    parser.feed(str(text))
    while((page_urls := parser.get_urls()) != []):
        urls_all.extend(page_urls)
        print("URLs gathered: ", len(urls_all))
        if limit != None and len(urls_all) >= limit:
            break
        page_num += 1
        url_next = ''.join([url, f'?page={page_num}'])
        f = urllib.request.urlopen(url_next)
        text = f.read()
        f.close()
        parser = SearchLinkParser()
        parser.feed(str(text))
    return urls_all[:limit]

if __name__ == "__main__":
    urls = get_urls("https://seek.com.au/data-science-jobs", limit = 100)
    print(urls)
    