from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import locators

path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'

browser = webdriver.Chrome(executable_path=path)
browser.get(url='https://www.google.com/')
elem = browser.find_element(By.NAME, 'q')
elem.send_keys('Калькулятор')
elem.send_keys(Keys.RETURN)
assert 'Калькулятор' in browser.title

elem = browser.find_element(By.XPATH, locators.loc_sin)
elem.click()
elem = browser.find_element(By.XPATH, locators.loc_equals)
elem.click()

answer1 = browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/span')
answer2 = browser.find_element(By.XPATH, '//*[@id="cwos"]')

assert 'sin() =' in answer1.text
assert 'Error' in answer2.text

browser.close()
