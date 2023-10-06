def solution(s):
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