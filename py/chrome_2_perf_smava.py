"""
Selenium Grid with Hub and Node test
"""
import os
import platform
from selenium import webdriver
from timingsclient import Perf

BROWSER = webdriver.Chrome(
    '/usr/local/bin/chromedriver')
#BROWSER.get('https://www.smava.de/kreditanfrage/kreditantrag.html?route=V1')
#BROWSER.get('https://www.smava.de/landing/kfzrechner')
BROWSER.get('https://www.smava.de/landing/kfzrechner?embed&placementId=1847502766&ref=9875f8f0&amount=52490&category=1&channel=desktop&data1=4&duration=84&initialPayment=0&subaffiliateid=4&vehicleBrand=Audi&vehicleKm=9625&vehicleModel=A4&vehiclePowerKw=200&vehiclePrice=52490&vehicleRegistrationYear=2016')

try:
    BROWSER.find_element_by_class_name('section__heading')
    print("FUNCTIONAL: Page looks good!")
except:
    print("FUNCTIONAL: Page sucks!")

# Setup custom config for PERF
CONFIG_FILE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    '', 'config_smava.yaml')
PERF = Perf(CONFIG_FILE)
INJECT_CODE = PERF.injectjs('navtiming')
API_PARAMS = PERF.getapiparams(es_create=True, log={
    'browser': BROWSER.name, 'env_tester': platform.system()})

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
