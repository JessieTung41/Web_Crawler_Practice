# -*- coding = utf-8 -*-
# @Time : 2022/2/1 6:25 PM
# @Author : Jieying Dong (Jessie)
# @File : 06_super_angle.py
# @Software: PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
import time

web = Chrome()

web.get('http://www.chaojiying.com/user/login/')

# Deal with verification codes
img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('xxxxxx', 'xxxxxxx', '96001')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

# Enter username, password and verification code
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('xxxxx')
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('xxxxx')

web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(5)

# Login
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

