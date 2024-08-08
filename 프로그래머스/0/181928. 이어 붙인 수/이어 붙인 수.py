def solution(num_list):
    first_result = ''
    second_result = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            first_result += str(num_list[i])
        else:
            second_result += str(num_list[i])
    answer = int(first_result) + int(second_result)
    return answer
        