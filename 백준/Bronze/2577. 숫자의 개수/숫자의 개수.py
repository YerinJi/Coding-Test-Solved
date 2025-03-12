from typing import Counter

a = int(input())
b = int(input())
c = int(input())

result = a*b*c

result = str(result)

c = Counter(result)
for i in range(10):
  print(f"{c.get(str(i),0)}")