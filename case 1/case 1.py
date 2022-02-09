from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe'

browser = webdriver.Chrome(executable_path=path)
browser.get(url='https://www.google.com/')
elem = browser.find_element(By.NAME, 'q')
elem.send_keys('Калькулятор')
elem.send_keys(Keys.RETURN)
assert 'Калькулятор' in browser.title

elem = browser.find_element(By.XPATH, '//*[text()="("]')
elem.click()
elem = browser.find_element(By.XPATH, '//*[text()="1"]')
elem.click()
elem = browser.find_element(By.XPATH, '//*[text()="+"]')
elem.click()
elem = browser.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/'
                                      'div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div')
elem.click()
elem = browser.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/'
                                      'div/div/div[3]/div/table[2]/tbody/tr[1]/td[2]/div/div')
elem.click()
elem = browser.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/'
                                      'div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div')
elem.click()
elem = browser.find_element(By.XPATH, '//*[text()="3"]')
elem.click()
elem = browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/'
                                      'td[4]/div/div')
elem.click()
elem = browser.find_element(By.XPATH, '//*[text()="4"]')
elem.click()
elem = browser.find_element(By.XPATH, '//*[text()="0"]')
elem.click()
elem = browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[2]/'
                                      'td[4]/div/div')
elem.click()
elem = browser.find_element(By.XPATH, '//*[text()="5"]')
elem.click()
elem = browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/'
                                      'td[3]/div/div')
elem.click()
answer = browser.find_element(By.CSS_SELECTOR, '#cwos')
assert '1' == answer.text

browser.close()
