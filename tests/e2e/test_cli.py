import json

from click.testing import CliRunner

import pytest

from imdb_tv_scraper.cli import main
from tests.e2e import helper


@pytest.mark.parametrize('path_and_id', helper.get_file_paths_and_imdb_ids(directory_name='cli'))
def test_main(path_and_id):
	path, imdb_id = path_and_id
	with open(path) as f:
		expected_output = json.load(f)
	
	runner = CliRunner()
	result = runner.invoke(main, [imdb_id])
	assert result.exit_code == 0
	assert result.output
