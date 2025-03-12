li = map(int,input().split())
sum =0
for i in li:
  sum += i*i

result = sum%10
print(result)