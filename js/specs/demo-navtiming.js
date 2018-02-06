const timings = require('timings-client-js');
const perf = new timings.PUtils('.perfconfig.js');

describe('Demo navtiming: ', function () {
    it(' should pass the performance assert', function () {
        const perfParams = perf.getApiParams( { sla: { pageLoadTime: 5000 }, debug: true } ); // overwrite values in perf.js
        return perf.getInjectJS('navtiming', 'visual_complete', true) // Get inject code from API - `true` = strip querystring
            .then((response) => {
                if (response && response.data && response.data.inject_code) {
                    const injectCode = response.data.inject_code || '';
                    return browser
                        .url('http://seleniumhq.org/test?strip_this')
                        .isVisible('#header')
                        .execute('window.performance.mark("visual_complete");') // Set visual complete mark
                        .execute(decodeURIComponent(injectCode)) // Inject JS code into browser object
                        .then((response) => {
                            // Grab the browser's response - has the perf data!
                            if (response.value) {
                                const browserResponse = response.value;
                                return perf.navtiming(browserResponse, perfParams, null) // Send perf data to API
                                .then((response) => {
                                        // Grab the API's response - has the assert field!
                                        if (response && response.data) {
                                            console.error("Navtiming:\n" + JSON.stringify(response.data.export.perf, null, 2));
                                            expect(response.data.assert, 'Performance failed! assert field is False').to.be.true; // Assert the result!
                                        } else {
                                            console.log('API error: ' + JSON.stringify(response, null, 2));
                                        }
                                    });
                            }
                        });
                }
            });
    });
});
