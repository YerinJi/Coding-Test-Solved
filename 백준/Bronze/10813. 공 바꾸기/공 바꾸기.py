n,m = map(int, input().split())
arr = []
for i in range(1,n+1):
  arr.append(i)

for i in range(1,m+1):
  a,b = map(int,input().split())
  tmp = arr[a-1]
  arr[a-1] = arr[b-1]
  arr[b-1] = tmp

answer_arr = " ".join([str(_) for _ in arr])
print(answer_arr)