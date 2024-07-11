n = []
for _ in range(26):
  n.append(-1)

stre = input()

for i in range(len(stre)):
  first = ord(stre[i])-97
  if(n[first] != -1):
    continue
  else:
    n[first] = i

answer = " ".join([str(_) for _ in n])
print(answer)