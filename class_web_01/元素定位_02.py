# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/24

E-mail:keen2020@outlook.com

=================================


"""

# from selenium import webdriver
# 轴定位,轴运算

# ancestor:祖先结点，包括父
# parent:父结点
# preceding:当前元素结点标签之前的所有结点  （html页面先后顺序)
# preceding-sibling:当前元素结点标签之前的所有兄弟结点
# following:当前元素结点标签之后的所有结点   (html页面先后顺序)
# following-sibling:当前元素结点标签之后的左右兄弟结点

# 语法 /轴名称::结点名称[@属性=值]
# css 语法 id:#id  class:.class 子孙:>
# 元素操作
# 等待 selenium webdriver 提供2种智能等待
# driver = webdriver.Chrome()
# 隐性等待
# driver.get('https://www.baidu.com')
# driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_login']").click()   # 找到百度首页的登录按钮，然后点击

# 显性等待

# 每隔一个时间段轮询一次，当满足条件时，执行下一步，否则继续等待，直到超时抛出异常
# WebDriverWait 类：显性等待类
# WebDriverWait(driver,等待时长,轮询周期).until()/until_not()
# excepted_conditions模块:提供了一系列期望发生的条件
# presence_of_element_located:元素存在
# visibility_of_element_located:元素可见
# element_to_be_clickable:元素可点击
# 切换: window/iframe/alert
# 键盘,鼠标
# 下拉列表
# 元素怎么滚动到可见区域
# js 操作 修改元素的属性
# 上传操作
# TANGRAM__PSP_10__footerULoginBtn


import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 傻等10s
# time.sleep(10)
# 开启一个浏览器会话
driver = webdriver.Chrome()
# 第一种  隐性等待
driver.implicitly_wait(30)  # 等待元素被找着、等待命令执行完成。
driver.get("http://www.baidu.com")
driver.maximize_window()
# selenium webdriver   2种智能等待。
# 时间上限：30秒   Timeout
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
# 第二种  显性等待
# 在我任何明确需要等待某个条件成立之后，才执行后续的代码。
# 等待 + 条件
# TANGRAM__PSP_10__footerULoginBtn
# 条件
loc = (By.ID, 'TANGRAM__PSP_10__footerULoginBtn')
# EC.visibility_of_element_located(loc)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
time.sleep(0.5)
# 操作条件满足之后的元素
driver.find_element(*loc).click()
# driver.find_element_by_id(loc[1]).click()     # 等价于上方
time.sleep(5)
# 结束会话
driver.quit()
