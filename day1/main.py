filename = 'input.txt'
def total_distance_from_file(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            # 3 espaces entre les deux nombres
            left, right = map(int, line.strip().split('   '))
            left_list.append(left)
            right_list.append(right)
    
    # Sort les listes
    left_list.sort()
    right_list.sort()

    # Distance totale
    distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return distance

result = total_distance_from_file(filename)
print("Distance totale :", result)
