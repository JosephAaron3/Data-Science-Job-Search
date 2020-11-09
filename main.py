from job_url_ws import *
from job_info_ws import *
from text_processor import *

def main():
    #User-defined values
    search_url = "https://seek.com.au/data-science-jobs"
    keywords = ['R', 'Python', 'SQL', 'C']
    
    total_kw = dict.fromkeys(keywords, 0)
    
    #Perform search
    urls = get_job_urls(search_url)
    for url in urls:
        text = get_text(url)
        text = clean_text(text)
        kw_presence = text_search(text, keywords)
        for key in keywords:
            if kw_presence[key]:
                total_kw[key] += 1
    
if __name__ == "__main__":
    main()