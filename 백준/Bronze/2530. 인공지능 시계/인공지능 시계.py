h,m,s = map(int,input().split())
time = int(input())

s += time%60
time = time//60

if s >= 60:
  s = s - 60
  m += 1

m += time % 60
time = time // 60
if(m >= 60):
  m = m-60
  h += 1

h += time % 24
if h >= 24:
  h -= 24

print(h,m,s)