/*
This file contains the default parameters for the API
Below values will be used if they are not provided by the test script!

Please set PERF_API_URL to the correct address of the API!!

*/

module.exports = {
    // Below is the full fqdn of the API server
    "PERF_API_URL": "http://timings-api.int.godaddy.com/v2/api/cicd/",
    "api_timeout": 3000,

    // Below are the "api parameters" that will be send to the API in teh POST body
    "api_params": {
        "sla": {                // This is the "flat SLA" - valid keys are "pageLoadTime" or "visualCompleteTime"
            "pageLoadTime": 5000                    // Flat maximum threshold - this will be used if baseline (+ padding) is greater or flags.assertBaseline=false!
        },
        "baseline": {           // These settings will be used by the API to calculate the baseline
            "days": 7,                              // Number of days to calculate the baseline for
            "perc": 75,                             // Percentile to calculate
            "padding": 1.2,                         // Extra padding on top of the calculated baseline (gives some wiggle-room)
            "incl": {
                "browser": "_log"                   // Filter the baseline based on the corresponding value in the log object
            },
            searchUrl: "*wildcard*"                 // Filter the baseline on the URL using this wildcard (if omitted, the main URL will be used)
        },
        "flags": {              // These booleans will tell the API what to do
            "assertBaseline": true,                 // Whether or not to compare against baseline
            "debug": false,                         // Request extra debug info from the API
            "esTrace": false,                       // Request elasticsearch output from API
            "esCreate": false,                      // Save results to elasticsearch
            "passOnFailedAssert": false             // Pass the test, even when the performance is above the threshold
        },
        "log": {                // These key-value pairs will be stored in elasticsearch and can be used to slice & dice the data in Kibana
            "app_info": "Sample test_info-JS",     // Info about the test(-step)
            "platform": "Sample tester",          // Environment of the test machine (local, saucelabs, selenium grid, etc.)
            "browser": "Sample browser",            // Browser used to run the test with
            "environment": "Sample target",          // Environment of the target app (usually dev, test, or prod)
            "team": "DEMO"                          // THe name of the (test-)team 
        }
    }
};
