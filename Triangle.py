x = int(input("enter number of rows: "))
k = 2
for i in range(x):
    print('%s%s' % (' ' * (x - i - 1), '*' * (i * 2 + 1)))
