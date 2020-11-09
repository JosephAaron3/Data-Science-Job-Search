from ._job_url_ws import get_urls
from ._job_info_ws import get_text
from ._text_processor import *
from tqdm import tqdm

def main(url, keywords, limit = None):
    total_kw = dict.fromkeys(keywords, 0)
    
    #Perform search
    urls = get_urls(url, limit)
    print("Scraping job info...")
    for url in tqdm(urls):
        try:
            text = get_text(url, clean = True)
        except:
            continue
        kw_presence = text_search(text, keywords)
        for key in keywords:
            if kw_presence[key]:
                total_kw[key] += 1
    
    #Print the list of keywords, sorted by frequency
    kw_freq = [(v,k) for k,v in total_kw.items()]
    kw_freq.sort(reverse=True)
    for k,v in kw_freq:
        print(f"{k}: {v}")
    return total_kw
    
if __name__ == "__main__":
    search_url = "https://seek.com.au/data-science-jobs"
    kw = ['R', 'Python', 'SQL', 'C', 'Java', 'C++', 'Spark', 'Hadoop',
                'C#', 'Tableau', 'Power BI', 'AWS', 'Azure', 'Scala', 'MATLAB',
                'Pig', 'Hive', 'Impala', 'Teradata', 'Oracle', 'SAS', 'MongoDB', 
                'Redshift', 'S3', 'EC2', 'Lambda', 'EMR', 'SageMaker', 'DynamoDB', 
                'Cloudformation', 'Athena', 'Kinesis', 'Cassandra', 'Alteryx', 
                'Jupyter', 'Clickhouse','PyTorch', 'TensorFlow']
    lim = 100
    main(search_url, kw, lim)