import requests
from bs4 import BeautifulSoup

def scrape_jobs_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    jobs = []
    for job_card in soup.select('.c-job-vertical'):
        a_tag = job_card.find('a', href=True)
        link = a_tag['href'] if a_tag else ''
        # If the link is relative, prepend the domain
        if link and link.startswith('/'):
            link = 'https://www.youthall.com' + link
        title = job_card.select_one('.c-job-vertical__text-area__company-info h5')
        company = job_card.select_one('.c-job-vertical__text-area__company-info small')
        jobs.append({
            'title': title.get_text(strip=True) if title else '',
            'company': company.get_text(strip=True) if company else '',
            'location': '',
            'link': link
        })
    return jobs

def scrape_jobs():
    url = 'https://www.youthall.com/en/jobs/'
    jobs = []
    page = 1
    while True:
        response = requests.get(url + f'?page={page}')
        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.select('.c-job-vertical')
        if not job_cards:
            break
        for job_card in job_cards:
            a_tag = job_card.find('a', href=True)
            link = a_tag['href'] if a_tag else ''
            if link and link.startswith('/'):
                link = 'https://www.youthall.com' + link
            title = job_card.select_one('.c-job-vertical__text-area__company-info h5')
            company = job_card.select_one('.c-job-vertical__text-area__company-info small')
            jobs.append({
                'title': title.get_text(strip=True) if title else '',
                'company': company.get_text(strip=True) if company else '',
                'location': '',
                'link': link,
                'source': 'youthall'
            })
        page += 1
    return jobs 