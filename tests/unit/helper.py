from typing import List

import os


def get_file_paths(directory_name: str) -> List[str]:
	"""directory_name should be series or season"""
	file_paths = []

	current_directory = os.path.dirname(__file__)
	path = f'{current_directory}{os.sep}html{os.sep}{directory_name}'
	for root, dirs, files in os.walk(path):
		for name in files:
			file_paths.append(os.path.join(root, name))

	return file_paths
