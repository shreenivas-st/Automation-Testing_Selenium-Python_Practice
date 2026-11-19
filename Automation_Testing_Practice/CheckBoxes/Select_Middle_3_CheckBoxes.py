from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service = serv_obj)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@class='form-check-input'][@type='checkbox']")
for i in range (2, len(checkboxes)-2):
    checkboxes[i].click()

time.sleep(5)
driver.close()

