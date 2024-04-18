def bank(x, y):
    total = x
    for i in range(y):
        total += total*0.1
    return total

print(bank(100, 10))