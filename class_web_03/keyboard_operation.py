# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/25

E-mail:keen2020@outlook.com

=================================


"""

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 键盘操作

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys('柠檬班', Keys.ENTER)

loc = By.XPATH, '//a[text()="-CSDN学院"]'
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 将元素滚动到可视区域,一般情况下无需拖动滚动条，直接查找元素点击即可

