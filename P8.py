import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('C:\myDrivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

url = "https://the-internet.herokuapp.com/iframe"
driver.get(url)
driver.implicitly_wait(5)

#switch to FRAME from html
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.CSS_SELECTOR, '#tinymce').clear()
driver.find_element(By.CSS_SELECTOR, '#tinymce').send_keys("I am automating this frame")
time.sleep(5)

#switching back from frame to html page
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, 'h3').text)

