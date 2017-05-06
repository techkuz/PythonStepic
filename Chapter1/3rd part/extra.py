'''
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков. 

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: 

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac
Sample Input 2:
dcba
badc
dcba
badc
Sample Output 2:
badc
dcba
'''

alphabet = input()
#alphabet = "abcd"
encoding_alphabet = input()
#encoding_alphabet = "*d%#"
data = {}

for count, element in enumerate(alphabet):
    data[element] = encoding_alphabet[count]

word_to_encode = input()
#word_to_encode = "abacabadaba"
encoded_word = ""

for letter in word_to_encode:
    encoded_word += data[letter]

word_to_decode = input()
#word_to_decode = "#*%*d*%"
decoded_word = ""

for letter in word_to_decode:
    for orig_letter, encode_letter in data.items():
        
        if(letter == encode_letter):
            decoded_word += orig_letter
            break
    
print(encoded_word)
print(decoded_word)