# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/24

E-mail:keen2020@outlook.com

=================================


"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# window_switch
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')     # get操作会自动等待，无需再次等待
print(driver.current_window_handle)
wins = driver.window_handles
print('所有的窗口0:{}'.format(wins))

driver.find_element_by_id('kw').send_keys('柠檬班')
driver.find_element_by_id('su').click()

wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="_腾讯课堂"]')))
driver.find_element_by_xpath('//a[text()="_腾讯课堂"]').click()     # 点击腾讯课堂，新窗口的出现

wait.until(EC.new_window_is_opened(wins))   # 等待，知道新窗口出现

# 获取所有的窗口列表
wins = driver.window_handles
print('所有的窗口1:{}'.format(wins))

# 切换新窗口
driver.switch_to.window(wins[1])    # 切换到第二个窗口进行操作，腾讯课堂页面
loc = By.XPATH, '//section//h2[contains(text(),"老师")]'
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
