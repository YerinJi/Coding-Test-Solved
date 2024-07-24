n = int(input())
x = []
y = []
for _ in range(n):
  a,b = map(int, input().split())
  if len(x)==0:
    x.append(a)
    x.append(a)
    y.append(b)
    y.append(b)
  else:
    if(x[0]> a):
      x[0] = a
    elif(x[1]<a):
      x[1]=a
    if(y[0]>b):
      y[0] = b
    elif(y[1]<b):
      y[1] = b
  

line1 = x[1] - x[0]
line2 = y[1] - y[0]
print(line1*line2)