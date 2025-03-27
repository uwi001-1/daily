#retrieve name from email address

def get_name_from_email(email):
    name = ""
    for i in range(len(email)):
        if email[i] == "@":
            break
        elif email[i] == ".":
            name += " "
        else:
            name += email[i]
    return name

email = input("Enter the email:  ")
print(get_name_from_email(email))