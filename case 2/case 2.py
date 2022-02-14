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

case_2 = [locators.loc_6,
          locators.loc_divide,
          locators.loc_0,
          locators.loc_equals,
          ]

for element in case_2:
    elem = browser.find_element(By.XPATH, element)
    elem.click()

answer = browser.find_element(By.CSS_SELECTOR, '#cwos')
assert 'Infinity' == answer.text

browser.close()
