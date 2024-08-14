def solution(my_string, is_prefix):
    answer = 0
    
    for i in range(len(my_string)):
        check = ''
        for j in range(i):
            check += my_string[j]
            if check == is_prefix:
                answer = 1
    return answer