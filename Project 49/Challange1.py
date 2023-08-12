from selenium import webdriver
CHROME_DRIVER_PATH = "C:/Users/kdlte/Python 100 Project/Chrome Driver/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url="https://www.python.org/")
XPATH = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'

ul_element = driver.find_element(by="xpath", value=XPATH)
data = ul_element.text.split("\n")

dic = {}
count = 0

for i in range(0, len(data), 2):
    dic[count] = {
        "time":data[i],
        "name":data[i+1]
    }
    count += 1
print(dic)


