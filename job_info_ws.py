from html.parser import HTMLParser
import urllib
import urllib.request

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

def get_text(url):
    f = urllib.request.urlopen(url)
    text = f.read()
    f.close()
    parser = JobLinkParser()
    parser.feed(str(text))
    return parser.get_text()
    
def main():
    job_url = 'https://www.seek.com.au/job/50732163?type=promoted#searchRequestToken=caac9ad3-e493-49bd-bf71-94137f7948be'
    text = get_text(job_url)
    print(text)

if __name__ == "__main__":
    main()