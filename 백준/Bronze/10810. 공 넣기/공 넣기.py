n,m = map(int, input().split())
arr = []
for _ in range(1,n+1):
  arr.append(0)

for i in range(1,m+1):
  a,b,c = map(int,input().split())
  for j in range(a-1,b):
    arr[j] =  c

answer_arr = " ".join([str(_) for _ in arr])
print(answer_arr)