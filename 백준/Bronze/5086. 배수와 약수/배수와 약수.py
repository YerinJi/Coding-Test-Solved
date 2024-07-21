while 1:
  a,b = input().split()
  if(a =='0' or b =='0'):
    break
  a = int(a)
  b = int(b)
  if (a < b) & (b % a == 0):
    print("factor")
  elif (a > b) & (a % b == 0):
    print("multiple")
  else:
    print("neither")
  

  