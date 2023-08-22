from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(executable_path='./chromedriver')

chrome_driver = webdriver.Chrome(options=options, service=service)

chrome_driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Show Message' in chrome_driver.page_source
# assert 'Selenium Easy Demo' in chrome_driver.title
# btn_element = chrome_driver.find_element(By.CLASS_NAME, 'btn-primary')
# print(btn_element.get_attribute('innerHTML'))

user_input = chrome_driver.find_element(By.CSS_SELECTOR, '#user-message')
user_input.clear()
user_input.send_keys('I AM EXTRA COOOL')

btn_element = chrome_driver.find_element(By.CSS_SELECTOR, '.btn-primary')
btn_element.click()

output_message = chrome_driver.find_element(By.CSS_SELECTOR, '#display')
assert 'I AM EXTRA COOOL' in output_message.text

chrome_driver.close()
