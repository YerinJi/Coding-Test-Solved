num,m = map(int,input().split())
arr = list(map(int, input().split()))
answer_list = []
for i in range(len(arr)):
  if arr[i] < m:
    answer_list.append(arr[i])

answer = " ".join([str(_) for _ in answer_list])
print(answer)