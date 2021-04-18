# Seek search
A webscraper/processor for finding the most common tools/skills from Seek job ads.  
Made for searching data science jobs.

## Files
*_job_url_ws.py* - Webscraper for getting urls from a base search (e.g. all urls from all pages of the search "Data scientist" on Seek).

*_job_info_ws.py* - For a job's given url, extract the text in the job description area.

*text_processor.py* - Clean up a given list of text entries and search for key terms

*search.py* - Using the above modules, find the highest frequency words (from a user-defined list) from a base search

## To do
- ~~Display/filter job names to ensure the right ads are being scraped~~
- ~~Develop a good default keyword list~~
- Make tests for keyword detection sensitivity (especially for one-letter keywords e.g. R and C)
- Search for things other than keywords (e.g. common soft skills)
- ~~Change scraper package to beautiful soup~~

## Sample output
![Keyword frequency graph](/Frequency_plot2.png)

As expected, this seems to follow a Pareto distribution

472: SQL  
436: Python  
248: AWS  
215: Java  
178: Scala  
175: Azure  
174: R  
132: Spark  
119: Tableau  
105: Power BI  
104: SAS  
80: Hadoop  
63: C#  
59: Oracle  
56: Hive  
56: C++  
56: C  
55: S3  
49: Redshift  
34: Lambda  
28: EMR  
27: EC2  
25: Athena  
20: Teradata  
19: MongoDB  
18: Alteryx  
16: MATLAB  
15: TensorFlow  
15: Cassandra  
14: Jupyter  
14: DynamoDB  
13: Kinesis  
11: PyTorch  
10: Pig  
10: Impala  
8: Cloudformation  
6: SageMaker  
1: Clickhouse
