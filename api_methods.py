import requests


class HttpMethods:
    def __init__(self, method):
        self.method = method
        self.link = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

    def without_method(self):
        response = requests.get(self.link).text
        return print(f'Without parameter: \n{response}')

    def another_method(self):
        payload = {'method': self.method}
        response = requests.head(self.link, data=payload)
        return print(f'Method not in the list: \n{response}')

    def correct_method(self):
        print('Correct methods: ')
        payload = {'method': self.method}
        if self.method == 'GET':
            print(f'Method: {self.method}')
            response = requests.get(self.link, params=payload).text
            return print(f'Response: {response}')
        elif self.method == 'POST':
            response = requests.post(self.link, data=payload).text
            return print(response)
        elif self.method == 'PUT':
            response = requests.put(self.link, data=payload).text
            return print(response)
        elif self.method == 'DELETE':
            response = requests.delete(self.link, data=payload).text
            return print(response)
        else:
            print('Error')

    def all_methods(self):
        print('All methods: ')
        payload = {'method': ['GET', 'POST', 'PUT', 'DELETE']}
        new_dict = {}

        if self.method == 'GET':
            for value in payload:
                for key in payload[value]:
                    print(f'Parameter = {key}')
                    new_dict[value] = key
                    response_get = requests.get(self.link, params=new_dict).text
                    print(f'Response: {response_get}')

        elif self.method == 'POST':
            for value in payload:
                for key in payload[value]:
                    print(f'Parameter = {key}')
                    new_dict[value] = key
                    response_post = requests.post(self.link, data=new_dict).text
                    print(f'Response: {response_post}')

        elif self.method == 'PUT':
            for value in payload:
                for key in payload[value]:
                    print(f'Parameter = {key}')
                    new_dict[value] = key
                    response_post = requests.put(self.link, data=new_dict).text
                    print(f'Response: {response_post}')

        elif self.method == 'DELETE':
            for value in payload:
                for key in payload[value]:
                    print(f'Parameter = {key}')
                    new_dict[value] = key
                    response_post = requests.delete(self.link, data=new_dict).text
                    print(f'Response: {response_post}')
        else:
            print('Error')


get = HttpMethods('GET')
get.without_method()
print()
get.another_method()
print()
get.correct_method()
print()
get.all_methods()


# У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type Запрашивать его можно четырьмя
# разными HTTP-методами: POST, GET, PUT, DELETE при этом в запросе должен быть параметр method. Он должен содержать
# указание метода, с помощью которого вы делаете запрос. Например, если вы делаете GET-запрос, параметр method должен
# равняться строке ‘GET’. Если POST-запросом - то параметр method должен равняться ‘POST’. надо написать скрипт,
# который делает следующее: 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в
# этом случае.#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае. 3.
# Делает запрос с правильным значением method. Описать что будет выводиться в этом случае. 4. С помощью цикла
# проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом
# передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов
# запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает
# так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так. Не забывайте,
# что для GET-запроса данные надо передавать через params= А для всех остальных через data=
