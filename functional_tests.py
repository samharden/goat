import selenium
from selenium import webdriver

browser = webdriver.Chrome("/Library/Python/chromedriver")
browser.get('http://localhost:8000')
assert 'Django' in browser.title
