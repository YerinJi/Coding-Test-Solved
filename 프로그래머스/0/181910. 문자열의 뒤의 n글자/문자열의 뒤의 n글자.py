def solution(my_string, n):
    answer = ''
    my_string = my_string[::-1]
    for i in range(0,n):
        answer += my_string[i]
    answer = answer[::-1]
    return answer