import time
from pycase import x
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get(
    'https://chrome.google.com/webstore/detail/hotspot-shield-free-vpn-p/nlbejmccbhkncgokjcmghpfloaajcffj/related')
input('Done?')
total = len(x) - 1
for i in range(500, len(x)):
    if i % 30 == 0:
        time.sleep(17)
    driver.get("https://public.courts.in.gov/mycase#/vw/Search")
    driver.find_element_by_id('SearchCaseNumber').clear()
    driver.find_element_by_id('SearchCaseNumber').send_keys(x[i])
    time.sleep(1)
    driver.find_element_by_xpath('//button[contains(text(),"Search")]').click()
    # time.sleep(3)
    f = open('D:\\files\\' + x[i] + '.txt', 'w')
    f.write(driver.page_source)
    f.close()
    print('index: ' + str(i) + '/' + str(total))
