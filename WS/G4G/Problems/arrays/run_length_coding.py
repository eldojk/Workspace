"""
amzn, msft

http://www.geeksforgeeks.org/run-length-encoding/
"""


def run_length_encoding(string):
    i = 0
    destination = []

    while i < len(string):
        destination.append(string[i])
        cnt = 1

        while i + 1 < len(string) and string[i] == string[i + 1]:
            cnt += 1
            i += 1

        destination.append(str(cnt))
        i += 1

    return ''.join(destination)


if __name__ == '__main__':
    print run_length_encoding('geeksforgeeks')
