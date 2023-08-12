import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)
time.sleep(2)

xpath_url = '/html/body/div[1]/header/nav/div/a[2]'
signup = driver.find_element(by=By.XPATH,value=xpath_url)
signup.click()
time.sleep(2)
email = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
email.send_keys("sg9967780426@gmail.com")
passw = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
time.sleep(2)

passw.send_keys("Nitinbhavana@2003")
passw.send_keys(Keys.ENTER)
time.sleep(3)


all_list = driver.find_element(by=By.CSS_SELECTOR, value='#main .scaffold-layout__list-detail-inner .scaffold-layout__list .jobs-search-results-list .scaffold-layout__list-container')
print(type(all_list))
print(all_list.find_element(by=By.TAG_NAME, value="a").text)
# for li in all_list.find_elements(by=By.TAG_NAME, value="a"):
#
#     li.send_keys(Keys.ENTER)
#     try:
#     #/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button
#         easy_apply = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button')
#         easy_apply.click()
#         time.sleep(2)
#     except:
#         print("There is no element like this")
#     else:
#         try:
#             phone = driver.find_element(by=By.XPATH,
#                                         value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3590341680-1520724192550698529-phoneNumber-nationalNumber"]')
#             phone.send_keys(Keys.NUMPAD9, Keys.NUMPAD9, Keys.NUMPAD6, Keys.NUMPAD7, Keys.NUMPAD8, Keys.NUMPAD9,
#                             Keys.NUMPAD9, Keys.NUMPAD9, Keys.NUMPAD9, Keys.NUMPAD9, )
#             next = driver.find_element(by=By.XPATH,
#                                        value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
#             next.click()
#             time.sleep(2)
#         except:
#             print(Exception)
#
#     finally:
#         cut = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/button')
#         cut.click()
#
#         time.sleep(2)
#
#         discard_btn = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div/div[3]/button[1]')
#         discard_btn.click()
#         time.sleep(2)
#
#
#

driver.quit()








