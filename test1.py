from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service('C:\myDrivers\chromedriver_win32.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get("http://google.com")

