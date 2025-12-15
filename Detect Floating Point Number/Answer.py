import re
t = int(input())
for _ in range(t):
    s = input()
    obj = r'[+-]?([0-9]+\.[0-9]+|\.[0-9]+)'
    print(bool(re.fullmatch(obj, s)))
