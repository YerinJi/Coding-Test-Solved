n = int(input())
result = 0
arr =list(map(int, input().split()))
for i in range(n):
  cnt = 0
  for j in range(1,arr[i]+1):
    if(arr[i] % j == 0):
      cnt += 1
  if( cnt == 2):
    result += 1
  
print(result)