#Return the number of prime numbers that are strictly less than a given integer

def count_primes(n):
    number = 0
    for i in range(2, n):
        count = 0
        for x in range(1, i + 1):
            if i % x == 0:
                count += 1
        if count == 2:
            number += 1
    return number

num = int(input("Enter the number to find count of prime numbers below it:  "))
print(count_primes(num))