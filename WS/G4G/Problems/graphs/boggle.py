"""
amzn, msft

http://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
"""


def is_valid(m, n, i, j):
    return (0 <= i < m) and (0 <= j < n)


def get_neighbours(m, n, i, j):
    valid_candidates = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1),
                        (i + 1, j + 1)]
    valid_neighbours = [tup for tup in valid_candidates if is_valid(m, n, tup[0], tup[1])]
    return valid_neighbours


def find_char(matrix, m, n, char):
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == char:
                return (i, j)

    return None


def boggle(matrix, m, n, word):
    ch1 = word[0]
    used_cells = []
    source = find_char(matrix, m, n, ch1)
    used_cells.append(source)

    if source is None:
        return False

    visited = [False for i in range(len(word))]
    visited[0] = True

    wrdIndex = 1
    while wrdIndex < len(word):
        for neighbour in get_neighbours(m, n, source[0], source[1]):
            if matrix[neighbour[0]][neighbour[1]] == word[wrdIndex] and neighbour not in used_cells:
                visited[wrdIndex] = True
                used_cells.append(neighbour)
                source = neighbour
                break

        if not visited[wrdIndex]:
            return False

        wrdIndex += 1

    return True


if __name__ == '__main__':
    m = [
        ['G', 'I', 'Z'],
        ['U', 'E', 'K'],
        ['Q', 'S', 'E']
    ]
    print boggle(m, 3, 3, 'GEEKS')
    print boggle(m, 3, 3, 'FOR')
    print boggle(m, 3, 3, 'QUIZ')
    print boggle(m, 3, 3, 'GO')
