def isAlphaToUpperStr(word):
    if word.isalpha():
        return word.upper()
    return word

def solution(s):
    # 방법 1. 문자열을 공백 기준으로 나누고(배열에 단어별로) 각 단어의 첫 문자열이 숫자가 아닌경우 JadenCase, 숫자인 경우는 LowerCase수정
    answer = []
    words = s.split(' ')
    print(words)
    for word in words:
        if word == '':
            answer.append(word)
        elif not word[0].isdigit():
            answer.append(word.capitalize())
        else:
            answer.append(word.lower())
    return " ".join(answer)
    # 방법 2. 모든 문자열을 소문자로 변경, 문자열 반복 시 첫 문자와 공백 이후에 오는 문자 숫자여부에 따른 대문자 변경
    # answer = ''
    # for i, j in  enumerate(s.lower()):
    #     if i == 0:
    #         answer += isAlphaToUpperStr(j)
    #     elif j.isalpha() and s[i-1] == ' ':
    #         answer += isAlphaToUpperStr(j)
    #     else:
    #         answer += j
    # return answer