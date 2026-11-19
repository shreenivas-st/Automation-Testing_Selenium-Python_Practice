import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID, "txtDate").click()
month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month.select_by_visible_text("May")
time.sleep(3)
year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
year.select_by_visible_text("2018")
time.sleep(3)

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for d in dates:
    if d.text == "1":
        d.click()
        break

time.sleep(5)
driver.close()


time.sleep(5)
driver.close()