from helperAxe.modules import *
from helperAxe.axeWriter import axeReporter

def test_axe():

    firefox_options = Options()
    firefox_options.add_argument("--headless")

    file = open("url.txt","r")
    urlList = file.readlines()
    driver = webdriver.Firefox(firefox_options=firefox_options)
    #driver.set_window_size(320, 568)
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
        axeReporter(urlTest, results, driver)

    
    driver.close


if __name__ == "__main__": test_axe()