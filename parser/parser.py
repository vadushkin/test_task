import json

import requests
from bs4 import BeautifulSoup


def parser_yandex(url: str) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    div_items = soup.find_all("div", class_='news-list__item')[:10]

    urls = []

    for item in div_items:
        urls.append('https://market.yandex.ru' + item.find('a').get('href'))

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        div_title = soup.find('div', class_='news-info__title')
        title = div_title.text

        div_tag = soup.find('div', class_='news-info__tags')
        div_a = div_tag.find_all('a')
        tags = []
        for a in div_a:
            tags.append(a.text)

        date = soup.find('time', class_='news-info__published-date').text

        data = {
                   'title': title,
                   'url': url,
                   'tags': tags,
                   'date': date,
               },

        with open('output_yandex.json', 'a') as for_write:
            json.dump(data,
                      for_write,
                      indent=4,
                      ensure_ascii=False, )
            for_write.write(',\n')


def parser_ozon(url: str) -> None:
    response = requests.get(url)
    data = response.json()
    with open('output_ozon.json', 'a') as for_write:
        json.dump(data,
                  for_write,
                  indent=4,
                  ensure_ascii=False, )
        for_write.write(',\n')


def main():
    parser_yandex('https://market.yandex.ru/partners/news')
    # parser_ozon('https://seller.ozon.ru/content-api/news/?_limit=10')


if __name__ == '__main__':
    main()
