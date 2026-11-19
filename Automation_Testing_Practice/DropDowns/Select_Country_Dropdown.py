import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service = serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

country = driver.find_element(By.ID, "country")
Country = Select(country)
Country.select_by_visible_text("India")
time.sleep(5)

all_option = Country.options
print("Number of options:", len(all_option))

print("All Options List.....")
for opt in all_option:
    print(opt.text)

time.sleep(5)
driver.close()