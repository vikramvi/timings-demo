# timings-demo
Sample Selenium tests to demonstrate the [timings API](https://www.github.com/godaddy/timings).

## Installation
To install, you can clone the repo using `git clone` and install JavaScript dependencies with `npm i` (**run this from the `js` sub-folder!**) and the Python dependencies with `pip`:

```bash
$ git clone https://github.com/Verkurkie/timings-demo.git
$ cd {rootFolder}/js
$ npm i
$ cd ..
$ pip install timingsclient selenium
```

## Configuration for JavaScript tests
Before running tests, you have to configure the default parameters by editing the config file `{rootFolder}/.config.js`. The most important settings to change are:
|key|description|example|
|-|-|-|
|`PERF_API_URL`|Full URL of the API|`"http://my_api_server:3000/v2/api/cicd/"`|
|`api_params.flags.esCreate`|Save results to ElasticSearch|`true`|
|`api_params.log.test_info`|Information about the test(-step)|`My test`|
|`api_params.log.env_tester`|Environment of the test machine|`local`|
|`api_params.log.browser`|Browser being used for the test|`Chrome`|
|`api_params.log.env_target`|Environment of the target app/api|`prod`|
|`api_params.log.team`|The name of your team/product|`MY_PRODUCT`|

## Running JavaScript tests (uses webdriverIO)

To run the all of the JS tests, run the following command:

```bash
$ cd {rootFolder}/js
$ node_modules/webdriverio/bin/wdio wdio.conf.js
```

Or, to run indivisual JS tests, you can run this command:

```bash
$ cd {rootFolder}/js
$ node_modules/webdriverio/bin/wdio --spec ./specs/{spec file}.js wdio.conf.js
```

## Configuration for Python tests
Before running tests, you have to configure the default parameters by editing the config file `{rootFolder}/py/config.yaml`. The most important settings to change are:
|key|description|example|
|-|-|-|
|`PERF_API_URL`|Full URL of the API|`"http://my_api_server:3000/v2/api/cicd/"`|
|`api_params.flags.esCreate`|Save results to ElasticSearch|`true`|
|`api_params.log.test_info`|Information about the test|`My test`|
|`api_params.log.env_tester`|Environment of the test machine|`local`|
|`api_params.log.browser`|The browser being used for the test|`Chrome`|
|`api_params.log.env_target`|Environment of the target (usually dev|test|prod)|`prod`|
|`api_params.log.team`|The name of your team/product|`MY_PRODUCT`|

## Running Python test
Then, to run the Python tests, simply run:

```bash
$ cd {rootFolder}/py
$ python demo_2_perf.py
```
