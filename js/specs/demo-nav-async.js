const timings = require('timings-client-js');
const perf = new timings.PUtils('.perfconfig.js');

describe('Demo navtiming [async/await]: ', () => {
  it(' should pass the performance assert', async () => {
    let url = 'http://seleniumhq.org/';
    const perfParams = perf.getApiParams({ sla: { pageLoadTime: 5000 }, debug: true }); // overwrite values in perf.js
    const injectJs = await perf.getInjectJS('navtiming', 'visual_complete', true);   // Request inject code from API - `true` = strip querystring
    const injectCode = injectJs.data.inject_code;
    const injectCodeResponse = await browser
      .url(url)
      .isVisible('#headersdfer')
      .execute('window.performance.mark("visual_complete");') // Set visual complete mark
      .execute(decodeURIComponent(injectCode)); // Inject JS code into browser object
    const injectCodeResponseValue = injectCodeResponse.value; // Grab the browser's response - has the perf data!
    const navtimingResponse = await perf.navtiming(injectCodeResponseValue, perfParams); // Send perf data to API
    if (navtimingResponse.data) {
      const apiResponse = navtimingResponse.data; // Grab the API's response - has the assert field!
      console.error("Navtiming [async]:\n" + JSON.stringify(apiResponse.export.perf, null, 2));
      expect(apiResponse.assert, 'Performance failed! assert field is False').to.be.true; // Assert the result!
    } else {
      console.error('API error: ' + JSON.stringify(navtimingResponse, null, 2));
    }
  }, 2);
});
