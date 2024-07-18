n = int(input())
cent = [25,10,5,1]
for _ in range(n):
  input_num = int(input())
  result = []
  for i,value in enumerate(cent):
    if(input_num < value):
        result.append(0)
    else:
      result.append(input_num//value)
      input_num -= input_num//value * value

  answer = " ".join([str(_) for _ in list(map(int, result))])
  print(answer)
    