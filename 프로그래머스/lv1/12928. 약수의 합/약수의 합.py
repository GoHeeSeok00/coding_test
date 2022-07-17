def solution(n): 
    # 방법 1
    # 시간복잡도 4n + 3 = O(n)
    # answer = 0                # 대입연산 1
    # for i in range(1, n+1):   # 반복문 n + 2
        # if n % i == 0:        # 조건문 2n
            # answer += i       # 덧셈 연산 n
            
    # 방법 2
    # 시간복잡도 10√n + 5 = O(√n)
    answer = 0                              # 대입연산 1
    for i in range(1, int(n**(0.5)+1)):     # 반복문 √n +3
        quotient, remainder = divmod(n, i)  # 대입연산 3√n
        if remainder == 0:                  # 조건문 √n
            if quotient == i:               # 조건문 √n 
                answer += i                 # 덧셈 연산 √n
            else:                           # 조건문 √n
                answer += i + quotient      # 덧셈 연산 2√n
    return answer                           # 리턴 1