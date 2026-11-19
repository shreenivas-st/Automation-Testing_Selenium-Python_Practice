import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service = serv_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(4)
frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(frame)
frame1 = driver.find_element(By.XPATH, "//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']")
driver.switch_to.frame(frame1)
time.sleep(4)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Shreenivas")
time.sleep(5)
driver.close()