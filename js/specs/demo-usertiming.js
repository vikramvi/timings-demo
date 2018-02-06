const timings = require('timings-client-js');
const perf = new timings.PUtils('.perfconfig.js');

describe('Demo usertiming: ', function () {
    it(' should pass the performance assert', function () {
        const perfParams = perf.getApiParams( { sla: { pageLoadTime: 5000 }, debug: true } ); // overwrite values in perf.js
        return perf.getInjectJS('usertiming', '', true) // Get inject code from API - `true` = strip querystring
            .then((response) => {
                if (response && response.data && response.data.inject_code) {
                    const injectCode = response.data.inject_code || '';
                    return browser
                        .url('https://reactjs.org/')
                        .isVisible('#examples')
                        .execute('window.performance.mark("demo_start");') // Set User Timing "start" mark
                        .click('a[href="/tutorial/tutorial.html"]')
                        .isVisible('#how-to-follow-along')
                        .execute('window.performance.mark("demo_stop");') // Set User Timing "stop" mark
                        .execute(decodeURIComponent(injectCode)) // Inject JS code into browser object
                        .then((response) => {
                            // Grab the browser's response - has the perf data!
                            if (response.value) {
                                // console.error(JSON.stringify(response.value, null, 2));
                                const browserResponse = response.value;
                                return perf.usertiming(browserResponse, perfParams, null) // Send perf data to API
                                .then((response) => {
                                        // Grab the API's response - has the assert field!
                                        if (response && response.data) {
                                            console.error("Usertiming:\n" + JSON.stringify(response.data.export.perf, null, 2));
                                            expect(response.data.assert, 'Performance failed! assert field is False').to.be.true; // Assert the result!
                                        } else {
                                            console.error('API error:\n' + JSON.stringify(response, null, 2));
                                        }
                                    });
                            }
                        });
                }
            });
    });
});
