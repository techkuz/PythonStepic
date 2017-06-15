import requests

r = requests.get('http://vgik.info')
print(r.text)

url = 'http://vgik.info'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params = par) # передача параметров в запрос
print(r.url) # Сформированный url-адрес с учетом параметров GET запроса


url = 'http://vgik.info'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies = cookies) # отправка сформированных cookies на сервер
print(r.text) # Сформированный url-адрес с учетом параметров GET запроса


'''
print(r.cookies['example_cookie_name']) # использование cookies, полученных от сервера
'''