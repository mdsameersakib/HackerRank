"""
Example:
>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
"""

if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    string = input().strip()
    
    if eval(string) == k:
        print(True)
    else:
        print(False)

# OR something like this"

s = list(map(int,"1 4".split(" ")))
x = s[0]
s2 = "x**3 + x**2 + x + 1"
if eval(s2)==s[1]:
    print(1>0)
