filename = 'input.txt'

with open(filename, 'r') as file:
    lines = file.read().strip().split('\n')

rules = []
updates = []
is_update_section = False

for line in lines:
    if line == '':
        is_update_section = True
        continue
    
    if is_update_section:
        updates.append(list(map(int, line.split(','))))
    else:
        x, y = map(int, line.split('|'))
        rules.append((x, y))

correct_updates = []
for update in updates:
    index_map = {page: idx for idx, page in enumerate(update)}
    correct = True
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                correct = False
                break
    if correct:
        correct_updates.append(update)

middle_pages = [update[len(update) // 2] for update in correct_updates]
result = sum(middle_pages)
print(result)