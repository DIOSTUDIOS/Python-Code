import requests
import re


def spider():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36'
    }
    response = requests.get(url=r'http://wabcw.info/?paged=3', headers=headers)
    pattern = '<a href="http://wabcw.info/\?p=\d+" rel="bookmark" ' \
              'title="Permanent Link to .*?">(.*?)</a>'

    titles = re.findall(pattern, response.text, re.S)

    pattern = '<p><strong><a href="(.*?)" target="_blank">.*?</a></strong></p>'
    links = re.findall(pattern, response.text, re.S)

    print(titles)


if __name__ == '__main__':
    spider()
    pass
