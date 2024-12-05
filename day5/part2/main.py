filename = 'input.txt'

def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
    rules = []
    updates = []
    for line in lines:
        if '|' in line:
            x, y = map(int, line.split('|'))
            rules.append((x, y))
        elif line:  # Ensure the line is not empty
            updates.append(list(map(int, line.split(','))))
    return rules, updates

def is_correct_order(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def correct_order(update, rules):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    indegree = defaultdict(int)
    for x, y in rules:
        graph[x].append(y)
        indegree[y] += 1
        if x not in indegree:
            indegree[x] = 0

    queue = deque([node for node in update if indegree[node] == 0])
    ordered_update = []

    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Ensure all nodes in the update are included in the ordered list
    remaining_nodes = set(update) - set(ordered_update)
    ordered_update.extend(remaining_nodes)

    return ordered_update

def find_middle_sum(updates, rules):
    middle_sum = 0
    for update in updates:
        if update:  # Ensure the update is not empty
            if not is_correct_order(update, rules):
                update = correct_order(update, rules)
            middle_sum += update[len(update) // 2]
    return middle_sum

rules, updates = parse_input(filename)
incorrect_updates = [update for update in updates if not is_correct_order(update, rules)]
result = find_middle_sum(incorrect_updates, rules)
print(result)
