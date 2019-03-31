# 自动关注

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import pymysql

import operator

from selenium.common.exceptions import TimeoutException

from time import sleep
import os


if __name__ == '__main__':

    # 连接database
    conn = pymysql.connect(host="127.0.0.1", user="XXXX", password="XXXX", database="XXXX", charset="utf8")  # 替换成你自己的数据库即可。

    # 拿到数据 id 字段

    sql = "select id from yuque "

    cur = conn.cursor()

    cur.execute(sql)

    data = cur.fetchall()

    list1 = list(data)

    # 加载浏览器驱动。

    driver = webdriver.Chrome(executable_path='./chromedriver')

    # chrome浏览器驱动,我这里选的是 Mac 版。windows 用户这里改成 ./chromedriver.exe ; Linux 用户请改成 ./chromedriver-linux

    url2 = 'https://www.yuque.com/liyaomei'  # get打开语雀个人信息主页

    driver.get(url2)
    btn = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_class_name('btn-follow'))
    btn.click()  # 点击按钮

    url1 = 'https://www.yuque.com/login'  # 登录

    driver.get(url1)

    name = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('login'))

    password = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('password'))

    btn_login = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_class_name('btn-login'))

    name.send_keys('xxxxxxx') # 这里替换成你的用户名

    password.send_keys('xxxxxx') # 这里替换成你的密码

    btn_login.click()  # 点击登录

    btn = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_class_name('btn-follow'))

    btn_text = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_class_name('btn-follow').text)

    if (btn):
        if(btn_text=='关 注'):
            btn.click()  # 点击按钮

    list2 = map(operator.itemgetter(0), list1)

    for id in list2:

        # print(id)
        url_home = 'https://www.yuque.com/%s' % (id)  # get打开语雀个人信息主页

        driver.get(url_home)

        try:
            btn = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_class_name('btn-follow'))
            btn_text = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_class_name('btn-follow').text)
        except TimeoutException:
            print("超时异常，可能用户主页不存在！")
            continue

        if (btn):
            if (btn_text == '关 注'):  # 如果按钮是"关 注" 两个字，则点击关注。
                btn.click()  # 点击按钮

        # sleep(1)

