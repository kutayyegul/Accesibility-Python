from modules import *

i=1
def axeReporter(urlTest, results, driver, i=i):
    axe = Axe(driver)
    violationNumber = len(results['violations'])
    print violationNumber, "violations found in ", urlTest
    Report_Axe = axe.report(results['violations'])
    if violationNumber != 0:
        file = open("finalReport{}.txt".format(i), "a")
        file.write("URL = %s" % urlTest)
        file.write(Report_Axe + "\n")
        file.flush()
        num_lines = sum(1 for line in open("finalReport{}.txt".format(i)))
        if num_lines >= 1000:
            i = i + 1

        formattedURL = urlTest.replace("/", "").replace("https:", "").replace(".", "-")
        axe.write_results('JSON_Results/{}.json'.format(formattedURL), results["violations"])