import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(service=Service(ChromeDriverManager().install()))
URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url=URL)
time.sleep(8)
english_lang = driver.find_element(by=By.ID, value="langSelect-EN")
english_lang.click()
time.sleep(8)
cookie = driver.find_element(by=By.ID, value="bigCookie")
# for i in range(12000):
#     cookie.click()
products = driver.find_element(by=By.ID, value="products")
print(products.text)

# for i in products.find_elements():

# time.sleep(100)

driver.quit()