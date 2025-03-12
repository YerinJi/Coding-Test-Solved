inp = list(map(int, input().split()))
first = [1,2,3,4,5,6,7,8]
second = [8,7,6,5,4,3,2,1]

if inp == first :
  print('ascending')
elif inp == second:
  print('descending')
else:
  print('mixed')