from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
element = WebDriverWait(driver,5,0.5).until(
    EC.presence_of_all_elements_located((By.ID,'kw'))
)

element.send_keys('我的一天')
driver.quit()

