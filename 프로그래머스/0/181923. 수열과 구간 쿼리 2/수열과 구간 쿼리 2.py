def solution(arr, queries):
    result = []
    for i in range(len(queries)):
        tmp = []
        for j in range(queries[i][0],queries[i][1]+1):
            if arr[j] > queries[i][2]:
                tmp.append(arr[j])
        if len(tmp) > 0:
            tmp.sort()
            result.append(tmp[0])
        else:
            result.append(-1)
            
    return result