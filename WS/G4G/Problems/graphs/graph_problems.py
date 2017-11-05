"""
amzn

#tricky
http://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/
"""
from Queue import Queue


def is_adjacent_word(w1, w2):
    diff = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1

        if diff > 1:
            return False

    return True if diff == 1 else False


def min_length_chain(words, src, tgt):
    visited = [False for w in words]
    q = Queue()
    dist = [0 for w in words]
    q.put(src)

    while not q.empty():
        node = q.get()
        for i in range(len(words)):
            if not visited[i]:
                if is_adjacent_word(words[node], words[i]):
                    dist[i] = dist[node] + 1
                    q.put(i)

                    if tgt == i:
                        print dist
                        return dist[i]

        visited[node] = True

    return dist[tgt]


if __name__ == '__main__':
    words = ['TOON', 'POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
    print min_length_chain(words, 0, 5)
