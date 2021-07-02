import time
from pycase import case_02D09
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://chrome.google.com/webstore/detail/earth-vpn-your-secured-vp/nabbmpekekjknlbkgpodfndbodhijjem?hl=en-US')
input('Done?')
total = len(case_02D09) - 1
for i in range(600, 900):
    driver.get("https://public.courts.in.gov/mycase#/vw/Search")
    driver.find_element_by_id('SearchCaseNumber').clear()
    driver.find_element_by_id('SearchCaseNumber').send_keys(case_02D09[i])
    time.sleep(2)
    driver.find_element_by_xpath('//button[contains(text(),"Search")]').click()
    time.sleep(3)
    f = open('files/4. cases_02D09/' + case_02D09[i] + '.txt', 'w')
    f.write(driver.page_source)
    f.close()
    print('index: ' + str(i) + '/' + str(total))
