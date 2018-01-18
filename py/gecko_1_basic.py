"""
Simple test to demonstrate Selenium
"""
from selenium import webdriver

BROWSER = webdriver.Firefox(
    executable_path=r'/Users/mverkerk/selenium/geckodriver.exe')
BROWSER.get('http://www.seleniumconf.de')

try:
    BROWSER.find_element_by_class_name('section__heading')
    print("FUNCTIONAL: Page looks good!")
except:
    print("FUNCTIONAL: Page working!")

BROWSER.close()
