def solution(n):            # 시간복잡도 n + 6 = O(n)
    answer = 0              # 대입연산 1
    for i in str(n):        # 반복문, str 변환 n + 1 
        answer += int(i)    # 대입연산, 덧셈연산, int 변환 3
    return answer           # 리턴 1