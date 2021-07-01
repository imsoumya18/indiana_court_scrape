import time
from pycase import case_01D01
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://chrome.google.com/webstore/detail/touch-vpn-secure-and-unli/bihmplhobchoageeokmgbdihknkjbknd?hl=en')
input('Done?')
total = len(case_01D01) - 1
for i in range(5584, 5601):
    driver.get("https://public.courts.in.gov/mycase#/vw/Search")
    driver.find_element_by_id('SearchCaseNumber').clear()
    driver.find_element_by_id('SearchCaseNumber').send_keys(case_01D01[i])
    # driver.execute_script("window.scrollTo(0, 1080)")
    time.sleep(2)
    driver.find_element_by_xpath('//button[contains(text(),"Search")]').click()
    time.sleep(3)
    f = open('files/1. cases_01D01/' + case_01D01[i] + '.txt', 'w')
    f.write(driver.page_source)
    f.close()
    print('index: ' + str(i) + '/' + str(total))
