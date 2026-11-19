import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

table = driver.find_element(By.XPATH, "//a[@class='home-link']")
driver.execute_script("arguments[0].scrollIntoView(true);", table)

time.sleep(5)
driver.close()