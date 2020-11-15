from html.parser import HTMLParser
import urllib
import urllib.request
from _text_processor import clean_text

class JobLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._recording = False
        self._in_block = False
        self._text = []

    def handle_starttag(self, tag, attr):
        if tag == 'div':
            for name, value in attr:
                if name == 'class' and value in ['templatetext', 'FYwKg WaMPc_4']:
                    self._in_block = True
        elif self._in_block and tag in ['p', 'li']:
            self._recording = True
                    
    def handle_endtag(self, tag):
        if tag == '/div':
            self._in_block = False

    def handle_data(self, data):
        if self._recording:
            self._text.append(data)
            self._recording = False
    
    def get_text(self):
        return self._text

def get_text(url, clean = False):
    if url[:5] != 'https':
        f = urllib.request.urlopen("https://www.seek.com.au"+url)
    else:
        f = urllib.request.urlopen(url)
    fulltext = f.read()
    f.close()
    parser = JobLinkParser()
    parser.feed(str(fulltext))
    text = parser.get_text()
    if clean:
        text = clean_text(text)
    return text

if __name__ == "__main__":
    text = get_text('https://www.seek.com.au/job/50907358?type=standard#searchRequestToken=88e63196-4468-46f6-b91c-bd0e450a4d6a')
    print(text)