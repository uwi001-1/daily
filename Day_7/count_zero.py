# Count the number of zeros in binary representation of a number

def count_zeroes(n):
    #convert to binary first
    binary = str(bin(n)[2:])
    count = 0
    for i in range(len(binary)):
        if binary[i] == "0":
            count += 1
    return count 

num = int(input("Enter the number:  "))
outs = count_zeroes(num)
print(f'The number of zeros in binary represenation is {outs}')