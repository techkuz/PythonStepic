'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. 

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''
import requests

url = "https://stepic.org/media/attachments/course67/3.6.3/"

url_end = "699991.txt"

while (True):
    r = requests.get(url + url_end)
    if(r.text.startswith("We")):
        
        print(r.text)
        break
    else:
        print(r.text)
        url_end = r.text
        