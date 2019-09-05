# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import pymongo


def structure_url(location='北京', page=1):
    url = (
            'https://piao.qunar.com/ticket/list.htm'
            '?keyword={:s}'
            '&region='
            '&from=mps_search_suggest'
            '&sort=pp'
            '&page={:s}'.format(location, str(page))
           )

    return url


def insert_to_mongodb(datum):
    mg_linker = pymongo.MongoClient(host='localhost', port=27017)
    mg_databs = mg_linker['menpiao']
    mg_gather = mg_databs['qunaer']

    mg_gather.insert_one(datum)


def get_scenic_information(url):
    browser = webdriver.Chrome()
    browser.get(url=url)

    wait = WebDriverWait(browser, 10)
    wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="searchValue"]')))

    names = browser.find_elements_by_class_name('name')
    sites = browser.find_elements_by_class_name('address > span')
    costs = browser.find_elements_by_class_name('sight_item_price > em')
    sales = browser.find_elements_by_class_name('hot_num')

    for i in range(15):
        datum = {
                    "name": names[i].text,
                    "site": sites[i].text,
                    "cost": costs[i].text,
                    "sale": sales[i].text
                }

        insert_to_mongodb(datum)

    browser.close()


locations = [
                '海南', '广东', '广西',
                '上海', '江西', '山东', '浙江', '安徽', '江苏', '福建',
                '湖北', '湖南', '河南',
                '黑龙江', '吉林', '辽宁',
                '云南', '重庆', '四川', '贵州', '西藏',
                '北京', '天津', '河北', '山西', '内蒙古',
                '新疆', '宁夏', '甘肃', '陕西', '青海',
                '香港', '台湾', '澳门'
            ]


if __name__ == '__main__':
    for location in locations:
        url = structure_url(location=location)

        get_scenic_information(url)
