filename = "input.txt"

with open(filename, "r") as f:
    reports = [list(map(int, line.split())) for line in f.readlines()]

safe_count = 0

for report in reports:
    increasing = True
    decreasing = True
    
    for i in range(len(report) - 1):
        if not (1 <= report[i+1] - report[i] <= 3):
            increasing = False
        if not (1 <= report[i] - report[i+1] <= 3):
            decreasing = False
    
    if increasing or decreasing:
        safe_count += 1
        continue
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        increasing = True
        decreasing = True
        
        for j in range(len(modified_report) - 1):
            if not (1 <= modified_report[j+1] - modified_report[j] <= 3):
                increasing = False
            if not (1 <= modified_report[j] - modified_report[j+1] <= 3):
                decreasing = False
        
        if increasing or decreasing:
            safe_count += 1
            break

print(safe_count)
