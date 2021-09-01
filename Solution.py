# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

a = OrderedDict()
n = int(input())
for i in range(n):
    s = input()
    if s in a.keys():
        a[s] += 1
    else:
        a[s] = 1
print(len(a.keys()))
print(' '.join([str(a[j]) for j in a.keys()]))
