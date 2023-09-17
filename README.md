# scrape_cve
This project scrapes data and inserts it in mysql database for processing..


## Steps
Install _requirements.txt_ in a virtual environment

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Start scrapy project

```
$ scrapy startproject cve
$ scrapy genspider exploit cve.mitre.org
```

Download website locally with

```
wget https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html
```

Scrape with

```
cd cve/cve/spiders/
scrapy crawl scrape_cve
```

Set up MySQL database

```
run setup.sql
```

Populate database with scraped data

```
run populate.sql
```

Created single script for populating database

```
mysqldump -u root -p cve > export.sql 
```

Single script for populating database

```
run export.sql 
```