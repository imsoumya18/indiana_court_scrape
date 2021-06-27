import time
from selenium import webdriver

identifiers = ['01D01', '01C01', '02D02', '02D09', '02D08', '02C01', '02D01', '02H01', '02D03', '02D05', '02D07',
               '02D04', '02D06', '03C01', '03D01', '03D02', '04C01', '05D01', '05C01', '06I02', '06D01', '06D02',
               '06C01', '07C01', '08C01', '08D01', '08H01', '09D01', '09C01', '09D02', '10I01', '10D01', '10D02',
               '10C01', '100', '10C04', '10C03', '10D03', '10C02', '11C01', '11D01', '12H01', '12D01', '12C01',
               '120', '13C01', '14D01', '14C01', '140', '15H02', '150', '15D01', '15D02', '15C01', '16D01', '16C01',
               '17D02', '17D01', '17C01', '18C01', '18D03', '18C04', '18C05', '18D01', '18C03', '18D02', '18D04',
               '18H01', '18C02', '19C01', '19D01', '20D06', '20D02', '200', '2000', '20D05', '20D04', '20C01', '20H03',
               '20H01', '20D01', '20H02', '20D03', '21C01', '21D01', '22C01', '22D01', '220', '22D03', '22D02', '23H01',
               '23C01', '24C02', '24C01', '25D01', '250', '25C01']

years = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

months = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

types = ['CF', 'CM', 'CR', 'DF', 'MC', 'MR', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'FA', 'FB', 'FC', 'FD']

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver.get('https://chrome.google.com/webstore/detail/touch-vpn-secure-and-unli/bihmplhobchoageeokmgbdihknkjbknd?hl=en')
input('Done?')
driver.get("https://public.courts.in.gov/mycase#/vw/Search")
driver.find_element_by_id('SearchCaseNumber').send_keys('30D02-1206-CM-000832')
driver.find_element_by_xpath('//button[contains(text(),"Search")]').click()
time.sleep(5)
print(driver.page_source)
f = open('30D02-1206-CM-000832' + '.txt', 'a')
f.write(driver.page_source)
f.close()
