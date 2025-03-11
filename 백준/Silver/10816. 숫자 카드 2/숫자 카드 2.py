import sys
from typing import Counter

input = sys.stdin.readline

n = int(input())
n_list = input().split()
m = int(input())
m_list = input().split()

n_counter = Counter(n_list)

answer = [n_counter[number] for number in m_list]

for i in range(m):
  print(answer[i])