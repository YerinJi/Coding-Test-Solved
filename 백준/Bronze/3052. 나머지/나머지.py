arr = []
for _ in range(10):
  n = int(input())
  k = n % 42
  if k not in arr:
    arr.append(k)

print(len(arr))