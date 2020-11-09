import seeksearch as ss

search_url = "https://seek.com.au/data-science-jobs"
kw = ['R', 'Python', 'SQL', 'C', 'Java', 'C++', 'Spark', 'Hadoop',
            'C#', 'Tableau', 'Power BI', 'AWS', 'Azure', 'Scala', 'MATLAB',
            'Pig', 'Hive', 'Impala', 'Teradata', 'Oracle', 'SAS', 'MongoDB', 
            'Redshift', 'S3', 'EC2', 'Lambda', 'EMR', 'SageMaker', 'DynamoDB', 
            'Cloudformation', 'Athena', 'Kinesis', 'Cassandra', 'Alteryx', 
            'Jupyter', 'Clickhouse','PyTorch', 'TensorFlow']
lim = 100

results = ss.search(search_url, kw, lim)