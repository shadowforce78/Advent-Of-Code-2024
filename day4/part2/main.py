with open("input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

rows = len(grid)
cols = len(grid[0])

count = 0

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if grid[i][j] == "A":
            if (
                grid[i - 1][j - 1] == "M"
                and grid[i][j] == "A"
                and grid[i + 1][j + 1] == "S"
            ):
                count += 1
            if (
                grid[i - 1][j - 1] == "S"
                and grid[i][j] == "A"
                and grid[i + 1][j + 1] == "M"
            ):
                count += 1
            if (
                grid[i - 1][j + 1] == "M"
                and grid[i][j] == "A"
                and grid[i + 1][j - 1] == "S"
            ):
                count += 1
            if (
                grid[i - 1][j + 1] == "S"
                and grid[i][j] == "A"
                and grid[i + 1][j - 1] == "M"
            ):
                count += 1

print(count)
