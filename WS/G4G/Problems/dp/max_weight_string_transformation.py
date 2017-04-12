"""
http://www.geeksforgeeks.org/maximum-weight-transformation-of-a-given-string/

Input: str = "AA"
Output: 3
Transformations of given string are "AA", "AB", "BA" and "BB".
Maximum weight transformation is "AB" or "BA".  And weight
is "One Pair - One Toggle" = 4-1 = 3.

Input: str = "ABB"
Output: 5
Transformations are "ABB", "ABA", "AAB", "AAA", "BBB",
"BBA", "BAB" and "BAA"
Maximum weight is of original string 4+1 (One Pair + 1
character)

If (n == 1)
   maxWeight(str[0..n-1]) = 1

Else If str[0] != str[1]
// Max of two cases: First character considered separately
//                   First pair considered separately
maxWeight(str[0..n-1]) = Max (1 + maxWeight(str[1..n-1]),
                              4 + getMaxRec(str[2..n-1])
Else
// Max of two cases: First character considered separately
//                   First pair considered separately
// Since first two characters are same and a toggle is
// required to form a pair, 3 is added for pair instead
// of 4
maxWeight(str[0..n-1]) = Max (1 + maxWeight(str[1..n-1]),
                              3 + getMaxRec(str[2..n-1])
"""


def find_max_weight(string):
    dp = [0 for i in range(len(string) + 1)]

    # dp[i] is the maximum possible weight using first i characters dp[n+1];
    dp[0] = 0  # empty string
    dp[1] = 1  # single char

    for i in range(2, len(string) + 1):
        dp[i] = 1 + dp[i - 1]

        if string[i - 1] != string[i - 2]:
            dp[i] = max(
                dp[i],
                4 + dp[i - 2]
            )
        else:
            dp[i] = max(
                dp[i],
                3 + dp[i - 2]
            )

    return dp[len(string)]


if __name__ == '__main__':
    print find_max_weight('AAAAABB')
