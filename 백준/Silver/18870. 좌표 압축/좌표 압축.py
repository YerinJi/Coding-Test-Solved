import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
set_li = sorted(set(li))
dic = {set_li[i] : i for i in range(len(set_li))}

for i in li:
  print(dic[i], end=' ')