import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service = serv_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
time.sleep(3)
frame = driver.find_element(By.ID, "singleframe")
driver.switch_to.frame(frame)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Shreenivas")
time.sleep(4)
driver.switch_to.default_content()
driver.close()
