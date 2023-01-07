import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\myDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

url = "https://rahulshettyacademy.com/dropdownsPractise"
driver.get(url)

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

web_countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
for country in web_countries:
    if country.text == "India":
        country.click()
        break
time.sleep(2)
#this wont work when we change the value dynamically with script, it still gives the value when the page loads first time which is null in this case.
#print(driver.find_element(By.ID, "autosuggest").text())

#get_attribute("value") comes from java
#print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

#to validate TC TRUE/FALSE assert is used: If condition is false TC is failed, if condtion is true TC is passed
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
driver.close()



