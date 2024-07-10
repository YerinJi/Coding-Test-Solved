n = int(input())
arr = list(map(int, input().split()))
max = max(arr)
answer_list = []
for i in range(0,n):
  tmp = arr[i]/max*100
  answer_list.append(tmp)

sum = sum(answer_list)
avg = sum/n
print(avg)
  
  