def knapsack(values, weights, capacity):
    n = len(values)
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i, w in enumerate(weights):
        for j in range(n + 1):
            # incorporate the capacity
            pass
    return table[n][n]

def test_knapsack():
    values = [1, 6, 18, 22, 28]
    weights = [1, 2, 5, 6, 7]
    assert knapsack(values, weights) == 40
