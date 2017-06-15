a = int(input()) 
b = int(input()) 
c = int(input()) 

check_bit = 0
smaller, bigger, biggest = 0, 0, 0
if a > b:
    bigger = a 
    smaller = b 
    
elif a == b:
    if a > c:
        print (a)
        print (c)
        print (b)
        check_bit = 1
    
    else:
        print (c)
        print (a)
        print (b)
        check_bit = 1
else:
    bigger = b # bigger = 25 
    
    smaller = a #smaller = 23
    
if check_bit != 1:
    if c > bigger:
        biggest = c
        
    elif c < smaller:
        biggest = bigger 
        bigger = smaller
        smaller = c
    else:
        biggest = bigger 
        
        bigger = c 

    print (biggest)
    print (smaller)
    print (bigger)