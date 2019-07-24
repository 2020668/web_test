# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/7/24

E-mail:keen2020@outlook.com

=================================


"""
from selenium import webdriver

driver = webdriver.Chrome()     # 启动与Chrome浏览器的会话
driver.get('https://www.baidu.com')       # 访问指定网站

driver.maximize_window()    # 最大化窗口
# driver.quit()    # 退出会话,关闭浏览器，kill chrome driver 进程
# driver.close()   # 关闭当前窗口

# driver.get('https://www.ketangpai.com')
# driver.back()     # 上一页
# driver.forward()    # 下一页
# driver.refresh()    # 刷新
# driver.close()   # 关闭当前窗口

# 6种单一属性查找元素，id name class tag_name
ele = driver.find_element_by_id('kw')
# ele.click()     # 单击
print(ele.get_attribute('class'))       # 获取属性值
# ele.send_keys('完美')     # 输入内容
# name
driver.find_element_by_name('wd')      # 匹配到的第一个元素
driver.find_elements_by_name('wd')     # 返回一个list 元素列表

driver.find_element_by_class_name('bg')     # 只能是一个class属性

driver.find_element_by_tag_name('span')     # tag_name

driver.find_element_by_link_text('更多产品')        # 精确匹配文本值
driver.find_element_by_partial_link_text('产品')      # 模糊匹配文本值
# 两种方式来找元素
# 绝对定位  /开头 严格按照层级，同级元素的位置
# 相对定位      //开头 在参照物之下，只要符合条件的元素存在即可
# 先根据自身特有的特征查找，附加条件用 //标签名[@属性名=值 and or @属性名=值]
# 百度首页的登录元素  //div[@id='u1']/a[@name='tj_login' and @class='lb']
# 文本定位方式    //标签名[text()=' ']
# 包含  //a[contains(@href,'Course/homework/courseid') and text()='作业']
