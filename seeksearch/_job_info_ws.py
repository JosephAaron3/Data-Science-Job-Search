from bs4 import BeautifulSoup as soup
import urllib
import urllib.request
from ._text_processor import clean_text

def JobLinkParser(url):
    page = urllib.request.urlopen(url)
    content = soup(page, 'html.parser')
    text_full = content.find_all(name = 'div', attrs = {'data-automation': ['templatetext','jobAdDetails']})
    text_full = text_full[0].find_all(['p','li'])
    return [text_full[j].text for j in range(len(text_full))]

def get_text(url, clean = False):
    if url[:5] != 'https':
        text = JobLinkParser("https://www.seek.com.au"+url)
    else:
        text = JobLinkParser(url)
    if clean:
        text = clean_text(text)
    return text

if __name__ == "__main__":
    text = get_text('https://www.seek.com.au/job/50907358?type=standard#searchRequestToken=88e63196-4468-46f6-b91c-bd0e450a4d6a')
    print(text)