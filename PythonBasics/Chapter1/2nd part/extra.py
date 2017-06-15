'''Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5)'''

n = int(input())

#n = 3

number = 0
resulting_matrix = [[0] * n for i in range(n)] # initialize empty list

values = n

x, y, c = 0, 0, 0
check_value1, check_value2 = n - 1, n - 2

for iteration in range(0, (((n - 1) * 2) + 1)):
    
    if(n % 2 == 1): # if input is even not even
        
        if (values % 2 == 1): #if values is not even
            
            if (iteration % 2 == 1): #if number of iteration is not even
                for i in range(check_value2, check_value2 - values, -1):
                    
                    number = number + 1
                    resulting_matrix[i][c] = number
                check_value2 = check_value2 - 1
                c = c + 1
                   
                
            else: #if number of iteration is even
                if (iteration == 0): #if first iteration
                    for i in range(0, values):
                        number = number + 1
                        resulting_matrix[y][i] = number
                    y = y + 1
                
                else: #if not first iteration
              
                    for i in range(y, y + values):
                        number = number + 1
                        resulting_matrix[y][i] = number
                        
                    y = y + 1
                
            
        else: #if values is even
            
            if (iteration % 2 == 1):  # if number of iteration is not even
               
                for i in range(y, check_value1 + 1):
                    
                    number = number + 1
                    resulting_matrix[i][check_value1] = number
            
            else: # if number of iteration is even
           
                for i in range(check_value1 - 1, check_value1 - values - 1, -1):
                    
                    number = number + 1
                    resulting_matrix[check_value1][i] = number
                check_value1 = check_value1 - 1
            
        if(iteration == 0):
             values = values - 1
        else:
            if(iteration % 2 == 0):
                values = values - 1
        
        
    else: # if input number is even
    
        if (values % 2 == 1): #if values is not even
            
            if (iteration % 2 == 1): # if number of iteration is not even
                
                for i in range(y, check_value1 + 1):
                    
                    number = number + 1
                    resulting_matrix[i][check_value1] = number
                
            else: #if number of iteration is even
                
                for i in range(check_value1 - 1, check_value1 - values - 1, -1):
                    
                    number = number + 1
                    resulting_matrix[check_value1][i] = number
                check_value1 = check_value1 - 1
                
            
        else: #if values is even
            
            if (iteration % 2 == 1): #if number of iteration is not even
                
                for i in range(check_value2, check_value2 - values, -1):
                    number = number + 1
                    resulting_matrix[i][c] = number
                check_value2 = check_value2 - 1
                c = c + 1
                
            
            else: # if number of iteration is even
                
                if (iteration == 0):
                    for i in range(0, values):
                        number = number + 1
                        resulting_matrix[y][i] = number
                    y = y + 1
                
                else:
               
                    for i in range(y, y + values):
                        number = number + 1
                        resulting_matrix[y][i] = number
                        
                    y = y + 1
                 
            
        if(iteration == 0):
             values = values - 1
        else:
            if(iteration % 2 == 0):
                values = values - 1

for lists in resulting_matrix:
    for i in lists:
        print (i, end = ' ')
    print()