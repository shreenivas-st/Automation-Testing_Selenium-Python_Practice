import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH,"//input[@class='form-check-input'][@type='checkbox']")
print(len(checkboxes))

for i in range(len(checkboxes)):
    checkboxes[i].click()
time.sleep(5)
driver.close()
