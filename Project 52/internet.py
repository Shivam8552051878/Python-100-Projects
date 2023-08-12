import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager


class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = Chrome(service=Service(ChromeDriverManager().install()))
        self.down = 65.57
        self.up = 102.07

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        # //cokie ='onetrust-accept-btn-handler'
        #
        go_link = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_link.click()
        time.sleep(60)
        print("speed test finsih")
        try:
            down_speed = self.driver.find_element(by=By.XPATH,
                                                  value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
            up_speed = self.driver.find_element(by=By.XPATH,
                                                value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        except NoSuchElementException:
            time.sleep(30)
        else:
            print(down_speed.text, up_speed.text)
            self.down = float(down_speed.text)
            self.up = float(up_speed.text)
        finally:
            self.driver.quit()

    def tweet_at_provider(self):
        tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
        self.driver.get(url="https://twitter.com/")
        time.sleep(5)
        login_xpath = '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a'
        try:
            login = self.driver.find_element(By.XPATH,
                                             value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        except NoSuchElementException:
            login = self.driver.find_element(By.XPATH, value=login_xpath)

        login.click()
        time.sleep(10)
        base_window = self.driver.window_handles[0]
        print(base_window.title())
        try:
            login_window = self.driver.window_handles[1]
            print(login_window.title)
            time.sleep(5)
            self.driver.switch_to.window(login_window)
        except IndexError:
            print("No new window")
        finally:
            gmail_input = self.driver.find_element(by=By.XPATH,
                                                   value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            gmail_input.send_keys("demo8552051878@gmail.com")
            gmail_input.send_keys(Keys.ENTER)
            time.sleep(3)
            try:
                password = self.driver.find_element(by=By.XPATH,
                                                    value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                password.send_keys(os.environ.get("PASSWORD"))
                password.send_keys(Keys.ENTER)
            except NoSuchElementException:
                print("Not found password")
                time.sleep(8)
                user_name = self.driver.find_element(by=By.XPATH,
                                                     value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                user_name.send_keys("@Shivam20030219")
                user_name.send_keys(Keys.ENTER)
                time.sleep(8)
                password = self.driver.find_element(by=By.XPATH,
                                                    value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                password.send_keys("Zamia@2003")
                password.send_keys(Keys.ENTER)
            try:
                # self.driver.switch_to.window(base_window)
                time.sleep(30)
                tweet = self.driver.find_element(by=By.XPATH, value=tweet_xpath)
                tweet.click()
                time.sleep(10)
                massage = self.driver.find_element(by=By.XPATH,
                                                   value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div')
                massage.send_keys(f"my internet downloading speed is {self.down} and uploading speed is {self.up}")
                time.sleep(10)
                # '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
                tweet_button = self.driver.find_element(by=By.XPATH,
                                                        value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div[4]')
                tweet_button.click()


            except NoSuchElementException:
                print("Problem")
            except ElementClickInterceptedException:
                print("problem ")
                cross = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div')
                cross.click()
                time.sleep(5)
                discard = self.driver.find_element(by=By.XPATH,
                                                   value='//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]')
                discard.click()
                time.sleep(5)

            finally:
                menu = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div'
                menu_find = self.driver.find_element(by=By.XPATH,
                                                     value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div')
                menu_find.click()
                time.sleep(10)

                # logut_a = '//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]'
                logut_a = self.driver.find_element(by=By.XPATH,
                                                   value='//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]')
                logut_a.click()
                print("Logout procces start")
                time.sleep(10)

                logut_button = self.driver.find_element(by=By.XPATH,
                                                        value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]')
                logut_button.click()
                time.sleep(10)
                self.driver.quit()


