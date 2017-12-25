#coding=utf-8
import unittest
from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys


class test_web_demo(unittest.TestCase):
    def test_baidu(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://www.baidu.com")

        driver.find_element_by_id("kw").send_keys("Selenium2")
        driver.find_element_by_id("su").click()
        sleep(3)
        #driver.quit()
        #driver.find_element_by_id("kw").send_keys("我的一天")
        #driver.find_element_by_id("su").click()
        #sleep(3)
        #鼠标悬停在设置，展开设置
        shezhi = driver.find_element_by_class_name('pf')
        ActionChains(driver).move_to_element(shezhi).perform()
        sleep(3)
        search_setting = driver.find_element_by_link_text('搜索设置')
        search_setting.click()
        sleep(4)
        close_search_setting = driver.find_element_by_link_text('保存设置')
        close_search_setting.click()
        sleep(2)
        #切换到弹窗
        al = driver.switch_to.alert
        al.accept()
        sleep(2)




if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(test_web_demo)
    unittest.TextTestRunner(verbosity=2).run(suite)