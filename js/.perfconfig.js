/*
This file contains default parameters which will be used if they are not provided by the test script!
Please set PERF_API_URL to the correct address of your timings API!!
*/

module.exports = {
    // Below is the full fqdn of the API server
    "PERF_API_URL": "http://localhost/v2/api/cicd/",             // The full URL to the API host
    "api_timeout": 3000,                        // Timeout for the API - increase this if you're experiencing slow connection to the API

    // Below are your default "api parameters" that will be send to the API in the POST body - you can overwrite these with the `getApiParams()` method
    "api_params": {
        "sla": {                                // This is the "flat SLA" - valid keys are "pageLoadTime" or "visualCompleteTime"
            "pageLoadTime": 2000                    // Flat maximum threshold - this will be used if baseline (+ padding) is greater or flags.assertBaseline=false!
        },
        "baseline": {                           // These settings will be used by the API to calculate the baseline
            "days": 7,                              // Number of days to calculate the baseline for
            "perc": 75,                             // Percentile to calculate
            "padding": 1.2,                         // Extra padding on top of the calculated baseline (gives some wiggle-room)
            "incl": {
                "browser": "_log_"                  // Filter the baseline based on the corresponding value in the log object
            },
            searchUrl: "*wildcard*"                 // Filter the baseline on the URL using this wildcard (if omitted, the main URL will be used)
        },
        "flags": {                              // These booleans will tell the API what to do
            "assertBaseline": true,                 // Whether or not to compare against baseline
            "debug": false,                         // Request extra debug info from the API
            "esTrace": false,                       // Request elasticsearch output from API
            "esCreate": false,                      // Save results to elasticsearch
            "passOnFailedAssert": false             // Pass the test, even when the performance is above the threshold
        },
        "log": {                                // These key-value pairs will be stored in elasticsearch and can be used to slice & dice the data in Kibana
            "test_info": "Sample test_info-JS",     // Info about the test(-step)
            "env_tester": "Sample tester",          // Environment of the test machine (local, saucelabs, selenium grid, etc.)
            "browser": "Sample browser",            // Browser used to run the test with
            "env_target": "Sample target",          // Environment of the target app (usually dev, test, or prod)
            "team": "DEMO TEAM"                     // The name of the (test-)team 
        }
    }
};
