profits = [1, 2, 5, 6]
weights = [2, 3, 4, 5]
capacity = 8

states = {(0, 0)}  # (weight, profit)

for i in range(len(weights)):
    new_states = set(states)
    for w, p in states:
        nw = w + weights[i]
        np = p + profits[i]
        if nw <= capacity:
            new_states.add((nw, np))
    states = new_states

# maximum profit
max_profit = max(p for w, p in states)
print(max_profit)
