import scrapy
import os
from os.path import dirname

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, 'source-EXPLOIT-DB.html')
top_dir = dirname(dirname(dirname(current_dir)))
sql_file = os.path.join(top_dir, 'sql_scripts/populate.sql')

class ScrapeCveSpider(scrapy.Spider):
    name = "scrape_cve"
    allowed_domains = ['cve.mitre.org']
    # Starting with actual URLs is fine
    #start_urls = ['http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html']
    # But you can use files as well!
    start_urls = [f"file://{url}"]

    def parse(self, response):
        table = None
        count = 0
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 100:
                table = child
        for row in table.xpath('//tr'):
            if count > 100:
                break
            cve_list = []
            try:
                # This captures 1 CVE only, but you may have many
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()
                print(f"exploit id: {exploit_id} -> {cve_id}")
                append_sql_file(exploit_id, cve_id)
#               # This is one way of doing that
#                for text in row.xpath('td//text()'):
#                    if text.extract().startswith('CVE'):
#                        cve_list.append(text.extract())
#                print(f"exploit id: {exploit_id} -> {cve_list}")
            except Exception as err:
                print(f"skipping due to: {err}")
            count += 1


def append_sql_file(exploit_id, cves):
    line = f"INSERT INTO cve(exploit_id, cve_id) VALUES ('{exploit_id}', '{str(cves)}');\n"
    if not os.path.exists(sql_file):
        with open(sql_file, 'w') as _f:
            _f.write(line)
        return
    with open(sql_file, 'a') as _f:
        _f.write(line)