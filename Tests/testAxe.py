import pytest
from selenium import webdriver
from axe_selenium_python import Axe
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import os
import time

def test_axe():

    firefox_options = Options()
    firefox_options.add_argument("--headless")

    file = open("url.txt","r")
    urlList = file.readlines()
    driver = webdriver.Firefox()
    driver.set_window_size(320, 568)
    time.sleep(1)
    i = 1
    for urlTest in urlList:
        driver.get(urlTest)
        axe = Axe(driver)

        # Inject axe-core javascript into page.
        axe.inject()
        # Run axe accessibility checks.
        options = {"runOnly": ["wcag2a"]}
        results = axe.execute(options=options)
        
        # Write results to file
        #-------------------------
        violationNumber = len(results['violations'])
        print violationNumber, "violations found in ", urlTest
        Report_Axe = axe.report(results['violations'])
        if violationNumber != 0 :
            file = open("finalReport{}.txt".format(i), "a")
            file.write("URL = %s" %urlTest)
            file.write(Report_Axe+ "\n")
            file.flush()
            num_lines = sum(1 for line in open("finalReport{}.txt".format(i)))
            if num_lines >= 1000:
                i = i+1
        
            formattedURL = urlTest.replace("/","").replace("https:","").replace(".","-")
            axe.write_results('JSON_Results/{}.json'.format(formattedURL), results["violations"])
    
    driver.close


if __name__ == "__main__": test_axe()