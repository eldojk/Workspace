"""
amzn, msft

http://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
"""


def is_valid(m, n, i, j):
    return (0 <= i < m) and (0 <= j < n)


def get_neighbours(m, n, i, j):
    valid_candidates = [(i - 1, j), (i + 1, j), (i, j - 1),
                        (i, j + 1), (i - 1, j - 1), (i + 1, j - 1),
                        (i - 1, j + 1), (i + 1, j + 1)]
    valid_neighbours = [tup for tup in valid_candidates if is_valid(m, n, tup[0], tup[1])]
    return valid_neighbours


def boggle_using_bt(matrix, i, j, m, n, word, w_idx, used):
    if w_idx == len(word):
        return True

    for neighbour in get_neighbours(m, n, i, j):
        x = neighbour[0]
        y = neighbour[1]

        if matrix[x][y] != word[w_idx] or used.get(x) == y:
            continue

        used[x] = y
        result = boggle_using_bt(matrix, x, y, m, n, word, w_idx + 1, used)

        if result:
            return True

        if used.get(x) == y:
            used.pop(x)

    return False


def boggle_using_back_tracking(matrix, m, n, word):
    used = {}
    # ^ todo just use a boolean matrix

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == word[0]:
                used[i] = j
                result = boggle_using_bt(matrix, i, j, m, n, word, 1, used)

                if result:
                    return True

                if used.get(i) == j:
                    used.pop(i)

    return False


if __name__ == '__main__':
    print ''
    _m = [
        ['G', 'I', 'Z'],
        ['U', 'E', 'K'],
        ['Q', 'S', 'E']
    ]
    print boggle_using_back_tracking(_m, 3, 3, 'GEEKS')
    print boggle_using_back_tracking(_m, 3, 3, 'FOR')
    print boggle_using_back_tracking(_m, 3, 3, 'QUIZ')
    print boggle_using_back_tracking(_m, 3, 3, 'GO')
