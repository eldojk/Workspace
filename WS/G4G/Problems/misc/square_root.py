"""
amzn

like binary search
http://stackoverflow.com/questions/1623375/writing-your-own-square-root-function

Let's say you want the square root of 62.104. You pick a value halfway between 0 and that, and square it. If the square
is higher than your number, you need to concentrate on numbers less than the midpoint. If it's too low,
concentrate on those higher.
"""


def sqrt(num):
    start = 1
    end = num
    ans = None

    while start <= end:
        mid = (start + end) / 2.0

        sq = mid**2
        if sq == num:
            return mid

        if sq > num:
            end = mid
        else:
            start = mid

        if abs(start - end) < 0.000001:  # accuracy
            break

        ans = mid

    return ans


if __name__ == '__main__':
    print sqrt(3)
    print sqrt(2)
    print sqrt(4)
