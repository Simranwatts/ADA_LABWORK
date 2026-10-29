def fractional_knapsack(weights: list[int], values: list[int], capacity: int) -> float:
    items = sorted(
        zip(weights, values),
        key=lambda x: x[1] / x[0],
        reverse=True
    )
    profit = 0
    for weight, value in items:
        if capacity >= weight:
            profit += value
            capacity -= weight
        else:
            profit += value * (capacity / weight)
            break
    return float(profit)
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum Profit:", fractional_knapsack(weights, values, capacity))
