from collections import defaultdict

data = open('input/day11.txt', 'r').read().split('\n')[0].split(' ')
data = [int(a) for a in data]


def apply_rules(num, lookup):
    if num in lookup:
        return lookup[num]
    if num == 0:
        lookup[num] = [1]
    elif len(str(num)) % 2 == 0:
        # Split in half
        alpha = str(num)
        l_len = len(alpha) // 2
        alpha1, alpha2 = alpha[:l_len], alpha[l_len:]
        lookup[num] = [int(alpha1), int(alpha2)]
    else:
        lookup[num] = [num * 2024]
    return lookup[num]


def iterative_count_end_nodes(n):
    # Initialize the count for iteration 0
    current_counts = defaultdict(int)
    for num in data:
        current_counts[num] += 1

    lookup = {}

    for iteration in range(n):
        next_counts = defaultdict(int)
        for num, count in current_counts.items():
            children = apply_rules(num, lookup)
            for child in children:
                next_counts[child] += count
        current_counts = next_counts  # Move to the next iteration

    # Sum all counts in the final iteration
    total = sum(current_counts.values())
    return total
