n = int(input())

for _  in range(n):
  a,b = map(str,input().split())
  a = int(a)
  answer = []
  answer_p = ""
  for i in range(len(b)):
    for _ in range(a):
      answer.append(b[i])
  answer_p = "".join([str(_) for _ in answer])
  print(answer_p)
