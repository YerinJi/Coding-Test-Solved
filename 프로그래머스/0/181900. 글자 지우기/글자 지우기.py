def solution(my_string, indices):
    answer = ''
    string_list = list(my_string)
    indices.sort()
    indices.reverse()
    for i in indices:
        del string_list[i]
    
    for str in string_list:
        answer += str
    return answer
