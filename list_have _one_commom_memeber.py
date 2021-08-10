def check(list1, list2):
    result = False
    for a in list1:
        for b in list2:
            if a == b:
                result = True
                return result


print(check([12345, 2441, 314365, 434561, 51436, 63146, 7346, 84643, 9], [5, 6, 7, 8, 9]))
print(check([1, 2, 3, 4, 5, 11, 12, 13, 234, 2354, 26235], [6, 7, 8, 9]))
