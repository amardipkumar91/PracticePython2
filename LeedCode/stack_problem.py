#Asteroid Collision
'''We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.Find out the state of the asteroids after all collisions.
 If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
 Two asteroids moving in the same direction will never meet.

'''
def astriod_collision(asteroids):
    stack = []
    for asteroid in asteroids:
        while stack and asteroid <0 and stack[-1] >0:
            if abs(asteroid) > stack[-1]:
                stack.pop()
            elif abs(asteroid) == stack[-1]:
                stack.pop()
                asteroid = 0
                break
            else:
                asteroid = 0 
                break
        if asteroid !=0:
            stack.append(asteroid)
    return stack

asteroids = [10,2,-5]
print (astriod_collision(asteroids))

#Removing Stars From a String
'''You are given a string s, which contains stars *.
In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.
'''

def remove_star(strn):
    stack = []
    for i in strn:
        if i == '*':
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return "".join(stack)
strn = "leet**cod*e"
print (remove_star(strn))


#Decode String
'''Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers,
 k. For example, there will not be input like 3a or 2[4].
'''

def decodeString(strn):
    stack = []
    cur_str = ""
    cur_num = 0
    for i in strn:
        if i.isdigit():
            cur_num = cur_num * 10 + int(i)
        elif i == '[':
            stack.append((cur_str, cur_num))
            cur_str = ""
            cur_num = 0
        elif i == ']':
            prev_str, r_count = stack.pop()
            cur_str = prev_str + cur_str * r_count
        else:
            cur_str = cur_str + i
    return cur_str
strn = "3[a]2[bc]"
print (decodeString(strn))

