from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#initialize chrome browser with this pre-conditions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
#chrome_options.add_argument("headless")

#Execute the driver with a specific webpage call
service_obj = Service("C:\myDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(10)

url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)

#go to shop page
driver.find_element(By.CSS_SELECTOR, '.nav-link[href="/angularpractice/shop"]').click()


#access all the elements
browser_elements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
#access phone title
# find specific element from above item_title list "iphoneX"

#for item in item_title:
    #if item == required_item:
required_item = "Blackberry"


for element in browser_elements:
    element_title = element.find_element(By.XPATH, "div/h4/a").text

    if element_title == required_item :
        element.find_element(By.XPATH, "div/button").click()   ##add to cart "element"

#scrollup the page and do the checkout
driver.execute_script("window.scrollBy(0, 0);")
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

#on checkout page validate the total > 0
total = driver.find_element(By.CSS_SELECTOR, "h3 strong").text
if  int(total.lstrip("₹. ")) > 0:
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()  #on checkout page do the checkout

#do the Purchase and grab success msg
address = "ind"
driver.find_element(By.CSS_SELECTOR, "#country").send_keys(address)

wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

success_mesg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert "Success! Thank you" in success_mesg

