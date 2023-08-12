from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:/Users/kdlte/Python 100 Project/Chrome Driver/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)
button = driver.find_element(by=by.By.ID, value="cookie")
portal = driver.find_element(by=by.By.ID,value="buyMine")


print(button.parent)
run = True
count = 0
while run:
    button.click()
    if count == 7000:
        run = False
    if count == 5:
        portal.click()
        count = 0
    count += 1
driver.quit()