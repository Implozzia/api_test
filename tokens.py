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
