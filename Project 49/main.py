from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

CHROME_DRIVER_PATH = "C:/Users/kdlte/Python 100 Project/Chrome Driver/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://stackoverflow.com/questions/37400974/error-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3")
x_path = "//*[@id='footer']/div/nav/div[2]/h5/a"
path = driver.find_element(by="xpath",value=x_path)
print(path.get_attribute("href"))
driver.quit()