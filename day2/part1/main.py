filename = "input.txt"

with open(filename, "r") as f:
    reports = f.readlines()

safe_reports_count = 0
for report in reports:
    levels = list(map(int, report.split()))
    increasing = True
    decreasing = True
    for i in range(len(levels) - 1):
        if not (1 <= levels[i+1] - levels[i] <= 3):
            increasing = False
        if not (1 <= levels[i] - levels[i+1] <= 3):
            decreasing = False
    if increasing or decreasing:
        safe_reports_count += 1

print(safe_reports_count)