#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

with open('test_requirements.txt') as test_requirements_file:
    test_requirements = test_requirements_file.read()

setup(
    author="Joe Turner",
    author_email='joe.turner@live.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="scrapes imdb data for tv series",
    entry_points={
        'console_scripts': [
            'imdb_tv_scraper=imdb_tv_scraper.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme ,
    include_package_data=True,
    keywords='imdb_tv_scraper',
    name='imdb_tv_scraper',
    packages=find_packages(include=['imdb_tv_scraper', 'imdb_tv_scraper.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jet76/imdb_tv_scraper',
    version='0.1.0',
    zip_safe=False,
)
