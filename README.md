# timings-demo

Sample tests scripts to demonstrate the [timings API](https://www.github.com/godaddy/timings). You can copy/reference the test scripts in this repo to build your own "timings-enabled" scripts. You can find both JavaScript and Python based scripts in the `/js` and `/py` folders.

The scripts are implementing two of the timings API clients that are available here:

* `npm` installable JavaScript client [(http://www.github.com/godaddy/timings-client-js)](http://www.github.com/godaddy/timings-client-js)
* `pip` installable Python client [(http://www.github.com/godaddy/timings-client-py)](http://www.github.com/godaddy/timings-client-py)

## Installation

You can also run the tests in this repo to test your **timings API**! See installation instructions below:

### **JavaScript based test scripts**

clone repo with `git clone` and install dependencies with `npm i` (**run this from inside the `/js` sub-folder!**)

```bash
$ git clone https://github.com/Verkurkie/timings-demo.git
$ cd {rootFolder}/js
$ npm i
```

#### Configuration for JavaScript tests

Before running tests, you have to configure the default parameters by editing the config file `{rootFolder}/js/.perfconfig.js`. The most important settings to change are:

|key|description|example|
|-|-|-|
|`PERF_API_URL`|Full URL of the API|`"http://my_api_server/v2/api/cicd/"`|
|`api_params.flags.esCreate`|Save results to ElasticSearch|`true`|
|`api_params.log.test_info`|Information about the test(-step)|`My test`|
|`api_params.log.env_tester`|Environment of the test machine|`local`|
|`api_params.log.browser`|Browser being used for the test|`Chrome`|
|`api_params.log.env_target`|Environment of the target app/api|`prod`|
|`api_params.log.team`|The name of your team/product|`MY_PRODUCT`|

#### Running JavaScript tests (uses webdriverIO)

To run the all of the JS tests, run the following command:

```bash
$ cd {rootFolder}/js
$ npm run test
```

Or, to run indivisual JS tests, you can run this command:

```bash
$ cd {rootFolder}/js
$ ./node_modules/.bin/wdio ./wdio.conf.js --spec ./specs/{spec file}.js
```

### **Python based test scripts**

clone repo with `git clone` and install dependencies with `pip`:

```bash
$ git clone https://github.com/Verkurkie/timings-demo.git
$ cd {rootFolder}/py
$ pip install timingsclient selenium
```

#### Configuration for Python tests

Before running tests, you have to configure the default parameters by editing the config file `{rootFolder}/py/config.yaml`. The most important settings to change are:

|key|description|example|
|-|-|-|
|`PERF_API_URL`|Full URL of the API|`"http://my_api_server/v2/api/cicd/"`|
|`api_params.flags.esCreate`|Save results to ElasticSearch|`true`|
|`api_params.log.test_info`|Information about the test|`My test`|
|`api_params.log.env_tester`|Environment of the test machine|`local`|
|`api_params.log.browser`|The browser being used for the test|`Chrome`|
|`api_params.log.env_target`|Environment of the target (usually dev|test|prod)|`prod`|
|`api_params.log.team`|The name of your team/product|`MY_PRODUCT`|

#### Running Python test

Then, to run the Python tests, simply run:

```bash
$ cd {rootFolder}/py
$ python demo_2_perf.py
```
