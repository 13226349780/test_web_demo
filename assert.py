from selenium import webdriver
from time import sleep

driver =webdriver.Chrome()
driver.get("https://www.baidu.com")
print('Before search =======')


title = driver.title
print(title)



now_url = driver.current_url
print(now_url)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)


print('After search =======')


title = driver.title
print(title)