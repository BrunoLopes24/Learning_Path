largest_so_far = -1
print('Antes, ', largest_so_far)
for num in [9, 41, 15, 99, 22, 200, 3]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)
print('Depois, ', largest_so_far)
