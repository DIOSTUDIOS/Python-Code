from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()

if __name__ == '__main__':
    try:
        browser.get(r'https://www.whzh-cw.com/chapter.html?1#mybookid=91514&bookid=95311&chapterid=42037433')
        text = browser.find_element_by_id('txt')
        keywords.send_keys('Python')
        keywords.send_keys(Keys.ENTER)

        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)
    finally:
        browser.close()