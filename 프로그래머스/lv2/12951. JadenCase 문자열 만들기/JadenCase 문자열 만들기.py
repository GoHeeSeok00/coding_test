def solution(s):
    answer = []
    
#     방법 1. 문자열을 반복문으로 돌면서 맨 처음과 공백 이후 처음 문자열이 숫자로 바꿀 수 없으면 대문자로 바꿔주기 -> case 필요
#     방법 2. 문자열을 공백 기준으로 나누고(배열에 단어별로) 각 단어의 첫 문자열을 숫자로 바꿀 수 없으면 대문자로 바꿔주기
    words = s.split(' ')

    for word in words:
        if word == '':
            answer.append(word)
        elif word == ' ':
            answer.append(word)
        elif not word[0].isdigit():
            answer.append(word.capitalize())
        else:
            answer.append(word.lower())
            
    return " ".join(answer)