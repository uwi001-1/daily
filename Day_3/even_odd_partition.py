#Partition a list of integers into two lists: one with all even numbers and the other with all odd numbers

def even_odd_partition(numbers):
    even = []
    odd = []
    for i in range(len(numbers)):
        if numbers[i] %2 == 0:
            even.append(numbers[i])
        else:
            odd.append(numbers[i])
    tup = (even, odd)
    return tup

num = [1,2,3,4,5,6,7,8,9,10,11]
print(even_odd_partition(num))