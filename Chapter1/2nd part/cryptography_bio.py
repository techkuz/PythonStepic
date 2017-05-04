'''Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.'''
#aaaabbcaa
word = input()
index = 0
end_string = ''
count = 0

for i,c in enumerate(word):
    if i == 0:
        end_string = end_string + c
        count = count + 1
        continue
    
    if c == word[i - 1]:
        count = count + 1
        
    else:
        if count != 0:
            end_string = end_string + str(count) 
            count = 0
            end_string = end_string + c
            count = count + 1
        else:
            end_string = end_string + c
            count = count + 1
        
if count != 0:
    end_string = end_string + str(count) 
print (end_string)    