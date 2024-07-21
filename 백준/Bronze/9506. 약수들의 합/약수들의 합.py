while 1:
  n = int(input())
  if n == -1:
    break
  result = []
  for i in range(1,n):
    if(n % i == 0):
      result.append(i)

  if sum(result) == n:
    print(f"{n} = ",end='')
    print(" + ".join(map(str,result)))
  else:
    print(f"{n} ",end='')
    print("is NOT perfect.")

    
      