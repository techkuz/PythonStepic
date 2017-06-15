''' Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению. '''

# put your python code here

incoming_line = input()

twoD_array = []

while(incoming_line != "end"):
    twoD_array.append(incoming_line.split())
    incoming_line = input()
    
count_lists = 0

resulting_matrix = [[0] * n for i in range(n)]

for lists in twoD_array:
    #print(lists)
    count_elements = 0        
    for element in lists:
        #print(element)
        if(count_lists == len(twoD_array) - 1):
            if(count_elements == len(twoD_array[count_lists]) - 1):
               resulting_list[count_lists].append(int(twoD_array[count_lists - 1][count_elements]) +
                   int(twoD_array[0][count_elements]) +
                   int(twoD_array[count_lists][count_elements - 1]) +
                   int(twoD_array[count_lists][0]))
            else:
                resulting_list[count_lists].append(int(twoD_array[count_lists - 1][count_elements]) +
                   int(twoD_array[0][count_elements]) +
                   int(twoD_array[count_lists][count_elements - 1]) +
                   int(twoD_array[count_lists][count_elements + 1]))    
            
        else: 
            if(count_elements == len(twoD_array[count_lists]) - 1):
               resulting_list[count_lists].append(int(twoD_array[count_lists - 1][count_elements]) +
                   int(twoD_array[count_lists + 1][count_elements]) +
                   int(twoD_array[count_lists][count_elements - 1]) +
                   int(twoD_array[count_lists][0]))   
            else:
                resulting_list[count_lists].append(int(twoD_array[count_lists - 1][count_elements]) +
                   int(twoD_array[count_lists + 1][count_elements]) +
                   int(twoD_array[count_lists][count_elements - 1]) +
                   int(twoD_array[count_lists][count_elements + 1]))                 
                
        count_elements += 1    
    
    count_lists += 1
    
for lists in resulting_list:
    for i in lists:
        print (i, end = ' ')
    print()