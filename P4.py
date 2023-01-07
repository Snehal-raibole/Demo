from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\myDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

options = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for option in options:
    if option.get_attribute("value") == "option2":
        option.click()
        assert option.is_selected()
        break

radio_buttons = driver.find_elements(By.CSS_SELECTOR, 'input[class="radioButton"]')
for btn in radio_buttons:
    if btn.get_attribute("value") == "radio3":
        btn.click()
        assert btn.is_selected()
        break

radio_buttons[1].click()
assert radio_buttons[1].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(2)

#alerts or handling the pop
name = "Snehal"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert name in alert_text
alert.accept()
#alert.dismiss()





time.sleep(3)
