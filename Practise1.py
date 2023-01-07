from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import random

couponList = ["ABC", "DEF", "IJK", "LMN"]

service_obj = Service("C:\myDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

url = "https://rahulshettyacademy.com/seleniumPractise/#/"
driver.get(url)
driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[1]").click()
driver.find_element(By.XPATH, "//h4[normalize-space()='Cucumber - 1 Kg']").click()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(5) > button:nth-child(1)").click()
driver.implicitly_wait(10)


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()


#driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter promo code']".format(random.choice(couponList)))
#driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
driver.implicitly_wait(10)

driver.close()








