def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def solution(w,h):
    result = gcd(w, h)
    return (w * h) - (w + h - result)