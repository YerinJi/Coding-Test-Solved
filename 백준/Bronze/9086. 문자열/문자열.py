n = int(input())

for _ in range(n):
  answer = []
  str = input()
  answer.append(str[0])
  answer.append(str[-1])
  answer_list = "".join(answer)
  print(answer_list)
