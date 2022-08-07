def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(n, m):
    gcd_n = gcd(n, m)
    return [gcd_n, int(n * m / gcd_n)]