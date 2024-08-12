def solution(my_string, is_suffix):
    answer = 0
    check = ''
    for i in range(1,len(my_string)+1):
        check = my_string[i-1::]
        if check == is_suffix:
            answer = 1
            break
    return answer