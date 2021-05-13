from bs4 import BeautifulSoup as Soup
import urllib
import urllib.request
import re
from tqdm import tqdm


class SeekSearch:
    def __init__(self, url, titles):
        self.url = url
        self.job_titles = titles

    @staticmethod
    def _job_link_parser(url):
        page = urllib.request.urlopen(url)
        content = Soup(page, 'html.parser')
        text_full = content.find_all(name='div', attrs={'class': ['templatetext', 'FYwKg WaMPc_4']})
        text_full = text_full[0].find_all(['p', 'li'])
        return [text_full[j].text for j in range(len(text_full))]

    def _get_text(self, url, clean=False):
        if url[:5] != 'https':
            text = self._job_link_parser("https://www.seek.com.au" + url)
        else:
            text = self._job_link_parser(url)
        if clean:
            text = self._clean_text(text)
        return text

    def _search_link_parser(self, url):
        page = urllib.request.urlopen(url)
        content = Soup(page, 'html.parser')
        links = content.find_all(name='a', attrs={'class': '_2S5REPk'})
        return [link.get('href') for link in links if any(keywords in link.text
                                                          for keywords in self.job_titles)]

    def _get_urls(self, url, limit=None):
        urls_all = []
        page_num = 1
        url_next = url

        while page_urls := self._search_link_parser(url_next):
            urls_all.extend(page_urls)
            print("URLs gathered: ", len(urls_all))
            if limit is not None and len(urls_all) >= limit:
                break
            page_num += 1
            url_next = ''.join([url, f'?page={page_num}'])
        return urls_all[:limit]

    @staticmethod
    def _clean_text(text_list):
        # Remove unformatted symbols
        bad_format = [('\\xe2\\x80\\x99', "'"), ('\\xe2\\x80\\x9c', '"'), ('\\xe2\\x80\\x9d', '"'),
                      ('\\xc2\\xa0', ' '), ('\\xc2\\xa0', ' ')]
        alt_text = ' '.join(text_list)
        for cur, new in bad_format:
            alt_text = alt_text.replace(cur, new)
        return alt_text

    @staticmethod
    def _text_search(text, keywords):
        kw_check = dict.fromkeys(keywords, False)
        for base in keywords:
            # Create alternate forms of the base word
            if len(base) == 1:  # Handle things like R and C
                forms = [' ' + base + ' ', ' ' + base + ',', ',' + base + ',',
                         '/' + base + '/', '/' + base + ' ', ' ' + base + '/']
            else:
                forms = [base]
            try:  # Handle errors from things like C++ in re
                if any(re.search(word, text, re.IGNORECASE) for word in forms):
                    kw_check[base] = True
            except Exception:
                if any(word in text for word in forms):
                    kw_check[base] = True
        return kw_check

    def run_search(self, keywords, limit=None):
        total_kw = dict.fromkeys(keywords, 0)

        # Perform search
        urls = self._get_urls(self.url, limit)
        print("Scraping job info...")
        for url in tqdm(urls):
            try:
                text = self._get_text(url, clean=True)
            except Exception:
                continue
            kw_presence = self._text_search(text, keywords)
            for key in keywords:
                if kw_presence[key]:
                    total_kw[key] += 1

        # Print the list of keywords, sorted by frequency
        kw_freq = [(v, k) for k, v in total_kw.items()]
        kw_freq.sort(reverse=True)
        for k, v in kw_freq:
            print(f"{k}: {v}")
        return total_kw


if __name__ == "__main__":
    search_url = "https://seek.com.au/data-science-jobs"
    job_titles = ["Data Science", "Scientist", "Analyst"]
    mySearch = SeekSearch(search_url, job_titles)

    kw = ['R', 'Python', 'SQL', 'C', 'Java', 'C++', 'Spark', 'Hadoop', 'C#', 'Tableau', 'Power BI',
          'AWS', 'Azure', 'Scala', 'MATLAB', 'Pig', 'Hive', 'Impala', 'Teradata', 'Oracle', 'SAS',
          'MongoDB', 'Redshift', 'S3', 'EC2', 'Lambda', 'EMR', 'SageMaker', 'DynamoDB',
          'Cloudformation', 'Athena', 'Kinesis', 'Cassandra', 'Alteryx', 'Jupyter', 'Clickhouse',
          'PyTorch', 'TensorFlow']
    lim = 100
    mySearch.run_search(kw, lim)
