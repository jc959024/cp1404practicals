for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# c
number = int(input("number of stars："))
for i in range(number):
    print('*', end='')
print()
# d
lines_of_stars = int(input("lines of increasing stars:"))
for i in range(lines_of_stars):
    for j in range(i + 1):
        print('*', end='')
    print()