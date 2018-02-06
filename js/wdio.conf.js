const chai = require('chai');
const fs = require('fs'),
  path = require('path');

exports.config = Object.assign({}, {
  // debug: true,
  // execArgv: ['--inspect=127.0.0.1:5859'],
  specs: [
  ],
  suites: {
    perf: [
      './specs/demo-navtiming.js',
      './specs/demo-nav-async.js',
      './specs/demo-user-async.js',
      './specs/demo-usertiming.js'
    ]
  },
  exclude: [
  ],
  maxInstances: 10,
  capabilities: getCapabilities(),
  sync: false,
  logLevel: 'error',
  coloredLogs: true,
  screenshotPath: './errorShots/',
  baseUrl: '',
  waitforTimeout: 20000,
  connectionRetryTimeout: 90000,
  connectionRetryCount: 3,
  services: ['selenium-standalone'],
  framework: 'mocha',
  reporters: ['dot'],
  mochaOpts: {
    ui: 'bdd',
    timeout: 999999999
  },
  before: () => {
    global.expect = chai.expect;
    global.assert = chai.assert;
  }

});

function getCapabilities() {
  const browsersList = [];
  if (process.env.BROWSERS_TO_RUN === 'chrome') {
    browsersList.push({ browserName: 'chrome', screenResolution: '1600x1200', version: 'latest' });
  }
  else if (process.env.BROWSERS_TO_RUN === 'ie11') {
    browsersList.push({ browserName: 'internet explorer', screenResolution: '1600x1200', version: 'latest' });
  }
  else if (process.env.BROWSERS_TO_RUN === 'safari') {
    browsersList.push({ browserName: 'safari', screenResolution: '1600x1200', version: 'latest' });
  }
  else if (process.env.BROWSERS_TO_RUN === 'firefox') {
    browsersList.push({ browserName: 'firefox', screenResolution: '1600x1200', version: 'latest' });
  }
  else if (process.env.BROWSERS_TO_RUN === 'edge') {
    browsersList.push({ browserName: 'MicrosoftEdge', screenResolution: '1600x1200',
      tunnelIdentifier: process.env.TUNNEL_IDENTIFIER, version: 'latest' });
  }
  else if (process.env.BROWSERS_TO_RUN === 'iPhone') {
    browsersList.push({ browserName: 'chrome', version: '60', chromeOptions: { mobileEmulation: { deviceName: 'iPhone 6' } } });
  }
  else if (process.env.BROWSERS_TO_RUN === 'android') {
    browsersList.push({ browserName: 'chrome', version: '60', chromeOptions: { mobileEmulation: { deviceName: 'Nexus 6' } } });
  }
  else {
    const defaultCapability = { browserName: 'chrome', version: 'latest' };
    browsersList.push(defaultCapability);
  }
  if (browsersList.length < 1) {
    const defaultCapability = { browserName: 'chrome', version: 'latest' };
    browsersList.push(defaultCapability);
    console.log('Running the test on the default browser.');
  }
  return browsersList;
}
