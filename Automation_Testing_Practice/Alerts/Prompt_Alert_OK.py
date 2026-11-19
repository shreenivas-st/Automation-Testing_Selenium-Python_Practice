import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID, "promptBtn").click()
time.sleep(3)
alert = driver.switch_to.alert
time.sleep(3)
print(alert.text)
time.sleep(3)
alert.send_keys("Shreenivas")
time.sleep(5)
alert.accept()
time.sleep(3)

driver.close()