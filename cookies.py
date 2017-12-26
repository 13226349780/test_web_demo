from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.youdao.com')

#想cookie的name和value中添加会话信息
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbb'})

#遍历cookies中的name 和 value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookie():
    print("%s -> %s" % (cookie['name'],cookie['value']))
driver.quit()
