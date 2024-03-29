def solution(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n      
    sieve[0] = False               
    # n의 최대 약수가 sprt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)             
    for i in range(2, m+1):        
        if sieve[i-1] == True:   
            for j in range(i+i, n+1, i): 
                sieve[j-1] = False
    return sieve.count(True)       