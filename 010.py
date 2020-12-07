def is_prime(n):
    prime = True
    # n/2 | √n => improve Algorithm
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    return prime


prime_count = 0
last_prime_number = 0
for j in range(1, 1000001):
    if is_prime(j):
        last_prime_number = j
        prime_count = prime_count + 1
print("total prims", prime_count, "last prime number is", last_prime_number)
