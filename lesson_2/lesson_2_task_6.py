lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
result = []
for i in lst:
    if i < 30 and i % 3 == 0:
        result.append(str(i))
result = ', '.join(result) # не поняла точно, устроит ли, если просто список выведется в ответе, поэтому перевела в строку на всякий случай
print(result)