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

case_1 = [locators.loc_open_brack,
          locators.loc_1,
          locators.loc_plus,
          locators.loc_2,
          locators.loc_close_brack,
          locators.loc_multiply,
          locators.loc_3,
          locators.loc_minus,
          locators.loc_4,
          locators.loc_0,
          locators.loc_divide,
          locators.loc_5,
          locators.loc_equals]

for element in case_1:
    elem = browser.find_element(By.XPATH, element)
    elem.click()

answer = browser.find_element(By.CSS_SELECTOR, '#cwos')
assert '1' == answer.text

browser.close()
