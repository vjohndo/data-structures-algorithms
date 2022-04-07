from math import gcd

def nth_ugly_number(n: int, a: int, b: int, c: int) -> int:
    ab = a * b // gcd(a, b)
    bc = b * c // gcd(b, c)
    ac = a * c // gcd(a, c)
    abc = ab * c // gcd(ab, c)
    def ugly_number_count(k: int) -> int:
        return (k // a + k // b + k // c) - (k // ab + k // bc + k // ac) + k // abc
    min_ptr = n
    max_ptr = n * min(a, b, c)
    boundaryIndex = max_ptr
    while min_ptr <= max_ptr:
        midpoint = (min_ptr + max_ptr) // 2
        if ugly_number_count(midpoint) < n:
            min_ptr = midpoint + 1
        else:
            boundaryIndex = midpoint
            max_ptr = midpoint - 1
    return boundaryIndex % (10 ** 9 + 7)

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    res = nth_ugly_number(n, a, b, c)
    print(res)