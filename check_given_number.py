def check(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False

print(check([1, 5, 8, 3], -1))
print(check([1, 5, 8, 3], 3))
print(check([1, 5, 8, 6, 7, 8, 9, 0, 3], 3))

