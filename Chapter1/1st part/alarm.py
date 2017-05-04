
def calculate_time():
    minutes = int(input("Type in the number of minutes "))
    hours = 0
    while minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
    
    
    print (hours)
    print (minutes)
    
calculate_time()
        