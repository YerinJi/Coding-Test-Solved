def solution(my_string):
    answer = [0] * 52
    for str in my_string:
        if str.isupper():
            answer[ord(str) - 65] += 1
        else:
            answer[ord(str) - 71] += 1
    
    return answer