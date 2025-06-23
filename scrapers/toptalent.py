import requests
from bs4 import BeautifulSoup


def scrape_jobs():
    base_url = 'https://toptalent.co'
    search_url = base_url + '/Job/SearchJob'
    jobs = []
    page_number = 1
    page_size = 9  # Default page size from the JS
    is_card_view = True
    while True:
        payload = {
            'pageSize': page_size,
            'pageNumber': page_number,
            'isCardView': is_card_view,
            'SearchKey': '',
            'DepartmentIds': [],
            'CityIds': [],
            'PositionLevelIds': [],
            'OrderBy': 'newests',
            'FilterTags': [],
            'DepartmentSeo': None,
            'CitySeo': None
        }
        response = requests.post(search_url, json=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_cards = soup.select('a.position')
        if not job_cards:
            break
        for job_card in job_cards:
            link = job_card.get('href', '')
            if link and link.startswith('/'):
                link = base_url + link
            else:
                link = base_url + '/is-ilanlari'
            media_body = job_card.select_one('div.media-body')
            if media_body:
                title_div = media_body.select_one('div.text-truncate.ff-pnova-b.f-16')
                company_divs = media_body.select('div.text-truncate')
                # The first is title, the second is company
                if len(company_divs) > 1:
                    company_div = company_divs[1]
                else:
                    company_div = None
                location_span = media_body.select_one('span.text-grey-l')
            else:
                title_div = company_div = location_span = None
            jobs.append({
                'title': title_div.get_text(strip=True) if title_div else '',
                'company': company_div.get_text(strip=True) if company_div else '',
                'location': location_span.get_text(strip=True) if location_span else '',
                'link': link,
                'source': 'toptalent'
            })
        page_number += 1
    return jobs 