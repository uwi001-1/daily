# Divide a certain number of chocolates among a group of children

def divide_chocolates(chocolates, children):
    get = chocolates // children
    remain = chocolates % children
    return get, remain

choco = int(input("Enter the number of chocolates:  "))
child = int(input("Enter the number of children:  "))
get, remain = divide_chocolates(choco, child)
print(f'Each child gets {get} chocolates.\nRemaining: {remain}')