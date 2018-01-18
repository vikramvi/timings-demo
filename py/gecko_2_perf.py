"""
Selenium Grid with Hub and Node test
"""
import os
import platform
from selenium import webdriver
from timingsclient import Perf

BROWSER = webdriver.Firefox(
    executable_path=r'/Users/mverkerk/selenium/geckodriver.exe')
BROWSER.get('http://www.seleniumconf.de')

try:
    BROWSER.find_element_by_class_name('section__heading')
    print("FUNCTIONAL: Page looks good!")
except:
    print("FUNCTIONAL: Page working!")

# Setup custom config for PERF
CONFIG_FILE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    '', 'config.yaml')
PERF = Perf(CONFIG_FILE)
INJECT_CODE = PERF.injectjs('navtiming')
API_PARAMS = PERF.getapiparams(es_create=False, log={
    'browser': BROWSER.name, 'env_tester': platform.system()})

if INJECT_CODE is not False:
    TIMING = BROWSER.execute_script(INJECT_CODE)
    NAV_RESP = PERF.navtiming(TIMING, API_PARAMS)

    if 'assert' in NAV_RESP:
        print(
            'PERFORMANCE was',
            ('GOOD' if NAV_RESP['assert'] is True else "BAD") + '! - ',
            str(NAV_RESP['export']['act_pageLoadTime']),
            '/ ' + str(NAV_RESP['export']['sla_pageLoadTime'])
        )
    else:
        print('Error - ', NAV_RESP)

BROWSER.close()
