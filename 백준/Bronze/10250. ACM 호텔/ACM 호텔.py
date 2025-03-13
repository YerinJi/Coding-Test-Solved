n = int(input())

for _ in range(n):
  h,w,m = map(int, input().split())
  li = []
  for i in range(1,w+1):
      for j in range(1,h+1):
        li.append(f"{j}{i:02}")
        
  print(li[m-1])
  
    