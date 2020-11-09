from job_url_ws import *
from job_info_ws import *
from text_processor import *
from tqdm import tqdm

def main():
    #User-defined values
    base_url = "https://www.seek.com.au"
    search_url = "https://seek.com.au/data-science-jobs"
    keywords = ['R', 'Python', 'SQL', 'C', 'Java', 'C++', 'Spark', 'Hadoop',
                'C#', 'Tableau', 'Power BI', 'AWS', 'Azure', 'Scala', 'MATLAB',
                'Pig', 'Hive', 'Impala', 'Teradata', 'Oracle', 'SAS', 'MongoDB', 
                'Redshift', 'S3', 'EC2', 'Lambda', 'EMR', 'SageMaker', 'DynamoDB', 
                'Cloudformation', 'Athena', 'Kinesis', 'Cassandra', 'Alteryx', 
                'Jupyter', 'Clickhouse','PyTorch', 'TensorFlow']
    
    total_kw = dict.fromkeys(keywords, 0)
    
    #Perform search
    urls = get_job_urls(search_url, limit = 100)
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
    
    #Print the list of keywords, sorted by frequency
    kw_freq = [(v,k) for k,v in total_kw.items()]
    kw_freq.sort(reverse=True)
    for k,v in kw_freq:
        print(f"{k}: {v}")
    return total_kw
    
if __name__ == "__main__":
    main()