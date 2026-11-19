import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

min = driver.find_element(By.XPATH, "//div[@id='HTML7']//span[1]")
max = driver.find_element(By.XPATH, "//div[@id='HTML7']//span[2]")

print(min.location)
print(max.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(min, -25,0).perform()
act.drag_and_drop_by_offset(max, -85,0).perform()



time.sleep(5)
driver.close()