import pymongo
import time
import re
import requests


def get_url():
    mg_linker = pymongo.MongoClient(host='localhost', port=27017)
    mg_databs = mg_linker['ppt_links']
    mg_gather = mg_databs['first_ppt_links']

    urls = mg_gather.find()

    return urls


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}


def download(urls):
    count = 401
    for url in urls:
        # print(url['url'])
        # url = r'http://www.1ppt.com/article/59009.html'
        response = requests.get(url['url'], headers)

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
    urls = get_url()
    download(urls)
    pass
