import time

from zillow import Zillow
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# data = Zillow()
data_list = [{"address":"313 amdkx amdknxkw",
              "url":"https//www.google.com",
              "price"
              :"$145216"
},{"address":"313 amdkx amdknxkw",
              "url":"https//www.google.com",
              "price"
              :"$145216"
}]
print(data_list)
if len(data_list) > 0:
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSftw2JkYAqLswpd4Tuv-Z3jtcAeTzUpXvOFfFDPM10_e2agpA/viewform?usp=sf_link")
    time.sleep(10)

    for data in data_list:
        address_input = driver.find_element(by=By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = driver.find_element(by=By.XPATH,
                                          value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = driver.find_element(by=By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

        address_input.send_keys(data["address"])
        link_input.send_keys(data["url"])
        price_input.send_keys(data["price"])
        submit_button.click()
        time.sleep(10)
        another_response = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_response.click()
        time.sleep(5)

    driver.get("https://docs.google.com/forms/d/1ODp3Zl9QhZXDlkph3Sh1AvfTVpHAazZF2qbrqHWxohg/edit?pli=1#responses")
    driver.find_element()