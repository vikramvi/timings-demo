"""
Selenium Grid with Hub and Node test
"""
import os
import platform
from selenium import webdriver
from timingsclient import Perf

# Setup custom config for PERF
CONFIG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), '', 'config.yaml')
# Initiate client
PERF = Perf(CONFIG_FILE)

# Get inject code from API
INJECT_CODE = PERF.injectjs(inject_type="usertiming", mark="visual_complete", strip_qs=True)

BROWSER = webdriver.Firefox(executable_path=r'/Users/mverkerk/selenium/geckodriver.exe')

# Get parameters for API call with custom values
API_PARAMS = PERF.getapiparams(es_create=False, log={
    'browser': BROWSER.name, 'env_tester': platform.system()})

BROWSER.get('https://reactjs.org/')

try:
    BROWSER.find_element_by_id('examples')
    print("FUNCTIONAL: Page looks good!")
except:
    print("FUNCTIONAL: Page not working!")

BROWSER.execute_script('window.performance.mark("demo_start")')     # Set User Timing "start" mark
BROWSER.find_element_by_link_text('Tutorial').click()
# BROWSER.find_element_by_css_selector('#prerequisites')
BROWSER.execute_script('window.performance.mark("demo_stop")')     # Set User Timing "stop" mark

if INJECT_CODE is not False:
    # Get perf data from browser object
    TIMING = BROWSER.execute_script(INJECT_CODE)     # Inject JS code into browser object
    # Send perf data with parameters to API
    API_RESP = PERF.usertiming(TIMING, API_PARAMS)     # Send perf data to API

    # Assert perf result
    if API_RESP is not False:
        # Check the API's response - has the assert field!
        print(
            'PERFORMANCE of [' + API_RESP["export"]["dl"] + '] was ',
            ('GOOD' if API_RESP['assert'] is True else "BAD") + '! - ',
            str(API_RESP['export']['perf']['measured']),
            '/ ' + str(API_RESP['export']['perf']['threshold'])
        )
    else:
        print("API_RESP problem!")
else:
    print("INJECT_CODE problem!")

BROWSER.close()
