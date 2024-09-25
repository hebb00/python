import math

def mySqrt(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    start = 1
    mid = 0
    high = x
    while start < high:
        mid = (start + high) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            start = mid + 1
        else:
            high = mid - 1
    return math.floor(mid)








if __name__ == "__main__":

    print(mySqrt(99))