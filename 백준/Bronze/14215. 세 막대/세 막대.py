num_list = sorted(list(map(int, input().split())))
while 1:
  if num_list[0] + num_list[1] <= num_list[2]:
    num_list[2] -= 1
  else:
    print(sum(num_list))
    break