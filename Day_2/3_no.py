#Calcualte the accumulating product of a list of numbers

def accumulating_product(numbers):
    new_list = []
    product = 1

    for i in range(len(numbers)):
        product *= numbers[i]
        new_list.append(product)
    return new_list
    
num = [1,2,3,4]
print(accumulating_product(num))