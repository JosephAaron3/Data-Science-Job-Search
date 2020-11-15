import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import seeksearch as ss
from tqdm import tqdm

search_url = "https://seek.com.au/data-science-jobs"
kw = ['R', 'Python', 'SQL', 'C', 'Java', 'C++', 'Spark', 'Hadoop',
            'C#', 'Tableau', 'Power BI', 'AWS', 'Azure', 'Scala', 'MATLAB',
            'Pig', 'Hive', 'Impala', 'Teradata', 'Oracle', 'SAS', 'MongoDB', 
            'Redshift', 'S3', 'EC2', 'Lambda', 'EMR', 'SageMaker', 'DynamoDB', 
            'Cloudformation', 'Athena', 'Kinesis', 'Cassandra', 'Alteryx', 
            'Jupyter', 'Clickhouse','PyTorch', 'TensorFlow', 'PowerBI']
lim = int(22*4.5)

results = ss.search(search_url, kw, lim)