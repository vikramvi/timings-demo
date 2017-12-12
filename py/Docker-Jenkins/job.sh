#!/bin/bash

for i in {1..5}
do
    echo "Attempt Number : $i"

    echo "Smava Home Page"
    python smava/chrome_perf_smavaHomePage.py
    sleep 1
    echo "check24 Home Page"
    python check24/chrome_perf_check24HomePage.py
    
    sleep 1
    echo "geld Home Page"
    python geld/chrome_perf_geldHomePage.py
    
    sleep 1
    echo "finanzcheck Home Page"
    python finanzcheck/chrome_perf_finanzcheckHomePage.py

    sleep 1
done
