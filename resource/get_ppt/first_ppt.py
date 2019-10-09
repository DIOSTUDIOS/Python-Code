import requests
import time
import re
import pymongo


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}


def get_ppt_details(page):
    access = r'http://www.1ppt.com/xiazai/ppt_xiazai_' + str(page) + '.html'
    response = requests.get(access, headers)

    pattern = r'<h2><a href="(.*?)" target="_blank">.*?</a></h2>'

    links = re.findall(pattern, response.text, re.S)

    for item in links:
        insert_into_database(item)

    time.sleep(3)


def insert_into_database(link):
    mg_linker = pymongo.MongoClient(host='localhost', port=27017)
    mg_databs = mg_linker['ppt_links']
    mg_gather = mg_databs['first_ppt_links']

    mg_gather.insert_one({'url': r'http://www.1ppt.com' + link})


if __name__ == '__main__':
    page = 1
    while page < 115:
        print(page)

        get_ppt_details(page)

        page += 1
