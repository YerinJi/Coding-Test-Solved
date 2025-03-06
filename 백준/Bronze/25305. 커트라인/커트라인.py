number, reword =  map(int, input().split())
list = list(map(int, input().split()))
list.sort(reverse=True)
print(list[reword-1])
