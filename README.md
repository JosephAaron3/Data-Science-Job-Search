# Data science job search
A webscraper/processor for finding the most common job skills from Seek job ads

## Files
*job_url_ws.py* - Webscraper for getting urls from a base search (e.g. all urls from all pages of the search "Data scientist" on Seek).

*job_info_ws.py* - For a job's given url, extract the text in the job description area.

*text_processor.py* - Clean up a given list of text entries and search for key terms

*main.py* - Using the above modules, find the highest frequency words (from a user-defined list) from a base search

## To do
- Display/filter job names to ensure the right ads are being scraped
- Develop a good default keyword list
- Make tests for keyword detection sensitivity (especially for one-letter keywords e.g. R and C)