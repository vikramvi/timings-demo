"""
Simple test to demonstrate Selenium
"""
from selenium import webdriver

BROWSER = webdriver.Chrome('/Users/mverkerk/selenium/chromedriver_2.34.exe')
BROWSER.get('http://www.seleniumconf.de')

try:
    BROWSER.find_element_by_class_name('section__heading')
    print("FUNCTIONAL: Page looks good!")
except:
    print("FUNCTIONAL: Page not working!")

BROWSER.close()
