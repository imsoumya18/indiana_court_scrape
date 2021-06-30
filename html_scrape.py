import time
from pycase import case_01D01
from selenium import webdriver

# case_01D01 = ['01D01-0012-DF-000126', '01D01-0012-SC-000776', '01D01-0012-SC-000777', '01D01-0012-SC-000778',
#               '01D01-0012-SC-000779', '01D01-0012-SC-000780', '01D01-0012-SC-000781', '01D01-0012-SC-000770',
#               '01D01-0012-SC-000771', '01D01-0012-SC-000772', '01D01-0012-SC-000773', '01D01-0012-SC-000774',
#               '01D01-0012-SC-000775', '01D01-0012-DF-000125', '01D01-0012-CP-000116', '01D01-0012-CM-000542',
#               '01D01-0012-CM-000543', '01D01-0012-CM-000544', '01D01-0012-CM-000545', '01D01-0012-CM-000546',
#               '01D01-0012-CM-000547', '01D01-0012-CM-000549', '01D01-0012-IF-003928']

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://chrome.google.com/webstore/detail/touch-vpn-secure-and-unli/bihmplhobchoageeokmgbdihknkjbknd?hl=en')
input('Done?')
total = len(case_01D01) - 1
for i in range(2151, 15565):
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
