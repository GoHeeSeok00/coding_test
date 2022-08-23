def solution(s):
    if s == "":
        return 1
    stack = []
    for v in s:
        if stack:
            if v == stack[-1]:
                stack.pop()
                continue
        stack.append(v)

    if stack:
        return 0
    return 1