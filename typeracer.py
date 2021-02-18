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

driver.get("https://play.typeracer.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/div[1]/h3'))
)
time.sleep(4)
keyboard.press_and_release('ctrl+alt+i')
time.sleep(5)

bokstav = driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]').text
print(bokstav)

rest = driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]').text
print(rest)

allt = driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]').text
print(allt)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Go!')]"))
)

skriv = driver.find_element_by_xpath('//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input').click()
time.sleep(0.1)
keyboard.write(bokstav)
keyboard.write(rest, delay=0.01)
keyboard.write(" ")
time.sleep(0.1)
keyboard.write(allt, delay=0.033)