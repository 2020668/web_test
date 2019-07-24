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
# 切换进iframe
# loc = (By.TAG_NAME, "iframe")
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))

# 要进入哪个iframe，下标/name属性/webelement对象
# driver.switch_to.frame('frame_name')
# driver.switch_to.frame(1)
# driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])

# 方式二,等待，切换，一步到位
WebDriverWait(driver, 20).until(
EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

# 切换之后，主html变成了切换之后的html页面

# 从iframe里，回到main的html
driver.switch_to.default_content()

# 从iframe里，回到上一层的html
driver.switch_to.parent_frame()
