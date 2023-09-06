#Number of ways to go from one point to another in a grid
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n -1)

# def count_of_ways(n):
#     total = fact(n + n)
#     total1 = fact(n)
#     ways = total // (total1 * total1)
#     return ways

# if __name__ == "__main__":
#     print ("Enter the no if grid : ")
#     n = input()
#     noOfWays = count_of_ways(n)
#     print ("no of ways", noOfWays)
#-------------------------other solution -------------------------------
#grid question solution
# def count_of_ways(m , n):
#     if m == 0 and n == 0:
#         return 0
#     elif m == 0 or n == 0:
#         return 1
#     else:
#         return count_of_ways(m -1, n) + count_of_ways(m , n- 1)

# if __name__ == "__main__":
#     print ("Enter the no if grid : ")
#     n = int(input())
#     noOfWays = count_of_ways(n, n)
#     print ("no of ways", noOfWays)


import bs4
import requests
url="http://www.mycellarhk.com/wine-list.php"
data=requests.get(url)
soup=bs4.BeautifulSoup(data.text,'html.parser')
import pdb;pdb.set_trace()
# soup.prettify()
for para in soup.find('p'):
    print(para.text)

