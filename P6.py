import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service('C:\myDrivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

url = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()

assert driver.find_element(By.ID, 'mousehover').is_displayed()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()
time.sleep(3)

select = Select(driver.find_element(By.XPATH, '//select[@id="dropdown-class-example"]'))
select.select_by_index(2)

time.sleep(3)


