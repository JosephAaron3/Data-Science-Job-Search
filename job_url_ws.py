import urllib
import urllib.request
from html.parser import HTMLParser
import math

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

def get_job_urls(url, limit = math.inf):
    urls_all = []
    page_num = 1
    
    f = urllib.request.urlopen(url)
    text = f.read()
    f.close()
    parser = SearchLinkParser()
    parser.feed(str(text))
    while((page_urls := parser.get_urls()) != [] and len(urls_all) < limit):
        urls_all.extend(page_urls)
        page_num += 1
        url_next = ''.join([url, f'?page={page_num}'])
        f = urllib.request.urlopen(url_next)
        text = f.read()
        f.close()
        parser = SearchLinkParser()
        parser.feed(str(text))
        print(len(urls_all))

    return urls_all[:limit]

def main():
    search_url = "https://seek.com.au/data-science-jobs"
    urls = get_job_urls(search_url)
    print(urls)

if __name__ == "__main__":
    main()