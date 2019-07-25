# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/25

E-mail:keen2020@outlook.com

=================================


"""

# 元素具有4中操作，click send_keys text get_attribute\
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.find_element_by_id('kw').send_keys('淘宝')
# driver.find_element_by_id('su').click()
# text = driver.find_element_by_id('su').text
# driver.find_element_by_id('su').get_attribute('class')

# 鼠标操作，由selenium的ActionChains类来完成模拟鼠标操作
# 存储鼠标操作，=perform()来执行鼠标操作
# 支持 双击 double_click
# 右键操作 context_click
# 拖拽 drag_and_drop
# 鼠标悬停 move_to_element()

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()

# 找到元素
ele = driver.find_element_by_xpath('//div[@id="u1"]//a[text()="设置"]')

# 实例化ActionChains
ac = ActionChains(driver)

# 悬浮操作
ac.move_to_element(ele).click(ele)

# 执行鼠标操作
ac.perform()

loc = By.XPATH, '//a[text()="高级搜索"]'
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# select类 下拉框操作
# selenium 提供了Select类来处理select/option
# 引入类 from selenium.webdriver.support.ui import Select

# 选择下拉列表值的三种方法
# 1.通过下标选择，select_by_index(index值) 从0开始
# 2.通过value属性：select_by_value(value值)
# 3.通过文本内容：select_by_visible_text(文本内容)

# 先找到select元素
loc = By.XPATH, '//select[@name="ft"]'
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
select_ele = driver.find_element(*loc)

# 实例化Select类
s = Select(select_ele)
s.select_by_index(4)
time.sleep(3)
s.select_by_value('all')
time.sleep(3)
s.select_by_visible_text('Adobe Acrobat PDF (.pdf)')
time.sleep(3)
driver.quit()





