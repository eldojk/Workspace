"""
amzn

http://www.geeksforgeeks.org/run-length-encoding/
"""


def encode(string):
    curr_char = string[0]
    curr_cnt = 1
    encoding = []

    for i in range(1, len(string)):
        if string[i] == curr_char:
            curr_cnt += 1

        else:
            encoding.append(curr_char)
            encoding.append(str(curr_cnt))
            curr_char = string[i]
            curr_cnt = 1

    encoding.append(curr_char)
    encoding.append(str(curr_cnt))

    return ''.join(encoding)


if __name__ == '__main__':
    print encode('wwwwaaadexxxxxx')
