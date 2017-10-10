"""
amzn

http://www.geeksforgeeks.org/minimize-cash-flow-among-given-set-friends-borrowed-money/

{0, 1000, 2000},
{0, 0, 5000},
{0, 0, 0}
"""
from sys import maxint


def fill_credit_and_debits(graph):
    amounts = [0 for i in graph]

    for i in range(len(graph)):
        for j in range(len(graph[0])):

            # amount for i += amount i have to get from j - amount i has to give j
            amounts[i] += (graph[j][i] - graph[i][j])

    return amounts


def find_max_creditor_and_min_debitor(amounts):
    _max = 0
    _min = 0
    max_val = -maxint
    min_val = maxint

    for i in range(len(amounts)):
        if amounts[i] > max_val:
            max_val = amounts[i]
            _max = i

        if amounts[i] < min_val:
            min_val = amounts[i]
            _min = i

    return _min, _max


def settle_debts(amounts):
    max_debitor, max_creditor = find_max_creditor_and_min_debitor(amounts)

    max_credit = amounts[max_creditor]
    max_debit = amounts[max_debitor]

    if max_credit == 0 and max_debit == 0:
        return

    _min_amount = min(max_credit, abs(max_debit))

    amounts[max_debitor] += _min_amount
    amounts[max_creditor] -= _min_amount

    print 'Person {0} should pay {1} ${2}'.format(max_debitor, max_creditor, _min_amount)

    settle_debts(amounts)


if __name__ == '__main__':
    g = [[0, 1000, 2000],
        [0, 0, 5000],
        [0, 0, 0]]
    amts = fill_credit_and_debits(g)
    print amts
    settle_debts(amts)
