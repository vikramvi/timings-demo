"""
Selenium Grid with Hub and Node test
"""
import os
import platform
from selenium import webdriver
from timingsclient import Perf

BROWSER = webdriver.Chrome(
    '/usr/local/bin/chromedriver')
#BROWSER.get('https://kredit.check24.de/kredit-desktop/processResult.html;jsessionid=64B7077C2696040B851F01200BD2A8E3.ajp13-01-ff02?id=426&comparisonParameters.loanAmount=10000&comparisonParameters.duration=84&comparisonParameters.purpose=8')

#BROWSER.get('https://www.geld.de/kredite.html?duration=60&amount=10000&category=888')

BROWSER.get('https://www.smava.de/pp/smava-kreditvergleich-responsive/comparison.html?amount=10000&category=888&duration=60&affiliateId=ec7b0c06&subAffiliateId=A-01-000&placementId=889722236&theme=grass&route=5&embedded=true&style=default&utm_source=emb&utm_medium=partner&includeSelection=true&build=20171107-0346')

try:
    if BROWSER.find_element_by_xpath('//*[@id="c24-fin-teaserbox"]//h2').text == "Bester Zins und beste Beratung":
      print("FUNCTIONAL: Page looks good!")
    else:
      print("FUNCTIONAL: Page sucks!")
except:
    print("FUNCTIONAL: Page sucks!")

# Setup custom config for PERF
CONFIG_FILE = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    '', 'config_check24.yaml')
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
