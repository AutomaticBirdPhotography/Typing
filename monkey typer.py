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

driver.get("https://monkeytype.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "words"))

)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="top"]/div[3]/div[4]/div/div[1]').click()
time.sleep(1)



for i in range(1,500):
    element = driver.find_element_by_css_selector("div.word.active").text
    print(element)
    keyboard.write(element)
    keyboard.write(" ")
    #time.sleep(0.05)
 