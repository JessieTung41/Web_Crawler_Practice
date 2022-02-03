# -*- coding = utf-8 -*-
# @Time : 2022/1/31 5:52 PM
# @Author : Jieying Dong (Jessie)
# @File : 02_selenium_exe.py
# @Software: PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

web = Chrome()

web.get("http://lagou.com")

# find a specific element, and click it
# el = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')
# el.click()
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[1]/a')
el.click()

time.sleep(1)

# find a text box, enter "python" ==> enter "return"
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python", Keys.ENTER)


# find data position and get data
# div_list = web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div')
# for div in div_list:
#     print(div)
div_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
for div in div_list:
    job_name = div.find_element(By.TAG_NAME, 'a').text
    job_salary = div.find_element(By.CLASS_NAME, 'money__3Lkgq').text
    company_name = div.find_element(By.XPATH, './div[1]/div[2]/div[1]/a').text
    print(job_name, job_salary, company_name)




