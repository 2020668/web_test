# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/24

E-mail:keen2020@outlook.com

=================================


"""

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 全新的html页面，内嵌html
# 首先判断要操作的元素是否在iframe内

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 触发alert弹框出现
driver.find_element_by_id('press_me').click()

time.sleep(0.5)     # 等待
WebDriverWait(driver, 20).until(EC.alert_is_present())

# 切换
alert = driver.switch_to.alert  # Alert类的实例化

alert.accept()      # 确定，并关闭弹窗
alert.dismiss()     # 取消，并关闭弹窗

