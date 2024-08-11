def solution(a, b, c, d):
    arr = [a,b,c,d]
    abcd = dict() # 주사위 숫자 개수 입력

    for elm in arr:
        if elm not in abcd: # abcd에 해당 숫자가 없다면 추가
            abcd[elm] = 1
        else: # abcd에 해당 숫자가 존재하면 개수 1 증가
            abcd[elm] += 1

    abcd = sorted(abcd, key=lambda x:abcd[x]) #오름차순 정렬 , key= 정렬기준 -> abcd의 각 요소 x에대해 abcd[x] 값을 반환
    if len(abcd) == 1: # 네 주사위 숫자가 모두 같을때
        return 1111 * a
    elif len(abcd) == 2: # 네 주사위 숫자가 중복 제외 2개일때
        if arr.count(abcd[0]) in [1,3]: # abcd[0]과 abcd[1] 이 존재 -> 하나라도 3또는 1인 경우
            return (10 * abcd[1] + abcd[0]) ** 2
        else: # 두 개씩 같은 값이 나온 경우
            return (abcd[0] + abcd[1]) * abs(abcd[0] - abcd[1])
    elif len(abcd) == 3: # 중복제외 3
        return abcd[0] * abcd[1]

    return min(arr) # 네 주사위에 적힌 숫자가 모두 다른 경우