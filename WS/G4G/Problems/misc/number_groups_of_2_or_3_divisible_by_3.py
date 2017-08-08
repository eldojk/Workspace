"""
amzn

http://www.geeksforgeeks.org/number-groups-sizes-two-three-divisible-3/

You are given N distinct numbers. You are tasked with finding the number of groups of
2 or 3 that can be formed whose sum is divisible by three.

f we carefully look at every number, we realize that 3 options exist:

The number is divisible by 3
The number leaves a remainder of 1, when divided by 3
The number leaves a remainder of 2, when divided by 3
Now, for groups of two being divisible by 3, either both number have to belong to category 1 (both are divisible by 3),
or one number should leave a remainder 1, and the other a remainder 2. This way the remainders add up to 3, making the
sum divisible by 3.
To form a group of three, either all three numbers should give the same remainder, or one should give remainder 0,
another should give 1, and the last should give 2.

In this way, we do not care about the numbers themselves, but their respective remainders. Thus by grouping them into
three categories, we can find the total possible groups using a simple formula.
Let C1 be number of elements divisible by 3.
Let C2 be number of elements leaving remainder 1.
Let C3 be number of elements leaving remainder 2.

Answer =
C2 * C3 + C1 * (C1 - 1) / 2    --> Groups of 2
+ C1 * (C1 - 1) * (C1 - 2) / 6
+ C2 * (C2 - 1) * (C2 - 2) / 6
+ C3 * (C3 - 1) * (C3 - 2) / 6 --> Groups of 3
                   with elements of same remainder
+ C1 * C2 * C3 --> Groups of three with all
                         distinct remainders
"""


def num_combinations(array):
    c = [0, 0, 0]

    for i in range(len(array)):
        rem = array[i] % 3
        c[rem] += 1

    result = 0

    # groups of 2
    result += (c[1] * c[2]) + (c[0] * (c[0] - 1) / 2)

    # groups of 3
    result += c[0] * ((c[0] - 1) * (c[0] - 2) / 6)
    result += c[1] * ((c[1] - 1) * (c[1] - 2) / 6)
    result += c[2] * ((c[2] - 1) * (c[2] - 2) / 6)

    # groups of 3 with all distinct remainders
    result += c[0] * c[1] * c[2]

    return result


if __name__ == '__main__':
    print num_combinations([1, 5, 7, 2, 9, 14])
    print num_combinations([3, 6, 9, 12])