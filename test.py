# a = [(2,4),(2,3),(4,8),(5,5),(5,7),(6,7)]

# a = sorted(a, key = lambda x: x[0])
# a = sorted(a, key = lambda x: x[1])

# print(a)
import sys

n = input().split()
a = list(map(int,input().split()))
cnt = 0

for k in range(n):
    if a[k] = a[k-1]+1:
        cnt += 1

