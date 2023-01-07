import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\myDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

url = "https://rahulshettyacademy.com/seleniumPractise/#/"
driver.get(url)
# wait for 5sec till the conditon matches, if condition matched in 2 sec it will proceed further. If condition didnt matched in 5sec TC will fail
# applied for all the steps in script max wait time is 5sec here.
driver.implicitly_wait(2)

itemstobuy_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg', 'Blueberry - 1 kg']
items_list = []


driver.find_element(By.XPATH, '//input[@class="search-keyword"]').send_keys("ber")
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# implicite_wait is not applicable to find_elements as it check for just the action item.
#empty list is task done for implicite_wait so we have to use time.sleep() to allow list to populate.
time.sleep(2)
results = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
print(len(results))
assert len(results) > 0

#Compair the list with itemstobuy_list
for result in results:
    items_list.append(result.find_element(By.XPATH, 'h4').text)
    result.find_element(By.XPATH, 'div/button').click()

print(items_list)
for itemtobuy in itemstobuy_list:
    if itemtobuy in items_list:
        print(itemtobuy, " added to cart")
    else:
        print(itemtobuy, " not available")

driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()


#do the sum of all the product
prices = driver.find_elements(By.XPATH, '//td[5]/p')
sum = 0
for price in prices:
    sum = sum + int(price.text)

total_amount = int(driver.find_element(By.CSS_SELECTOR, 'span[class="totAmt"]').text)
assert sum == total_amount



#apply the promocode and wait for its validation with explicite wait
driver.find_element(By.CLASS_NAME, 'promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

#ExpliciteWait for special condtion which take more time to excute other than all steps and we have to wait for this condition specificaly for certain duration
#the moment condition met it proceed further, without waiting anylonger. apllied to specific condition
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

promostatus = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(promostatus)

#calculate the discount after promocode

discount = driver.find_element(By.CSS_SELECTOR, 'span[class="discountPerc"]').text
if '%' in discount:
    discount = float(discount.rstrip('%'))

print(discount)

mytotal_after_discount = sum - (sum * (discount/100))

total_after_discount = float(driver.find_element(By.CLASS_NAME, 'discountAmt').text)

assert mytotal_after_discount == total_after_discount

#Place an order
print("total is matched:", total_after_discount)
driver.find_element(By.XPATH, '//button[text()="Place Order"]').click()

#select location for delivery
countries = driver.find_element(By.XPATH, '//div[@class="wrapperTwo"]/div/select').click()
time.sleep(3)

