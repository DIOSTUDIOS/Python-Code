import requests
import re
import sqlite3
import time


def create_database():
    db_link = sqlite3.connect('spider_one.db')
    db_csor = db_link.cursor()

    db_csor.execute(r'''
        CREATE TABLE URLS
        (
            ID INTEGER AUTHORIZATION,
            DETAIL_URL NVARCHAR(999)
        )
    ''')

    db_csor.close()
    db_link.close()


def insert_into_db(detail_url):
    db_link = sqlite3.connect('spider_one.db')
    db_csor = db_link.cursor()

    db_csor.execute(r"INSERT INTO URLS(DETAIL_URL) VALUES('{:s}')".format(r'http://www.1ppt.com' + detail_url))

    db_csor.close()

    try:
        db_link.commit()
    except:
        db_link.rollback()
    finally:
        db_link.close()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}


def get_ppt_details(page):
    access = r'http://www.1ppt.com/xiazai/ppt_xiazai_' + str(page) + '.html'
    response = requests.get(access, headers)

    pattern = r'<h2><a href="(.*?)" target="_blank">.*?</a></h2>'

    links = re.findall(pattern, response.text, re.S)

    for item in links:
        insert_into_db(item)

    time.sleep(3)


def get_ppt_download_address():
    db_link = sqlite3.connect('spider_one.db')
    db_csor = db_link.cursor()

    db_csor.execute(r'SELECT DETAIL_URL FROM URLS')
    urls = db_csor.fetchall()

    db_csor.close()
    db_link.close()

    # print(urls[10][0])
    # print(len(urls))

    return urls


def downloader(urls):
    count = 1679
    for url in urls:
        # print(url[0])
        response = requests.get(url[0], headers)

        pattern = r'<li><a href="(.*?)" target="_blank"> .*? </a></li>'
        file_url = re.findall(pattern, response.text, re.S)

        print(count, end='\t')
        print(file_url)

        time.sleep(1)

        zip_file = requests.get(file_url[0], headers).content
        with open(r'D:\下载\\' + str(count) + '.zip', 'wb') as file:
            file.write(zip_file)

        time.sleep(4)

        count += 1


if __name__ == '__main__':
    urls = get_ppt_download_address()

    downloader(urls)
