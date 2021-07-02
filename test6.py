import time
from pycase import case_02H01
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://chrome.google.com/webstore/detail/hola-free-vpn-proxy-unblo/gkojfkhlekighikafcpjkiklfbnlmeio?hl=en-US')
input('Done?')
total = len(case_02H01) - 1
for i in range(3660):
    driver.get("https://public.courts.in.gov/mycase#/vw/Search")
    driver.find_element_by_id('SearchCaseNumber').clear()
    driver.find_element_by_id('SearchCaseNumber').send_keys(case_02H01[i])
    time.sleep(2)
    driver.find_element_by_xpath('//button[contains(text(),"Search")]').click()
    # time.sleep(3)
    f = open('D:\\files\\8. case_02H01\\' + case_02H01[i] + '.txt', 'w')
    f.write(driver.page_source)
    f.close()
    print('index: ' + str(i) + '/' + str(total))
