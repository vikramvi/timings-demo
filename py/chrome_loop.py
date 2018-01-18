"""
Selenium Grid with Hub and Node test
"""
import os
import time
from itertools import repeat
from selenium import webdriver
from timingsclient import Perf

# Setup custom config
CONFIG_FILE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    '', 'config.yaml')

PERF = Perf(CONFIG_FILE)

INJECT_CODE = PERF.injectjs('navtiming')
API_PARAMS = PERF.getapiparams(es_create=True, days=14)

def run():
    BROWSER = webdriver.Chrome(
        '/Users/mverkerk/selenium/chromedriver.exe')
    BROWSER.get('http://www.seleniumconf.de')
    time.sleep(2)

    try:
        BROWSER.find_element_by_class_name('section__heading')
        print("FUNCTIONAL: Page looks good!")
    except:
        print("FUNCTIONAL: Page not working!")

    if INJECT_CODE is not False:
        TIMING = BROWSER.execute_script(INJECT_CODE)
        NAV_RESP = PERF.navtiming(TIMING, API_PARAMS)

        if NAV_RESP is not False:
            print(
                'PERFORMANCE was',
                ('GOOD' if NAV_RESP['assert'] is True else "BAD") + '! - ',
                str(NAV_RESP['export']['perf']['measured']),
                '/ ' + str(NAV_RESP['export']['perf']['threshold'])
            )

    BROWSER.close()

for i in repeat(None, 50):
    run()
    time.sleep(3)

print('All done!')
