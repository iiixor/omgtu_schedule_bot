def get_today_horoscope(sign):
    import requests
    import fake_useragent
    from bs4 import BeautifulSoup

    link = f"https://horo.mail.ru/prediction/{sign}/today/"
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')

    block = soup.find('div', class_ = 'article__text')

    # print(block.text)

    return block.text
