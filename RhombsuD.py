row = 19
index = 0
tmp_index_1 = int(row / 2);
tmp_index_2 = int(row / 2);
for i in range(0, row):
    for j in range(0, row):
        if i <= int(row / 2):
            if tmp_index_1 + index >= j and tmp_index_2 - index <= j:
                print("*", end='')
            else:
                print(" ", end='')
        else:
            if tmp_index_1 + index == j or tmp_index_2 - index == j or j == int(row / 2):
                print("*", end='')
            else:
                print(" ", end='')
    if tmp_index_1 - index == 0:
        tmp_index_1 = 0
        tmp_index_2 = row - 1
        index = 0
        index += 1
print()
