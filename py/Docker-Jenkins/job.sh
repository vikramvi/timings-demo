#!/bin/bash

for i in {1..5}
do
    echo "Attempt Number : $i"

    echo "Smava Home Page"
    python smava/chrome_perf_smavaHomePage.py
    sleep 1

    echo "Smava Comparision Page"
    python smava/chrome_perf_smavaComparisionPage.py
    sleep 1

    echo "Smava Kredit"
    python smava/chrome_perf_smavaKredit.py
    sleep 1

    echo "Smava Kredit Vergleichen"
    python smava/chrome_perf_smavaKreditVergleichen.py
    sleep 1

    echo "Smava Lead Form"
    python smava/chrome_perf_smavaLeadForm.py
    sleep 1

    echo "Smava Mobile Kredit"
    python smava/chrome_perf_smavaMobileKredit.py
    sleep 1

    echo "Smava Route V1"
    python smava/chrome_perf_smavaRouteV1Page.py
    sleep 1

    echo "Smava Top Kredit"
    python smava/chrome_perf_smavaTopKredit.py
    sleep 1

    echo "Smava Zugangsdaten"
    python smava/chrome_perf_smavaZugangsdaten.py
    sleep 1

    echo "Mobilede Smava Integration Page"
    python smava/chrome_perf_mobiledeSmava.py

    echo "Smava Kfzrechner Page"
    python smava/chrome_perf_smavaKfzrechner.py
    
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
