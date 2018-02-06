import os
import platform
import sys

from selenium import webdriver
from timingsclient import Perf

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ChromeOptions

#Jenkins Chrome Browser Fix
#from pyvirtualdisplay import Display
#display = Display(visible=0, size=(800, 800))  
#display.start()
#BROWSER = webdriver.Chrome()

#BROWSER = webdriver.Chrome('/usr/local/bin/chromedriver')

chromedriver = '/usr/local/bin/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver
BROWSER = RemoteWebDriver(
    command_executor= sys.argv[1] +'/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

urlValue = "https://www.finanzcheck.de/"
BROWSER.get(urlValue)


try:
    BROWSER.find_element_by_xpath('//div/a/img[contains(@alt, "FINANZCHECK")]')
    print("FUNCTIONAL: Page looks good!")
except:
    print("FUNCTIONAL: Page sucks!")

# Setup custom config for PERF
CONFIG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)),'', 'config_finanzcheckHomePage.yaml')
PERF = Perf(CONFIG_FILE)
INJECT_CODE = PERF.injectjs('navtiming')

API_PARAMS = PERF.getapiparams(es_create=True, log={'browser': BROWSER.name, 'env_tester': platform.system()})

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
