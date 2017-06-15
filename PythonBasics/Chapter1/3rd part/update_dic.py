'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

Если ключ key есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу. 
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key. Если и ключа 2⋅key нет, то нужно добавить  ключ2 key   в словарь и сопоставить ему список из переданного элемента [value]

Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.
'''

def update_dictionary(d, key, value):
    if(key in d):
        d[key].append(value)
    elif(2*key in d):
        d[2*key].append(value)
    else:
        d[2*key] = [value]

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d) 