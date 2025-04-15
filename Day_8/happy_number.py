# Find happy number
# Sum of squares that repeatedly reaches 1 else goes on a loop

def is_happy(n):
    seen_numbers = []

    while n != 1:
        current = n
        total = 0

        while current > 0:
            digit = current % 10       # take the last digit
            total += digit * digit     # square it 
            current = current // 10    #removes last digit

        if total in seen_numbers:
            return False

        seen_numbers.append(total)
        n = total

    return True

n = int(input("Enter a number to check if it is happy or not:  "))
xx = is_happy(n)
if xx:
    print(f'{n}, is a Happy number.')
else:
    print(f'{n}, is NOT a Happy number.')