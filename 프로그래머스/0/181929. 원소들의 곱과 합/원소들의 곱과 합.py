def solution(num_list):
    s_number = 0
    a_number = 1
    for i in range(len(num_list)):
        s_number += num_list[i]
        a_number *= num_list[i]
    if a_number < s_number**2:
        return 1
    else:
        return 0