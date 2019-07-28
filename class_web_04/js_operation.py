# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/27

E-mail:keen2020@outlook.com

=================================


"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime


"""
移动到元素element对象"底部" 与当前窗口的底部对齐
driver.execute_script("arguments[0].scrollIntoView(false);", element)

移动元素element对象的顶端与当前窗口的顶部对齐
driver.execute_script("arguments[0].scrollIntoView();", element)

移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

移动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

"""

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("汽车", Keys.ENTER)
loc = By.XPATH, '//a[text()="之家_看车买车用车 都回"]'

WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)
driver.execute_script("arguments[0].scrollIntoView(false);", ele)

time.sleep(3)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 12306 js修改日期输入框,可灵活更换日期(format) 或 a.value = arguments[0] driver.execute_script(js, "python当前时间")
js = """
var a = document.getElementById("train_date");
a.readOnly = false;
a.value = arguments[0]

"""
driver.execute_script(js, datetime.datetime.now().date() + datetime.timedelta(days=1))  # 明天

