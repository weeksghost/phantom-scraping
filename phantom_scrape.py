#!/usr/bin/python

import bs4
import requests
from selenium import webdriver

driver = webdriver.PhantomJS('phantomjs')
root_url = 'http://www.brooklyndelta.com'
browser = driver.get(root_url)
content = driver.page_source
soup = bs4.BeautifulSoup(content)
links = [a.attrs.get('href') for a in soup.find_all('a')]
for paths in links:
    urls = paths
    try:
        response = requests.get(urls)
        if ('http://' or 'https://' not in urls):
            new_url = '%s%s' % (root_url, urls)
            print new_url
        elif response.status_code != 200:
            print '[%s] %s' % (response.status_code, urls)
    except:
        print urls
        #pass
driver.close()
