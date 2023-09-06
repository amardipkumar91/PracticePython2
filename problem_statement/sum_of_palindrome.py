def get_palindrome(number):
    tmp = number
    rev = 0
    while (number > 0):
        dig = number % 10
        rev = rev * 10 + dig
        number = number //10
    if tmp == rev:
        return True

def get_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True

sum =0 
for i in range(15):
    if get_palindrome(i):
        print i
        sum = sum + i

print (sum)