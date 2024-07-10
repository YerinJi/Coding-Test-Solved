n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  arr[a-1:b] = arr[a-1:b][::-1]

answer_list = " ".join(str(_) for _ in arr)
print(answer_list)