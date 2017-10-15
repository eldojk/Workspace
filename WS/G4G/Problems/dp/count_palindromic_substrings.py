"""
amzn

http://www.geeksforgeeks.org/count-palindrome-sub-strings-string/
of length >= 2

Input : str = "abaab"
Output: 3
Explanation : All palindrome substring are : "aba" , "aa" , "baab"

Input : str = "abbaeae"
Output: 4
Explanation : All palindrome substring are : "bb" , "abba" ,"aea","eae"


Initial Values : i = 0, j = n-1;
Given string 'str'

CountPS(i, j)

   // If length of string is 2 then we
   // check both character are same or not
   If (j == i+1)
      return str[i] == str[j]

   Else If str[i..j] is PALINDROME
      // increment count by 1 and check for
      // rest palindromic substring (i, j-1), (i+1, j)
      // remove common palindrome substring (i+1, j-1)
      return  countPS(i+1, j) + countPS(i, j-1) + 1 -
                                   countPS(i+1, j-1);

    Else // if NOT PALINDROME
       // We check for rest palindromic substrings (i, j-1)
       // and (i+1, j)
       // remove common palindrome substring (i+1 , j-1)
       return  countPS(i+1, j) + countPS(i, j-1) -
                             countPS(i+1 , j-1);

"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix

"""
Example of maintaining two matrices when we require
"""


def count_pal_substrings(string):
    pal = [[False for i in string] for j in string]
    dp = [[0 for i in string] for j in string]

    for i in range(len(string)):
        pal[i][i] = True

    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            pal[i - 1][i] = True
            dp[i - 1][i] = 1

    for l in range(2, len(string)):
        for i in range(len(string)):

            j = i + l

            if j < len(string):

                if string[i] == string[j] and pal[i + 1][j - 1]:
                    pal[i][j] = True

                if pal[i][j]:
                    dp[i][j] = 1 + dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]  # add sub pals and remove common
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]

    print_matrix(dp)

    return dp[0][len(string) - 1]


if __name__ == '__main__':
    count_pal_substrings('abbaeae')
