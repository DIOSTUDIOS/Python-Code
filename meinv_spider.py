from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import datetime

# 初始 url
access = r'http://www.win4000.com/meinv185222.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}

new_access = ''


def main():
    is_continue = True
    # 图片计数器
    image_count = 0
    # 设置浏览器对象，并获取网页内容
    browser = webdriver.Chrome(chrome_options=webdriver.ChromeOptions().add_argument('--headless'))
    browser.get(url=access)
    # 判断是否继续执行
    while is_continue:
        try:
            # 延时等待
            wait = WebDriverWait(browser, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pic-meinv"]/a/img')))
            # 获取图片地址
            url = browser.find_element_by_xpath('//*[@id="pic-meinv"]/a/img').get_attribute('url')
            # 下载图片
            image = requests.get(url=url, headers=headers).content
            with open(r'D:\我的图片' + url[32:], 'wb') as file:
                file.write(image)
        except TimeoutError:
            print('time out')
        finally:
            browser.find_element_by_xpath('//*[@id="pic-meinv"]/a/img').click()

        image_count += 1
        # 设置想要下载的图片的数量
        if image_count < 5:
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