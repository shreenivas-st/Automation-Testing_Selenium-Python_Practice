import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID, "datepicker").send_keys("04/03/2015")
time.sleep(5)

driver.close()
