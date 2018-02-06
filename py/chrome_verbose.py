"""
Selenium Grid with Hub and Node test
"""
import os
import datetime
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from timingsclient import Perf

# Setup custom config
CONFIG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), '', 'config.yaml')

# Initiate the client
PERF = Perf(CONFIG_FILE)

# Get/Set parameters for the navtiming call
API_PARAMS = PERF.getapiparams(
    days=15,
    es_trace=True,
    log=dict(something="crazy"))

# Get inject code from the perf API
INJECT_CODE = PERF.injectjs('navtiming', 'visual_complete', True)

# # Setup Selenium webdriver
BROWSER = webdriver.Chrome("/Users/mverkerk/selenium/chromedriver_2.34.exe")
WAIT = WebDriverWait(BROWSER, 10)
BROWSER.implicitly_wait(10)

# Get web page and take initial screenshot
print('start nav - Opening page ...')
START = datetime.datetime.now()

# Get web page, sleep for 5 seconds and close BROWSER
BROWSER.get('http://seleniumconf.de/')
ELEMENT = WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, 'hero')))

print('{0} - Browser onload complete ...'.format(
    str((datetime.datetime.now() - START).total_seconds())
))
BROWSER.get_screenshot_as_file(
    os.path.dirname(__file__) + '/screens/demo-perf-api_before.png')

# Wait for visual complete
print('{0} - Waiting for visual complete ...'.format(
    str((datetime.datetime.now() - START).total_seconds())
))

try:
    ELEMENT = WebDriverWait(BROWSER, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "section__heading"))
    )

finally:

    # Visual element found -> immediately set a 'mark' in the BROWSER
    print('{0} - Setting visual complete mark ...'.format(
        str((datetime.datetime.now() - START).total_seconds())
    ))
    BROWSER.execute_script('window.performance.mark("visual_complete");')
    BROWSER.get_screenshot_as_file(
        os.path.dirname(__file__) + '/screens/demo-perf-api_after.png')

    # get performance data from BROWSER
    print('{0} - Collecting perf data from BROWSER ...'.format(
        str((datetime.datetime.now() - START).total_seconds())
    ))

    if INJECT_CODE is not False:
        TIMING = BROWSER.execute_script(INJECT_CODE)

        # call navtiming API
        print('{0} - Calling navtiming API ...'.format(
            str((datetime.datetime.now() - START).total_seconds())
        ))
        NAV_RESP = PERF.navtiming(TIMING, API_PARAMS)

        if NAV_RESP is not False:

            # Print the API's response
            print('{0} - Here is the API response:\n\n{1}'.format(
                str((datetime.datetime.now() - START).total_seconds()),
                json.dumps(NAV_RESP['export']['perf'], indent=4)))

            # assert perf
            if 'assert' in NAV_RESP and NAV_RESP['assert'] is True:
                print('{0} - PERF IS LOOKING GOOD! Your pageload time was: {1}'.format(
                    str((datetime.datetime.now() - START).total_seconds()),
                    str(NAV_RESP['export']['perf']['measured']) + ' [ms]'))
            else:
                print('{0} - PERF FAILED! Your pageload time was: {1}'.format(
                    str((datetime.datetime.now() - START).total_seconds()),
                    str(NAV_RESP['export']['perf']['measured']) + ' [ms]'))

    BROWSER.quit()
