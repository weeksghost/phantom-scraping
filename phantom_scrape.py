#!/usr/bin/python

import bs4
import requests
from urlparse import urlparse
from selenium import webdriver

driver = webdriver.PhantomJS('phantomjs')
root_url = 'http://brooklyndelta.com'
browser = driver.get(root_url)
content = driver.page_source
soup = bs4.BeautifulSoup(content)
links = [a.attrs.get('href') for a in soup.find_all('a')]
for paths in links:
    urls = paths
    try:
        response = requests.get(urls)
        if response.status_code != 200:
            print '[%s] %s' % (response.status_code, urls)
        elif root_url not in urls:
            resp = requests.get(urls)
            if resp.status_code != 200:
                print '[%s] %s' % (resp.status_code, urls)
    except:
        new_url = '%s%s' % (root_url, urls)
        r = requests.get(new_url)
        if r.status_code != 200:
            print '[%s] %s' % (r.status_code, new_url)
driver.close()
