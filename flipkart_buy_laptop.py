from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait


service_obj = Service('C:\myDrivers\chromedriver_win32.exe')
driver = webdriver.Chrome(service=service_obj)
url = "https://confluence.community.veritas.com/login.action?os_destination=%2Fpages%2Fviewpage.action%3FpageId%3D311289684&permissionViolation=true"
driver.get(url)
driver.find_element(By.XPATH, "//body[@id='com-atlassian-confluence']").send_keys("snehal.raibole")
driver.find_element(By.XPATH, "//input[@id='os_password']").send_keys("Akshay@05031993")
driver.find_element(By.CSS_SELECTOR, "label[for='os_cookie']").click()
driver.find_element(By.ID, "loginButton").click()
driver.implicitly_wait(15.00)
