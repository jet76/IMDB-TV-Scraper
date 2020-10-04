import pytest

from imdb_tv_scraper import TVScraper
from tests.unit import helper

def test_create_series_url():
	imdb_id = 'garbage'
	
	url = TVScraper._create_series_url(imdb_id=imdb_id)
	assert url == f'https://www.imdb.com/title/{imdb_id}'

def test_create_season_url():
	imdb_id = 'garbage'
	series_url = f'https://www.imdb.com/title/{imdb_id}'
	season_number = '666'
	
	url = TVScraper._create_season_url(series_url=series_url, season_number=season_number)
	assert url == f'{series_url}/episodes?season={season_number}'

@pytest.mark.parametrize('path', helper.get_file_paths(directory_name='series'))
def test_scrape_series_success(path):
	with open(path) as f:
		html = f.read()
	
	data = TVScraper._scrape_series(html=html)
	assert data['title']
	assert type(data['title']) is str

	assert data['seasons']
	assert type(data['seasons']) is int

def test_scrape_series_failure():
	
	data = TVScraper._scrape_series(html=None)

	assert data is None

@pytest.mark.parametrize('path', helper.get_file_paths(directory_name='season'))
def test_scrape_season_success(path):
	with open(path) as f:
		html = f.read()

	season_data = TVScraper._scrape_season(html=html)

	for episode in season_data:
		assert episode['title']
		assert type(episode['title']) is str

		assert episode['rating']
		assert type(episode['rating']) is float

def test_scrape_season_failure():
	season_data = TVScraper._scrape_season(html=None)
	assert season_data == []
