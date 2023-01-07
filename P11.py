from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--start-maximized")


service_obj = Service('C:\myDrivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj, options=chrome_options)


url = 'https://rahulshettyacademy.com/seleniumPractise/#/offers'
driver.get(url)
driver.implicitly_wait(5)

veggiesItemList = []

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggiesBrowserList = driver.find_elements(By.XPATH, "//tr/td[1]")
for item in veggiesBrowserList:
       veggiesItemList.append(item.text)

print(veggiesItemList)



oriveggiesItemList  = veggiesItemList.copy()
print(oriveggiesItemList)

veggiesItemList.sort()
assert oriveggiesItemList == veggiesItemList

print(driver.title)
print(driver.get_screenshot_as_file("pic2.png"))

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

