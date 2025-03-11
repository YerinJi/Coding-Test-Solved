import sys

input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
  name, state = input().strip().split()
  dic[name] = state

for name in sorted(dic.keys(), reverse=True):
  if dic[name] == 'enter':
    print(name)
