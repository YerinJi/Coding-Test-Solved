import sys

n = int(input())
arr = 10001 * [0]

for _ in range(n):
  r = int(sys.stdin.readline())
  arr[r] += 1

for i in range(10001):
  if arr[i] != 0:
    for _ in range(arr[i]):
      print(i)