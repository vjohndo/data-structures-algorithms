def square_root(n: int) -> int:
    if n == 0:
        return 0
    left, right = 1, n
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
