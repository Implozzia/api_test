import requests


def redirect(response):
    count_of_redirections = 0
    if response.history:
        print('Request was redirected')
        for resp in response.history:
            count_of_redirections += 1
            print(resp.url, resp.status_code)
        return print(f'Final destination: {response.url}, Status Code: {response.status_code}, Count of redirections: {count_of_redirections}')
    else:
        return print('Request was not redirected')


res = requests.get('https://playground.learnqa.ru/api/long_redirect')
redirect(res)


# Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect С
# помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки
# назначения до итоговой. И какой URL итоговый. Ответ опубликуйте в виде ссылки на коммит со скриптом,
# а также укажите количество редиректов и конечный URL.




