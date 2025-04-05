#Check if a number is Disarium or not
# for 175  --> 1^1 + 7^2 + 5^3 = 175

def is_disarium_number(num):
    n = str(num)
    total = 0
    for i in range(len(n)):
        total = total + (int(n[i])**(i+1))
    if num == total:
        return True
    else:
        return False

num = int(input("Enter the number:  "))
print(is_disarium_number(num))