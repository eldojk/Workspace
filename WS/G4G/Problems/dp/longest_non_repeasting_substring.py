"""
amzn, msft

http://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
"""


def longest_non_repeating_substring(string):
    # last occurrence of a character
    last_occurrence = [-1 for i in range(26)]
    longest_substring_length = 0
    current_length = 0

    for i in range(len(string)):
        char = string[i]
        idx = ord(char) - ord('a')

        # character not previously occurred
        if last_occurrence[idx] == -1:
            current_length += 1  # add current char to substring

            if current_length > longest_substring_length:
                longest_substring_length = current_length

        else:
            # update longest len before current len is changed ( this required?? )
            if current_length > longest_substring_length:
                longest_substring_length = current_length

            # ignore the current substring and start considering from right of last occurrence
            current_length = i - last_occurrence[idx]

            # update ast occurrence every time
        last_occurrence[idx] = i

    return longest_substring_length


if __name__ == '__main__':
    print longest_non_repeating_substring('ABDEFGABEF'.lower())
