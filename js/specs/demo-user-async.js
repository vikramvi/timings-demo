const timings = require('timings-client-js');
const perf = new timings.PUtils('.perfconfig.js');

describe('Demo usertiming [async/await]: ', () => {
  it(' should pass the performance assert', async () => {
    const perfParams = perf.getApiParams({ sla: { pageLoadTime: 5000 }, debug: true }); // overwrite values in perf.js
    const injectJs = await perf.getInjectJS('usertiming', '', true);   // Request inject code from API - `true` = strip querystring
    const injectCode = injectJs.data.inject_code;
    const injectCodeResponse = await browser
      .url('https://reactjs.org/')
      .isVisible('#examples')
      .execute('performance.mark("demo_start");') // Set User Timing "start" mark
      .click('a[href="/tutorial/tutorial.html"]')
      .isVisible('#how-to-follow-along')
      .execute('performance.mark("demo_stop");') // Set User Timing "stop" mark
      .execute(decodeURIComponent(injectCode)); // Inject JS code into browser object
    const injectCodeResponseValue = injectCodeResponse.value; // Grab the browser's response - has the perf data!
    const navtimingResponse = await perf.usertiming(injectCodeResponseValue, perfParams); // Send perf data to API
    if (navtimingResponse.data) {
      const apiResponse = navtimingResponse.data; // Grab the API's response - has the assert field!
      console.error("Usertiming [async]:\n" + JSON.stringify(apiResponse.export.perf, null, 2));
      expect(apiResponse.assert, 'Performance failed! assert field is False').to.be.true; // Assert the result!
    } else {
      console.error('API error: ' + JSON.stringify(navtimingResponse, null, 2));
    }
  }, 2);
});
