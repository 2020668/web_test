# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/24

E-mail:keen2020@outlook.com

=================================


"""

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

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://ke.qq.com/")
# wait = WebDriverWait(driver, 20)
# wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='账号密码登录']")))

driver.find_element_by_xpath("//section//a[text()='登录']").click()   # 点击登录

# 等待页面出现QQ登录
WebDriverWait(driver, 20).until(
EC.visibility_of_element_located((By.XPATH, '//a[text()="QQ登录"]')))

# 点击QQ登录
driver.find_element_by_xpath('//a[text()="QQ登录"]').click()
time.sleep(2)

WebDriverWait(driver, 20).until(
EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@name='login_frame_qq']")))

driver.find_element_by_xpath('//a[text()="帐号密码登录"]').click()

driver.find_element_by_id('u').send_keys('415250069')
driver.find_element_by_id('p').send_keys('zuowei19881128')
driver.find_element_by_xpath("//input[@value='登 录']").click()

# WebDriverWait(driver, 20).until(
# EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//a[text()=" 跳过 "]')))
# driver.find_element_by_xpath('//a[text()=" 跳过 "]').click()
# driver.find_element_by_xpath('//a[text()="下次再选"]').click()

WebDriverWait(driver, 20).until(EC.alert_is_present())

# 切换
alert = driver.switch_to.alert  # Alert类的实例化

# alert.accept()      # 确定，并关闭弹窗
# alert.dismiss()    # 取消，并关闭弹窗
# driver.find_element_by_xpath('//a[text()="下次再选"]').click()
