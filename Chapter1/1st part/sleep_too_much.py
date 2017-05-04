to_sleep = int(input())
max_sleep = int(input())
now_sleep = int(input())

if now_sleep < to_sleep:
    print("Недосып")

elif now_sleep > max_sleep:
    print ("Пересып")
    
elif max_sleep >= now_sleep >= to_sleep:
    print("Это нормально")
    
