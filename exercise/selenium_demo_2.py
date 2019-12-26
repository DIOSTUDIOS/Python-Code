from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')

login = browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')
login.click()
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="J_QRCodeLogin"]/div[5]/a[1]')))

login = browser.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]')
login.click()

browser.find_element_by_xpath('//*[@id="J_Form"]/div[2]/span').send_keys('云逸苍穹')
browser.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys(r'W4585z5430q3931?')
browser.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()

print(browser.current_url)