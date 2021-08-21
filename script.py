from job_card import JobCard
from bs4 import BeautifulSoup
import requests
from database import insert_job_card

site = 'https://ca.indeed.com/jobs?q=part-time%20summer&l=scarborough,+ON&jt=part-time&fromage=3'
page2, page3 = '', ''

html_text = requests.get(site)
soup = BeautifulSoup(html_text.text, 'html.parser')
job_titles= soup.find('div', id='mosaic-provider-jobcards')

def get_job_card_info(job):
    job_page = requests.get(job)
    job_soup = BeautifulSoup(job_page.text, 'html.parser')
    title, location, company, type, description = '', '', '', '', ''
    title = job_soup.find('h1', class_='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title').text
    loc = job_soup.find('div', class_='icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle')
    
    for div in loc.children:
        if not div.has_attr('class'):
            location = div.text

    company = job_soup.find('div', class_='icl-u-lg-mr--sm icl-u-xs-mr--xs').text
    type_spans = job_soup.find('div', class_='jobsearch-JobMetadataHeader-item')
    description = get_job_description(job_soup=job_soup)
    
    if type_spans != None:
        for span in type_spans.children:
            if span.name == 'span':
                type += span.text

    return JobCard(title=title, location=location, company=company, type=type, description=description)

jobs = []

def get_job_description(job_soup):
    description = ''
    div = job_soup.find('div', id='jobDescriptionText')
    for p in div.children:
        if p.name == 'p':
            description += p.text
    return description

for a in job_titles.children:
    if a.name == 'a':
        jobs.append(get_job_card_info('https://ca.indeed.com' + a['href']))

# pages = soup.findAll('a')
# for page in pages:
#     if page.has_attr('data-pp'):
#         if page.span.text != '':
#             new_page = requests.get('https://ca.indeed.com{}'.format(page.span.text, page.get('href')))
#             new_soup = BeautifulSoup(new_page.text, 'html.parser')
#             new_titles = new_soup.find('div', id='mosaic-provider-jobcards')
#             for link in new_titles.children:
#                 if link.name == 'a':
#                     jobs.append(get_job_card_info('https://ca.indeed.com' + link['href']))
#             print('{} https://ca.indeed.com{}'.format(page.span.text, page.get('href')))
            
for job in jobs:
    print(job.title)
    print(job.location)
    print(job.company)
    print(job.type)
    print(job.description)
    print('----------------------\n------------------------\n')
    insert_job_card(job=job)



