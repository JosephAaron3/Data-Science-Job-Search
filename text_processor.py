

def clean_text(text_list):
    #Remove text from bottom tab
    tab_start = text_list.index('Job search')
    if len(text_list)-tab_start != 60:
        print("Warning - Possibly removing info")
    text_list = text_list[:tab_start]
    
    #Remove unformated symbols
    bad_format = [('\\xe2\\x80\\x99',"'"),('\\xe2\\x80\\x9c', '"'), ('\\xe2\\x80\\x9d', '"'), 
                  ('\\xc2\\xa0', ' '), ('\\xc2\\xa0', ' ')]
    alt_text = ' '.join(text_list)
    for cur, new in bad_format:
        alt_text = alt_text.replace(cur, new)
    return alt_text
    
def text_search(text, keywords):
    kw_count = dict.fromkeys(keywords, False)
    for base in keywords:
        #Create alternate forms of the base word
        if len(base) == 1: #Handle things like R and C
            forms = [' '+base+' ', ' '+base+',', ','+base+',', 
                     '/'+base+'/', '/'+base+' ', ' '+base+'/']
        else:
            forms = [base, base.lower()]
        if any(word in text for word in forms):
            kw_count[base] = True
    return kw_count
            

def main():
    EXAMPLE = ['About us', 'Scalene Group is a fast-growing, specialist retail advisory and analytics business. We provide strategy, process design and analytics services to help retailers optimise their performance and leverage data in day-to-day decision-making.\\xc2\\xa0', 'We deliver tailored solutions for our clients that turn complex data into high value, easy to implement solutions. We operate from our offices in Melbourne, Sydney and London to support a growing number of leading retailers in Australia, Asia and Europe.\\xc2\\xa0', "Scalene Group has an ambitious growth agenda and we\\'re keen to expand our team with highly skilled and passionate individuals to help us deliver this.", 'Qualifications & experience', '3-5 years experience in a data analyst / reporting analyst or data scientist role, ideally with a Retailer/FMCG', 'Exceptional analytical and insight skills, comfortable in dealing with large datasets', 'Hands-on experience in coding and analysis using R / Python, SQL', 'Experience with one or more from Power BI, Azure ML, Shiny is preferred', 'Able to work with loosely defined problems, handle ambiguity well', 'Experience in data cleansing, validation and preparation steps \\xc2\\xa0', 'Have practical and output oriented mindset', 'Flexible and adaptable approach applied to all activities', 'Tasks & responsibilities', 'As a Data Scientist you will contribute to the growth of Scalene by supporting successful delivery of client work as a key member of project delivery teams and by helping to develop and implement internal strategic initiatives.\\xc2\\xa0', 'Your responsibilities include:', 'Prepare and analyse datasets and generate insights to help bring clients along the \\xe2\\x80\\x9cproject journey\\xe2\\x80\\x9d', 'Build self service reports, dashboards and web applications', 'Develop and deploy statistical models', 'Convert data and analysis outputs into effective, clear communication documents appealing to a wide range of stakeholders', 'Capture and document client requirements, and then translate them into an analytical roadmap / initiative', 'Help identify opportunities with potential to drive value both for our clients and Scalene going forward', 'Propose, develop and lead streams of work to support Scalene\\xe2\\x80\\x99s internal development agenda', 'Benefits', 'Flexible working options including work from home', 'Strong focus on team training and development', 'Generous annual leave', 'Opportunity to shape and drive the development of an innovative fast-growing business', '\\xc2\\xa0', 'Which of the following statements best describes your right to work in Australia?', "How many years' experience do you have as a data scientist?", 'Which of the following programming languages are you experienced in?', 'Which of the following data analytics tools are you experienced with?', 'Have you worked in a role which requires experience with statistical modelling?', 'Job search', 'Profile', 'Recommended jobs', 'Saved searches', 'Saved jobs', 'Applied jobs', 'Career Advice', 'Explore Careers', 'Company reviews', 'Download apps', 'iOS', 'Android', 'SEEK sites', 'Employer site', 'SEEK NZ', 'Courses', 'Business for sale', 'Volunteering', 'About SEEK', 'Newsroom', 'Investors', 'International partners', 'Bdjobs', 'BrighterMonday', 'Catho', 'Jobberman', 'jobsDB', 'JobStreet', 'Jora', 'OCC Mundial', 'Workana', 'Zhaopin', 'Jora', 'Partner services', 'Certsy', 'GradConnection', 'Jora Local', 'Sidekicker', 'GO1', 'FutureLearn', 'Employment Hero', 'JobAdder', 'Help centre', 'Contact us', 'Work for SEEK', 'Product & Tech Blog', 'SEEK videos', 'Social', 'Facebook', 'Instagram', 'Twitter', 'YouTube', 'Register for free', 'Post a job ad', 'Products & prices', 'Customer service', 'Hiring Advice', 'Market Insights', 'Recruitment software partners', '\\xc2\\xa9 SEEK. All rights reserved.']
    keywords = ['R', 'Python', 'SQL', 'C']
    text = clean_text(EXAMPLE)
    freq = text_search(text, keywords)
    print(freq)
    
if __name__ == "__main__":
    main()