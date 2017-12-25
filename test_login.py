
import unittest
from time import sleep

from selenium import webdriver


class test_baidu_login(unittest.TestCase):
    def test_login(self):
        dirver = webdriver.Chrome()
        dirver.get('http://baidu.com')
        dirver.maximize_window()
        login = dirver.find_element_by_link_text('登录')
        login.click()
        sleep(2)
        account = dirver.find_element_by_id('TANGRAM__PSP_10__userName')
        account.clear()
        account.send_keys('13226349780')
        login = dirver.find_element_by_id('TANGRAM__PSP_10__password')
        login.clear()
        login.send_keys('lqf1994019')
        sleep(3)








if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_baidu_login)
    unittest.TextTestRunner(verbosity=2).run(suite)