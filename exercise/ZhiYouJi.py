from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time


def structure_url(job='测试工程师', city='哈尔滨', degree='本科', sort='last', page='1'):
    url = (
        'https://www.jobui.com/jobs'
        '?jobKw={:s}'
        '&cityKw={:s}'
        '&degreeType={:s}'
        '&sortField={:s}'
        '&n={:s}'
        .format(job, city, degree, sort, page)
    )

    return url


def spider(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    wait = WebDriverWait(browser, 10)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'job-search-word')))

    jobs = browser.find_elements(By.CLASS_NAME, 'job-name> h3')
    salaries = browser.find_elements(By.CLASS_NAME, 'job-pay-text')
    companies = browser.find_elements(By.CLASS_NAME, 'job-company-name')
    links = browser.find_elements(By.CLASS_NAME, 'job-name')

    for i in range(len(links)):
        print(jobs[i].text, end='\t')
        print(salaries[i].text, end='\t')
        print(companies[i].text, end='\t')
        print(links[i].get_attribute('href'))

    browser.close()


if __name__ == '__main__':
    url = structure_url()
    spider(url)
