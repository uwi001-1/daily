#Count the number of unique email addresses from a list of emails 

def count_unique_emails(emails):
    unique_emails = set(emails)  # Set stores only unique elements
    return len(unique_emails)

emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com"]
print(count_unique_emails(emails))  # Output: 3
