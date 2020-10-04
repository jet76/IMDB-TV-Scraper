"""
Example:
python scripts/save_html.py https://www.imdb.com/title/tt0412142 tests/unit/html/series/house.html
"""

import requests
import sys

def get_html(url: str) -> str:
	response = requests.get(url)
	assert response.ok
	return response.text

def save_html(html: str, path: str):
	with open(path, 'w') as f:
		f.write(html)

if __name__ == '__main__':
	url = sys.argv[1]
	path = sys.argv[2]
	
	html = get_html(url=url)
	save_html(html=html, path=path)
