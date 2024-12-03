import re

with open('input.txt', 'r') as file:
    data = file.read()

total_sum = 0
enabled = True

mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r"don't\(\)")

for match in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)', data):
    if do_pattern.fullmatch(match.group(0)):
        enabled = True
    elif dont_pattern.fullmatch(match.group(0)):
        enabled = False
    elif enabled and mul_pattern.fullmatch(match.group(0)):
        x, y = int(match.group(1)), int(match.group(2))
        total_sum += x * y

print(total_sum)
