import requests
import logging
from imdb_tv_scraper import TVScraper
logger = logging.getLogger(__name__)

def test_get_html_success():
	url = 'https://www.imdb.com/title/tt0412142'
	html = TVScraper._get_html(url=url)
	assert html

def test_get_html_not_found():
	url = 'https://www.imdb.com/title/123'
	html = TVScraper._get_html(url=url)
	assert html is None

def test_get_html_bad_schema():
	"""
	Gracefully fail on bad schema
	"""
	url = 'https://bad.url'
	html = TVScraper._get_html(url=url)
	assert html is None

def test_scrape_imdb_id_success():
	imdb_id = 'tt0412142'
	series_data = TVScraper.scrape_imdb_id(imdb_id=imdb_id)
	assert type(series_data) is dict
	assert series_data['title']
	assert series_data['seasons']
	for season in series_data['seasons']:
		assert season
		for episode in season:
			assert episode['title']
			assert type(episode['title']) is str
			assert episode['rating']
			assert type(episode['rating']) is float

def test_scrape_imdb_id_bad_id():
	imdb_id = ''
	series_data = TVScraper.scrape_imdb_id(imdb_id=imdb_id)
	assert series_data is None
