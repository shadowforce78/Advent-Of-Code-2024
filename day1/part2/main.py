from collections import Counter

with open("input.txt", "r") as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

right_counts = Counter(right_list)

similarity_score = sum(num * right_counts[num] for num in left_list)

print(similarity_score)
