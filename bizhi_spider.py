from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import datetime


access = r'https://sj.enterdesk.com/bizhi/41599.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}
new_access = ''


def main():
    is_continue = True
    image_count = 0

    browser = webdriver.Chrome(chrome_options=webdriver.ChromeOptions().add_argument('--headless'))
    browser.get(url=access)

    while is_continue:
        try:
            wait = WebDriverWait(browser, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div[1]/div[2]/img')))

            url = browser.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]/img').get_attribute('src')
            # print(url)

            image = requests.get(url, headers).content
            # print(image)
            with open(r'D:\下载\\' + url[40:], 'wb') as file:
                file.write(image)
        except TimeoutError:
            print('time out')
        finally:
            browser.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]/img').click()


        image_count += 1

        if image_count < 999:
            is_continue = True
        else:
            is_continue = False

    global new_access
    new_access = browser.current_url

    browser.close()


if __name__ == '__main__':
    print(datetime.datetime.now())
    main()
    print(new_access)
    print(datetime.datetime.now())