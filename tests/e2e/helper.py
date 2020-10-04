from typing import List

import os


def get_file_paths_and_imdb_ids(directory_name: str) -> zip:
	"""directory_name should be cli or TBD"""
	file_paths = []
	imdb_ids = []

	current_directory = os.path.dirname(__file__)
	path = f'{current_directory}{os.sep}json{os.sep}{directory_name}'
	for root, dirs, files in os.walk(path):
		for name in files:
			file_paths.append(os.path.join(root, name))
			imdb_ids.append(name.split('.')[0])

	return zip(file_paths, imdb_ids)
