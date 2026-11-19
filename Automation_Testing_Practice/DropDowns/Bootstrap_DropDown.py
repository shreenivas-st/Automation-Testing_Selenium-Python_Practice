import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service = serv_obj)
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/bootstrap-dropdown-example-for-selenium.html")

driver.find_element(By.ID, "menu1").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='About Us']").click()
time.sleep(5)

driver.close()