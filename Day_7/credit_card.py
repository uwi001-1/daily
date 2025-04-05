#Hide a credit card number

def mask_credit_card(card_number):
    old = str(card_number)
    new = ''
    for i in range(len(old)-4):
        new = new + '*'
    new = new + old[len(old)-4:len(old)]
    return new

ins = int(input("Enter your credit card number: "))
outs = mask_credit_card(ins)
print(f'Your credit card number is {outs}')

# input : 4444444444444444
# ouput : ************4444