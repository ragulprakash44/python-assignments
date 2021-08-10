str = "hplaptop123456"
digit = letter = 0
for ch in str:
    if ch.isdigit():
        digit = digit + 1
    elif ch.isalpha():
        letter = letter + 1
    else:
        pass
print("Letter count are :", letter)
print("Digit count is:", digit)
