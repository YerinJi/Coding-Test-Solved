from itertools import combinations
n,m = map(int,input().split())
arr = list(map(int,input().split()))
com = list(combinations(arr,3))
total = 0
for i in com:
  if sum(i)<=m:
    total = max(total, sum(i))

print(total)