#coding=utf-8
import unittest
from datetime import time
from time import sleep

from selenium import webdriver

class test_web_demo(unittest.TestCase):
    def test_baidu(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://www.baidu.com")

        driver.find_element_by_id("kw").send_keys("Selenium2")
        driver.find_element_by_id("su").click()
        sleep(10)
        #driver.quit()



if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(test_web_demo)
    unittest.TextTestRunner(verbosity=2).run(suite)