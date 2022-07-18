def solution(n):                # 시간복잡도 : 3n + 5 = O(n)
    answer = []                 # 대입연산 : 1
    for i in str(n)[::-1]:      # 반복문, str변환, reverse : n + 3
        answer.append(int(i))   # append, int : 2n
    return answer               # 리턴 :1