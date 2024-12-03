import re

with open("input.txt", "r") as file:
    memory = file.read()

pattern = re.compile(r"mul\((\d+),(\d+)\)")
matches = pattern.findall(memory)
total = sum(int(x) * int(y) for x, y in matches)

print(total)
