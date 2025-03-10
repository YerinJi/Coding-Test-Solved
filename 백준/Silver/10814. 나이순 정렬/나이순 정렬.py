import sys

input = sys.stdin.readline
n = int(input())

li = [list(map(str,input().split())) for _ in range(n)]

li.sort(key=lambda x: int(x[0]))

for lis in li:
  print(* lis)