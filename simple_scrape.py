#!/usr/bin/python

import bs4
import requests
from selenium import webdriver

driver = webdriver.PhantomJS('phantomjs')
url = 'http://www.snapdeal.com/'
browser = driver.get(url)
content = driver.page_source
soup = bs4.BeautifulSoup(content)
links = [a.attrs.get('href') for a in soup.find_all('a')]
for paths in links:
    print paths
driver.close()
