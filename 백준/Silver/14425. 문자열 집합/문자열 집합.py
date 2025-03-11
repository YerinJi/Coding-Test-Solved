import sys

input = sys.stdin.readline

n,m =  map(int, input().strip().split())

n_li = [input().strip() for _ in range(n)]
m_li = [input().strip() for _ in range(m)]


cnt = 0 
for item in m_li:
  if item in n_li:
    cnt += 1

print(cnt)