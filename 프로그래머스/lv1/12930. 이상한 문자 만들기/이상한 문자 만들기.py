def solution(s):
    answer = '' # 대입연산 1
    words = s.split(" ") # split 연산 n
    for word in words: # 반복문 n (4n + 4n^2)
        status = 0 # 대입연산 1
        for phoneme in word: # 반복문 n (4n)
            if status == 0: # 조건 연산 1
                answer += phoneme.upper() # 덧셈 대입 연산 1
                status = 1 # 대입연산 1
            else:
                answer += phoneme.lower() # 덧셈 대입 연산 1
                status = 0 # 대입연산 1
        else:
            answer += " " # 대입연산 1
    return answer[:-1] # 리턴 연산 1 (5n + (4n)^2 + 2) -> 시간 복잡도 : n^2