from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    browser = webdriver.Chrome(executable_path=r'C:\Python37\Scripts\chromedriver.exe',options=options)
    browser.get(r'https://www.taobao.com/')

    wait = WebDriverWait(browser, 10)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'h')))

    login = browser.find_element_by_class_name('h')
    login.click()

    logon = browser.find_element_by_class_name('J_Quick2Static')
    logon.click()

    username = browser.find_element_by_id('TPL_username_1')
    username.send_keys('云逸苍穹')

    time.sleep(1)

    password = browser.find_element_by_id('TPL_password_1')
    password.send_keys('W4585z5430q3931?')

    time.sleep(1)

    submin = browser.find_element_by_id('J_SubmitStatic')
    submin.click()

    time.sleep(3)

    browser.close()