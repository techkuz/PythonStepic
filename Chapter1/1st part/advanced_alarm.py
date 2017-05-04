def calculate_time():
    minutes = int(input())
    now_hours = int(input())
    now_minutes = int(input())
    hours = 0
    final_minutes = 0
    final_hours = 0
    while minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1
        
    final_minutes = minutes + now_minutes
    final_hours = hours + now_hours
    
    while final_minutes >= 60:
        final_hours = final_hours + 1
        final_minutes = final_minutes- 60
    
    while final_hours > 24:
        final_hours = final_hours + hours - 24
    
    
    print (final_hours)
    print (final_minutes)
    
calculate_time()
        