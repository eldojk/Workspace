"""
http://www.geeksforgeeks.org/dynamic-programming-set-36-cut-a-rope-to-maximize-product/

must make at least one cut.

so if i have len = 4, i made a cut at 3 -> val = (4-3) * max[cut_rope(3), 3]
bcoz since i already made a cut at 3 before calling cut_rope(3), i can use the len 3 rope as it is
without cutting. If i had to cut that too, it would become 2*1 instead of 3 as is.

mx_val = 1 if n = 2
         2 if n = 3
         MAX( MAX(mx_val(i), i) * (n - i) for i in (0, n) if n >= 4 )
"""


def cut_rope(num):
    if num == 2:
        return 1

    elif num == 3:
        return 2

    values = range(num + 1)

    for i in range(4, len(values)):

        values[i] = 0

        for k in range(1, i):
            values[i] = max(values[i], values[k] * (i - k))  # 1 * (4 - 1) and 2 * (4 - 2) and ....

    print values
    return values[num]


if __name__ == '__main__':
    print cut_rope(10)