def solution(n): 
    # 방법 1
    # 시간복잡도 4n + 3 = O(n)
    answer = 0                # 대입연산 1
    for i in range(1, n+1):   # 반복문 n + 2
        if n % i == 0:        # 조건문 2n
            answer += i       # 덧셈 연산 n

    return answer                           # 리턴 1