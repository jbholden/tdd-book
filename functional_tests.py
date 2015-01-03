from selenium import webdriver

browser = webdriver.Firefox()
#browser = webdriver.Safari()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
