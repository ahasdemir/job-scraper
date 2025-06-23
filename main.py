import pandas as pd
from scrapers.youthall import scrape_jobs as scrape_youthall
from scrapers.toptalent import scrape_jobs as scrape_toptalent

def main():
    jobs = []
    print('Scraping Youthall...')
    jobs.extend(scrape_youthall())
    print('Scraping Toptalent...')
    jobs.extend(scrape_toptalent())
    print(f'Total jobs scraped: {len(jobs)}')
    df = pd.DataFrame(jobs)
    # Ensure 'source' is always a column, even if some jobs are missing it
    if 'source' not in df.columns:
        df['source'] = ''
    df.to_csv('jobs.csv', index=False, columns=['title', 'company', 'location', 'link', 'source'])
    print('Saved to jobs.csv')

if __name__ == '__main__':
    main() 