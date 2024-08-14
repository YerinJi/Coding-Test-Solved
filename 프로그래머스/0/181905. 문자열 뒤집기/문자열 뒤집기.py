def solution(my_string, s, e):
    answer = ''
    tmp = ''
    for i in range(s):
        answer += my_string[i]
    for j in range(s,e+1):
        tmp += my_string[j]
    tmp = tmp[::-1]
    answer += tmp
    for k in range(e+1,len(my_string)):
        answer += my_string[k]
    return answer