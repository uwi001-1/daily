#Check if a list contains three consecutive common numbers

def check_consecutive_numbers(numbers):
    for i in range(len(numbers)-2):
        if numbers[i] == numbers[i+1] and numbers[i] == numbers[i+2]:
            return True
    return False

print(check_consecutive_numbers([1, 2, 2, 2, 3, 4])) 