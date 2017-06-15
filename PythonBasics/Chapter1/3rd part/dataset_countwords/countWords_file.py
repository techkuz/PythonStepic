'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
'''

fh = open('dataset.txt', "r")

s1 = fh.read().lower().split()

fh.close()

count_words = dict()

for element in s1:
    if(element in count_words):
        count_words[element] = count_words[element] + 1
    else:
        count_words[element] = 1
    
maximum = max(count_words.values())

maximum_list = []
for k, v in count_words.items():
    if(v == maximum):
        maximum_list.append(k)

fh = open("solution.txt", "w")
print(maximum, maximum_list)

fh.write(str(min(maximum_list)) + " " + str(maximum))

fh.close()