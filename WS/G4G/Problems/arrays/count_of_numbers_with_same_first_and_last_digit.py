"""
amzn

#tricky
http://www.geeksforgeeks.org/count-numbers-first-last-digits/

From 120 to 130, only 121 has same starting and ending digit
From 440 to 450, only 444 has same starting and ending digit
From 1050 to 1060, only 1051 has same starting and ending digit

From above examples, we can observe that in each ten number span we have only one number which
has the given property except 1 to 10 which has 9 numbers (all one digit number) having same
starting and ending digit.

Using above property we can solve given problem, first we break the given interval into two parts
that is if interval is l to r, we break this into 1 to l and 1 to r, our answer is obtained by
subtracting result of first query from second query.

Now we remain to find count of numbers with given property in range 1 to x, for this we divide x by
10, which gives number of 10-spans. We add 9 to the span for taking one digit numbers into account.
If last digit of x is smaller than first digit of x, then 1 should be decreased in final answer to
discard last ten span number because that number is out of range.
"""


def get_first_digit(x):
    while x > 10:
        x //= 10

    return x


def get_count_from_1(num):
    if num < 10:
        return num

    spans = num // 10

    result = spans + 9

    first_digit = get_first_digit(num)
    last_digit = num % 10

    if last_digit < first_digit:
        result -= 1

    return result


def get_count(start, end):
    return get_count_from_1(end) - get_count_from_1(start - 1)


if __name__ == '__main__':
    print get_count(5, 40)