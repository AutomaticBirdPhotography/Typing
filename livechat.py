from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time
options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

PATH = "C:/Users/04rob/Downloads/chromedriver.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)

driver.get("https://www.livechat.com/typing-speed-test/#/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/span/div[1]/h2'))

)
time.sleep(1)

for i in range(1,1000):
    element = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]').text
    keyboard.write(element)
    keyboard.write(" ")
    