from job_url_ws import *
from job_info_ws import *
from text_processor import *
from tqdm import tqdm

def main():
    #User-defined values
    base_url = "https://www.seek.com.au"
    search_url = "https://seek.com.au/data-science-jobs"
    keywords = ['R', 'Python', 'SQL', 'C', 'Java', 'C++']
    
    total_kw = dict.fromkeys(keywords, 0)
    
    #Perform search
    urls = get_job_urls(search_url)
    print("Scraping job info:")
    for url in tqdm(urls):
        try:
            text = get_text(base_url+url)
        except:
            continue
        text = clean_text(text)
        kw_presence = text_search(text, keywords)
        for key in keywords:
            if kw_presence[key]:
                total_kw[key] += 1
    print(total_kw)
    
if __name__ == "__main__":
    main()