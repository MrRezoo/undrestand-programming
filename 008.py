n = 13

prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False

if prime:
    print("it is prime")
else:
    print("is is not prime")

