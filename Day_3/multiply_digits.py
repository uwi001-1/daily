#Multiply the digits of the number

def multiply_digits(n):
    dig = 1
    for i in str(n):   
        dig *= int(i)  
    return dig

num = int(input("Enter the number:  "))
print(multiply_digits(num))