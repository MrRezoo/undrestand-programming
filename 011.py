def div(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False


jam = 0
for i in range(1, 10000):
    if div(i):
        jam = jam + i

print(jam)
