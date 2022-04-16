import inspect
import os
import sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import seeksearch as ss

search_url = "https://seek.com.au/data-science-jobs"
kw = ['R', 'Python', 'SQL', 'Java', 'Scala', 'MATLAB', 'C', 'C#', 'C++',  # Programming languages
      'Linux', 'Unix',  # OS
      'Apache', 'Spark', 'Hadoop', 'Spark', 'Pig', 'Hive', 'Impala', 'HBase', 'Storm', 'Kafka',  # Apache
      'Sqoop', 'Airflow', 'Air flow', 'Zookeeper', 'Zoo keeper',
      'GCP', 'AWS', 'Azure', 'Google cloud', 'Amazon Web',  # Cloud platforms
      'Tableau', 'Power BI', 'PowerBI', 'Qlik',  # Business intelligence
      'Kubernetes', 'Docker',  # Containerization
      'RapidMiner', 'BigML', 'Databricks', 'Data bricks',  # DS/ML platforms
      'TensorFlow', 'PyTorch', 'Keras', 'Scikit',  # ML libraries
      'Teradata', 'Oracle', 'SAS', 'SPSS', 'MongoDB',  # Other
      'Redshift', 'S3', 'EC2', 'Lambda', 'EMR', 'SageMaker', 'DynamoDB',
      'Cloudformation', 'Athena', 'Kinesis', 'Cassandra', 'Alteryx', 'Anaconda',
      'Jupyter', 'Clickhouse', 'Excel', 'H2O', 'DataRobot', 'git']
lim = int(200)

results = ss.search(search_url, kw, lim)
