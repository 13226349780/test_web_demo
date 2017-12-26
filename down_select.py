from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

dirver = webdriver.Chrome()
dirver.implicitly_wait(10)
dirver.get('http://www.baidu.com')


dirver.find_element_by_link_text('设置').click()
sleep(1)

dirver.find_element_by_link_text('搜索设置').click()

sleep(2)

sel = dirver.find_element_by_xpath("//select[@id='nr']")
sl = Select(sel).select_by_value('50')


sleep(5)
save = dirver.find_element_by_link_text('保存设置')
save.click()
sleep(2)
al = dirver.switch_to.alert
al.accept()
sleep(2)



dirver.quit()