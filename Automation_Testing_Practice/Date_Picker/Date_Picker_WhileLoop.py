import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

month = "April"
year = "2022"
date = "1"

driver.find_element(By.ID, "datepicker").click()
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()
time.sleep(5)

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for d in dates:
    if d.text == date:
        d.click()
        break

time.sleep(5)
driver.close()

