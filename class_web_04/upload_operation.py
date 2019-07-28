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
import time
import win32gui
import win32con

# edit – combobox – comboboxex32 - #32770
# 前提 windows上传窗口 sleep2秒等待弹框的出现

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ketangpai.com/")
loc = By.XPATH, '//a[text()="登录"]'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = By.XPATH, '//input[@name="account"]'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("15071366971")

driver.find_element_by_xpath('//input[@name="pass"]').send_keys("zuowei19881128")
driver.find_element_by_xpath('//div[@class="padding-cont pt-login"]//a[text()="下次自动登录"]').click()
driver.find_element_by_xpath('//div[@class="padding-cont pt-login"]//a[text()="登录"]').click()

loc = By.XPATH, '//a[text()="Python全栈第18期"]'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

time.sleep(3)

loc = By.XPATH, '//a[contains(text(),"0726")]'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

time.sleep(3)
# loc = By.XPATH, '//div[text()="上传文件"]'
loc = By.XPATH, '//label[@style="opacity: 0; width: 100%; height: 100%; ' \
                'display: block; cursor: pointer; background: rgb(255, 255, 255);"]'
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()


def upload(filePath, browser_type="chrome"):
    if browser_type == "chrome":
        title = "打开"
    else:
        title = ""

    # 找元素
    # 一级窗口 "#32770", "打开"
    dialog = win32gui.FindWindow("#32770", title)
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)    # 二级窗口,0代表从第一个开始找,后面是class和title
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)    # 三级窗口
    # 编辑按钮
    edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)       # 四级窗口
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")

    # 往编辑当中输入文件路径
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)     # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)      # 点击打开按钮


time.sleep(3)
upload("C:\\Users\keen\\Documents\\Software Testing\\Python自动化\\作业\\1831\\12306.py")
# upload("C:\\aow_drv.log")

time.sleep(3)
driver.find_element_by_xpath('//a[text()="提交"]').click()
