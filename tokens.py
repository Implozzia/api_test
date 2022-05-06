import requests
import time


def new_task():
    response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job').text.split('"')
    token = response[3]
    print('Received a token!')
    return token


def get_status():
    payload = {'token': new_task()}
    print('Request before job is done:')
    response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload).text
    print(response)
    print('Waiting ...')
    response = response.split('"')
    if response[3] == 'Job is NOT ready':
        time.sleep(10)
        response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload).text
        print('Response after job is done:')
        response_text = response.split('"')
        status = response_text[7]
        result = response_text[1]
        assert status == "Job is ready", "Incorrect status"
        assert result == 'result', "Don't have Status field"
        print(response)


get_status()


# Сам API-метод находится по следующему URL: https://playground.learnqa.ru/ajax/api/longtime_job
#
# Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со следующими полями:
#
# * seconds - количество секунд, через сколько задача будет выполнена
# * token - тот самый токен, по которому можно получить результат выполнения нашей задачи
#
# Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:
#
# * error - будет только в случае, если передать token, для которого не создавалась задача. В этом случае в ответе будет следующая надпись - No job linked to this token
# * status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
# * result - будет только в случае, если задача готова, это поле будет содержать результат
#
# Наша задача - написать скрипт, который делал бы следующее:
#
# 1) создавал задачу
# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

