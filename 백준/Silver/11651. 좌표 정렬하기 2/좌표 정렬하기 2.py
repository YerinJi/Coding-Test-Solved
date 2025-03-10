num = int(input())
int_arr = []

for _ in range(num):
  a,b = map(int, input().split(' '))
  int_arr.append([b,a])

sor_arr = sorted(int_arr)

for i in range(num):
  print(sor_arr[i][1],sor_arr[i][0])
  
