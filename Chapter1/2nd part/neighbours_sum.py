''' Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.'''

numbers = input().split()
resulting_list = []

for i, c in enumerate(numbers):
    if len(numbers) == 1:
        print (numbers[0])
    else:
        if i == 0:
            resulting_list.append(int(numbers[-1]) + int(numbers[1]))
        
        elif i == len(numbers) - 1:
            resulting_list.append(int(numbers[-2]) + int(numbers[0]))
            
        else:
            resulting_list.append(int(numbers[i - 1]) + int(numbers[i + 1]))
        
for i in resulting_list:
    print (i, end = ' ')