import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

Rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
print("Total Number of Rows : ", Rows)

Columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))
print("Total Number of Columns : ", Columns)

data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[6]/td[2]")
print(data.text)

print("Read All the data in table")

for r in range (2,Rows+1):
    for c in range (1, Columns+1):
        allData = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(allData,end="        ")
    print()


time.sleep(4)
driver.close()
