import sys

input = sys.stdin.readline

n = int(input())
card_li = list(map(int, input().strip().split()))
find = int(input())
find_li = list(map(int, input().strip().split()))

card_set = set(card_li)

result = [1 if num in card_set else 0 for num in find_li]

print(*result)
