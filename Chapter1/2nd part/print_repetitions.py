'''Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.'''

x = input().split()
resulting_list = []

if len(x) != 1:
    for i in x:
        if x.count(i) > 1 and i not in resulting_list:
            resulting_list.append(i)
    
    resulting_list.sort()
    for i in resulting_list:
        print (i, end = ' ')