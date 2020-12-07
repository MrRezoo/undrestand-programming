def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


first = 1
seccond = 2
jam = 0

while first < 4 * 10 ** 6:
    if is_even(first):
        jam = jam + first
    new = first + seccond
    first = seccond
    seccond = new
print(jam)
