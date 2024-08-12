def solution(intStrs, k, s, l):
    answer = []
    for j in range(len(intStrs)):
        tmp = ''
        for i in range(0,l):
            tmp += ''.join(intStrs[j][s+i])

        if(int(tmp)>k):
            answer.append(int(tmp))
    return answer