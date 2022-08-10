def trinary_digit(a):
    rev_base = ""
    base = ["4", "1", "2"]
    while a > 0:
        a, remainder = divmod(a, 3)
        if remainder == 0:
            a = a - 1
        rev_base += base[remainder]
    return rev_base[::-1]

def solution(n):
    return trinary_digit(n)