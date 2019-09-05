import requests
import re


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }


def get_page_urls():
    url = r'https://www.kuaikanmanhua.com/web/topic/4/'

    response = requests.get(url=url, headers=headers)

    pattern = r'<div class="title fl"><a href="(.*?)"><span>'
    result = re.findall(pattern=pattern, string=response.text, flags=re.I)

    urls = []

    for i in range(len(result)):
        urls.append(r'https://www.kuaikanmanhua.com' + result[i])

    urls.reverse()

    return urls

    pass


def get_images_urls():
    page_urls = get_page_urls()

    response = requests.get(url=page_urls[0], headers=headers)

    pattern = r'<img noinit="true" class="img" data-src="http://p1.kkmh.com/image/150909/wh4g61buz.jpg?sign=3f7fc3757d9c2524fe86381ed08c5101&amp;t=5d541adb" src="(.*?)" lazy="loaded">'
    result = re.findall(pattern=pattern, string=response.text, flags=re.I)
    print(result)
    # print(response.text)


if __name__ == '__main__':
    get_images_urls()

    pass
