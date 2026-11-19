import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://vinothqaacademy.com/mouse-event/")

Button = driver.find_element(By.ID, "rightBtn")
Copy = driver.find_element(By.XPATH, "//button[normalize-space()='Copy']")
act = ActionChains (driver)
act.context_click(Button).click(Copy).perform()
time.sleep(5)

driver.close()