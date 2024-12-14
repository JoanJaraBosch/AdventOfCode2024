from collections import defaultdict, deque


def print_order():
    dictionary = {}
    result = 0
    with open("input/day5_part1.txt", 'r') as file:
        for line in file:
            seq = line.replace("\n", "").split("|")
            if seq[0] not in dictionary:
                dictionary[seq[0]] = []
            dictionary[seq[0]].append(seq[1])

    with open("input/day5_part2.txt", 'r') as file:
        for line in file:
            is_valid = True
            line = line.strip().split(",")  # clean line to ","

            # Check order
            for x in dictionary:
                for y in dictionary[x]:
                    if x in line and y in line:
                        if line.index(x) > line.index(y):
                            is_valid = False
                            break
                if not is_valid:
                    break

            if is_valid:
                middle_index = len(line) // 2
                result += int(line[middle_index])

    return result


def print_order_and_fix():
    dictionary = defaultdict(list)
    incorrect_updates = []
    fixed_sum = 0

    with open("input/day5_part1.txt", 'r') as file:
        for line in file:
            seq = line.strip().split("|")
            dictionary[seq[0]].append(seq[1])

    with open("input/day5_part2.txt", 'r') as file:
        for line in file:
            is_valid = True
            update = line.strip().split(",")

            for x in dictionary:
                for y in dictionary[x]:
                    if x in update and y in update:
                        if update.index(x) > update.index(y):
                            is_valid = False
                            break
                if not is_valid:
                    incorrect_updates.append(update)
                    break

    def topological_sort(pages, rules):
        in_degree = defaultdict(int)
        graph = defaultdict(list)

        for index_x, dependencies in rules.items():
            for index_y in dependencies:
                graph[index_x].append(index_y)
                in_degree[index_y] += 1

        queue = deque([page for page in pages if in_degree[page] == 0])
        sorted_pages = []

        while queue:
            current = queue.popleft()
            sorted_pages.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_pages

    for update in incorrect_updates:
        relevant_rules = {x: [y for y in ys if y in update] for x, ys in dictionary.items() if x in update}

        ordered_update = topological_sort(update, relevant_rules)

        middle_index = len(ordered_update) // 2
        fixed_sum += int(ordered_update[middle_index])

    return fixed_sum
