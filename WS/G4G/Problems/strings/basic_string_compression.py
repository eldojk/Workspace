"""
aabcccccaaa -> a2b1c5a3
CTIC - 176, #1.5
"""


def compress(string):
    new_s = ''
    prev_s = string[0]
    curr_count = 1

    for i in range(1, len(string)):
        if string[i] == prev_s:
            curr_count += 1
        else:
            # When something becomes unequal append the current string
            new_s = new_s + prev_s + str(curr_count)
            curr_count = 1
            prev_s = string[i]

    # Append again to handle the last case
    new_s = new_s + prev_s + str(curr_count)

    return new_s
