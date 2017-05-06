'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:
'''
fh = open('dataset.txt', "r")

data_to_write = []
s1_grades = 0
s2_grades = 0
s3_grades = 0
count = 0

for line in fh:
    s1 = [int(i) for i in line.strip().split(";")[1:]]
    data_to_write.append((s1[0] + s1[1] + s1[2]) / 3)
    s1_grades += s1[0]
    s2_grades += s1[1]
    s3_grades += s1[2]
    count += 1
    
fh.close()

fh = open("solution.txt", "w")

for element in data_to_write:
    fh.write(str(element))
    fh.write("\n")
fh.write( str((s1_grades / count)) + " " + str((s2_grades / count)) + " " + str((s3_grades / count)))

fh.close()