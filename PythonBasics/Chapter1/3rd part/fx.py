def f(x):
    # put your python code here
    if(x <= -2):
        return 1 - (x + 2) * (x + 2)
    elif(x <= 2):
        return -(x/2)
    else:
        return (x-2) * (x-2) + 1

print(f(1))