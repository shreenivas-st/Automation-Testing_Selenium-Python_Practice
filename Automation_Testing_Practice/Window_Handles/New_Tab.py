import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//button[normalize-space()='New Tab']").click()
time.sleep(4)
print("current window title :", driver.title)
driver.switch_to.window(driver.window_handles[0])
print("parent window title :", driver.title)
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
print("child window title :", driver.title)
time.sleep(5)

driver.close()