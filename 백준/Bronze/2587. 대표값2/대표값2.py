sum = 0
avg = 0
list = []
for i in range(5):
  list.append(int(input()))
  sum += list[i]

avg = sum // 5
list.sort()
print(avg)
print(list[2])