import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH = "chefsteps"
INSTA_ID = "__demo__2003"
PASSWORD = os.environ.get("PASSWORD")


class InstagramBot():
    def __init__(self):
        self.driver = Chrome(service=Service(ChromeDriverManager().install()))

    def run(self):
        self.driver.get("https://www.instagram.com/")
        try:
            username = WebDriverWait(
                self.driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[name='username']")))

            # target Password
            password = WebDriverWait(
                self.driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[name='password']")))
            # enter username and password
            username.clear()
            username.send_keys(INSTA_ID)
            password.clear()
            password.send_keys(PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(10)
        #     //*[@id="mount_0_0_ZC"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a
            search = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div')
            search.click()
            time.sleep(5)
            search_input = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
            search_input.send_keys(SEARCH)
            search_input.send_keys(Keys.ENTER)
            time.sleep(2)
            checf = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a')
            checf.send_keys(Keys.ENTER)
            time.sleep(10)
            followers = self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="followers")
            followers.click()
            time.sleep(5)

            # # class button _acan _acap _acas _aj1-
            # button = self.driver.find_elements(by=By.CSS_SELECTOR, value="button")
            # print(len(button))
            # for btn in button:
            #     if btn.text == "Follow":
            #         btn.find_element(by=By.CLASS_NAME, value="_acan _acap _acas _aj1-").click()
            #         time.sleep(5)//*[@id="mount_0_0_kl"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]
            modal = self.driver.find_element(by=By.XPATH, value='//*[@id="mount_0_0_vQ"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]')
            # print(len(modal))
            for i in range(10):
                # In this case we're executing some Javascript, that's what the execute_script() method does.
                # The method can accept the script as well as a HTML element.
                # The modal in this case, becomes the arguments[0] in the script.
                # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
                self.driver.execute_script(f"arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            self.driver.quit()
        except NoSuchElementException:
            print("HEllO ")


cls = InstagramBot()
cls.run()