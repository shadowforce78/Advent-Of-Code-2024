filename = 'input.txt'
with open(filename) as file:
    lines = file.readlines()

directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
count = 0
grid = [list(line.strip()) for line in lines]

for x in range(len(grid)):
    for y in range(len(grid[0])):
        for dx, dy in directions:
            found = True
            for i in range(4):
                nx, ny = x + i * dx, y + i * dy
                if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] != 'XMAS'[i]:
                    found = False
                    break
            if found:
                count += 1

print(count)