import itertools

def solution(numbers):
    answer = 0
    number_list = list(numbers)
    number_list.sort(reverse=True)
    max_num = int("".join(number_list))
    sieve = [False, False] + [True] * (max_num - 1)
    m = int(max_num ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:         # i가 소수인 경우
            for j in range(i+i, max_num+1, i): # i이후 i의 배수들을 False
                sieve[j] = False
        
    for i in range(1,len(number_list)+1):
        result = list(itertools.permutations(number_list, i))
        for r in result:
            index = int("".join(r))
            if sieve[index]:
                sieve[index] = False
                answer += 1
    return answer