#!/bin/bash

IP_ADDRESS_OF_CHROME_CONTAINER=http://0.0.0.0:5902

for i in {1..5}
do
    echo "Attempt Number : $i"

    echo "Smava Home Page"
    python smava/chrome_perf_smavaHomePage.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Comparision Page"
    python smava/chrome_perf_smavaComparisionPage.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Kredit"
    python smava/chrome_perf_smavaKredit.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Kredit Vergleichen"
    python smava/chrome_perf_smavaKreditVergleichen.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Lead Form"
    python smava/chrome_perf_smavaLeadForm.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Mobile Kredit"
    python smava/chrome_perf_smavaMobileKredit.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Route V1"
    python smava/chrome_perf_smavaRouteV1Page.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Top Kredit"
    python smava/chrome_perf_smavaTopKredit.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Zugangsdaten"
    python smava/chrome_perf_smavaZugangsdaten.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Mobilede Smava Integration Page"
    python smava/chrome_perf_mobiledeSmava.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "Smava Kfzrechner Page"
    python smava/chrome_perf_smavaKfzrechner.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "check24 Home Page"
    python check24/chrome_perf_check24HomePage.py $IP_ADDRESS_OF_CHROME_CONTAINER    
    sleep 1

    echo "geld Home Page"
    python geld/chrome_perf_geldHomePage.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

    echo "finanzcheck Home Page"
    python finanzcheck/chrome_perf_finanzcheckHomePage.py $IP_ADDRESS_OF_CHROME_CONTAINER
    sleep 1

done
