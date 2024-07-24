while 1:
  num= list(map(int, input().split()))
  long = max(num)
  if(sum(num) == 0):
    break
  if (0 < sum(num)-long <= long):
    print("Invalid")
  else:
    if num[0] == num[1] == num[2]:
      print("Equilateral")
    elif num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
      print("Isosceles")
    else:
      print("Scalene")

  
  