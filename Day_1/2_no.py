#largest of three numbers
a = int(input("Enter first numbers: "))
b = int(input("Enter second numbers: "))
c = int(input("Enter third numbers: "))

if a >b and a>c:
    print(f"{a} is the largest number")
elif b>a and b>c:
    print(f"{b} is the largest number")
elif c>a and c>b:
    print(f"{c} is the largest number")
else: 
    print("The large numbers might be same")