from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
"""
browser_dict = {'chrome':"C:\myDrivers\chromedriver_win32\chromedriver.exe",'firefox':"C:\myDrivers\geckodriver-v0.32.0-win32.exe"}
#browser_name = request.config.getOption("browser_name")
browser_name = "firefox"
for key, val in browser_dict.items():
    if key == browser_name:
        print(key, val)
"""
service_obj = Service("C:\myDrivers\geckodriver-v0.32.0-win32.geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.maximize_window()
