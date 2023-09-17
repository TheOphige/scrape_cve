install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv *.py

format:	
	black *.py 

lint:
	pylint --disable=R,C,E1120,W0621 --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py  mylib/*.py

refactor: format lint

run:
	cd cve/cve/spiders/ &&\
		scrapy crawl scrape_cve
		
all: install run