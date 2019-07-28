# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/28

E-mail:keen2020@outlook.com

=================================


"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import datetime
import time

# 查询明天的北京到上海的火车票（学生票）
i = 0
while i < 5:
    driver = webdriver.Chrome()
    driver.get("https://www.12306.cn/index/")
    driver.maximize_window()

    # 智能等待页面加载完成，出现搜索框
    loc = By.XPATH, '//a[@id="search_one"]'
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))

    js = """
    
    f = document.getElementById("fromStation")
    f1 = document.getElementById("fromStationText")
    f.value = "BJP"
    f1.value = "北京"
    
    t = document.getElementById("toStation")
    t1 = document.getElementById("toStationText")
    t.value = "SHH"
    t1.value = "上海"
    
    d = document.getElementById("train_date")
    d.readOnly = false
    d.value = "{}"
    
    s = document.getElementById("isStudentDan")
    s.click()
    
    se = document.getElementById('search_one')
    se.click()
    
    
    """.format(datetime.datetime.now().date() + datetime.timedelta(days=1))

    time.sleep(3)
    driver.execute_script(js)
    time.sleep(8)
    driver.quit()
    i += 1
    print("第{}次查询执行完成".format(i))
