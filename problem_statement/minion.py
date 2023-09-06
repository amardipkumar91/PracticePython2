vowels = 'AIOUE'
data = "BANANA"
x = y = 0
for i in range(len(data)):
    if data[i] in vowels:
        x += len(data) - i
    else:
        y += len(data) - i

if x > y:
    print ("winner is x", x)
elif x == y:
    print ("draw")
else:
    print ("winner is y", y)