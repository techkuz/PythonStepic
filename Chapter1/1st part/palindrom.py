s = input()

i = 0

j = len(s) - 1

is_palindrome = True

while i < j:
    if(s[i] != s[j]):
        is_palindrome= False
    i += 1
    j -= 1

if(is_palindrome):
    print('YES')
else:
    print('NO')
    