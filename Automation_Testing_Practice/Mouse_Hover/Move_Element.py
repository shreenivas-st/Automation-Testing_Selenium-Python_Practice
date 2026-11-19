import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


serv_obj = Service ('D:/Shreenivas/Project/Selenium_Python/Automation_Testing_Practice/Drivers/chromedriver.exe')
driver = webdriver.Chrome (service=serv_obj)
driver.maximize_window()
driver.get("https://vinothqaacademy.com/mouse-event/")
time.sleep(3)

DemoSite = driver.find_element(By.XPATH, "//div[@class='collapse navbar-collapse pull-right']//a[contains(text(),'Demo Sites')]")
Practice_Automation = driver.find_element(By.XPATH, "//div[@class='collapse navbar-collapse pull-right']//a[contains(text(),'Practice Automation')]")
Mouse_Event = driver.find_element(By.XPATH, "//div[@class='collapse navbar-collapse pull-right']//a[normalize-space()='Mouse Event']")
time.sleep(5)

action = ActionChains(driver)
action.move_to_element(DemoSite).move_to_element(Practice_Automation).click(Mouse_Event).perform()


time.sleep(5)
driver.close()
