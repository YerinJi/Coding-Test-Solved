c = [1,1,2,2,2,8]
input_c = list(map(int, input().split()))
answer_l = [(c[i] - input_c[i]) for i in range(6)]
answer = " ".join([str(_) for _ in answer_l])
print(answer)
