import time

URL = "https://tinder.com/"
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url=URL)
time.sleep(3)

login = driver.find_element(by=By.LINK_TEXT, value="Log in")
login.click()
time.sleep(5)
try:
    more_option = driver.find_element(by=By.XPATH, value='//*[@id="q43969269"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
    more_option.click()
    time.sleep(15)
    facebook = driver.find_element(by=By.XPATH,value='//*[@id="q43969269"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    facebook.click()
    time.sleep(13)
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    time.sleep(3)

    singin_phone = driver.find_element(by=By.ID, value='email')
    singin_phone.send_keys(Keys.NUMPAD8 ,Keys.NUMPAD5, Keys.NUMPAD5, Keys.NUMPAD2, Keys.NUMPAD0, Keys.NUMPAD5, Keys.NUMPAD1, Keys.NUMPAD8, Keys.NUMPAD7, Keys.NUMPAD8)
    singin_pass = driver.find_element(by=By.ID, value='pass')
    singin_pass.send_keys("Zamia@2003")
    time.sleep(10)

    singin_pass.send_keys(Keys.ENTER)
    time.sleep(10)
    base_window = driver.window_handles[0]
    driver.switch_to.window(base_window)
#//*[@id="email"]
except NoSuchElementException:
    print("Not Found")

driver.quit()