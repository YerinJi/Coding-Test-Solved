import sys

input = sys.stdin.readline

n,m = map(int, input().split())
poke = {}

for i in range(1,n+1):
  name = input().strip()
  poke[str(i)] = name
  poke[name] = str(i)

for _ in range(m):
  que = input().strip()
  print(poke[que])
      
    