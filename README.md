# Job Scraper

This project scrapes job listings from:
- [Youthall](https://www.youthall.com/en/jobs/)
- [Toptalent](https://toptalent.co/is-ilanlari)

## Features
- Scrapes job title, company, location, and job link.
- Saves results as CSV.
- Modular design for adding new scrapers.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Output will be saved as `jobs.csv`.

## Adding New Scrapers
- Add a new Python file in the `scrapers/` directory.
- Implement a `scrape_jobs()` function that returns a list of job dicts.
- Import and call your function in `main.py`. 