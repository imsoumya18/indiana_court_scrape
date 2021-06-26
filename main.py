from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://chrome.google.com/webstore/detail/touch-vpn-secure-and-unli/bihmplhobchoageeokmgbdihknkjbknd?hl=en')
input('Done?')
driver.get("https://public.courts.in.gov/mycase#/vw/Search")
driver.find_element_by_id('SearchCaseNumber').send_keys('30D02-1206-CM-000832')
driver.find_element_by_xpath('//button[contains(text(),"Search")]').click()
