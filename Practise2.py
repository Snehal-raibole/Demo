import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\myDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.implicitly_wait(10)

Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")).select_by_value("option3")
time.sleep(3)

