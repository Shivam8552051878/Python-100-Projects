from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:/Users/kdlte/Python 100 Project/Chrome Driver/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
response = driver.get("https://en.wikipedia.org/wiki/Main_Page")
article = driver.find_element(by.By.XPATH, value='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]')
# print(article.text)
# article.click()
search = driver.find_element(by.By.NAME, value="search")
# print(type(search))
search.send_keys("Python")
search.send_keys(Keys.ENTER)
search.click()
driver.quit()