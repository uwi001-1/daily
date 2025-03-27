#Extract all the numbers from a given string

import re

def extract_numbers(s):
    ru = re.findall(r'\d+', s)
    if not ru:
        return None
    string = ''.join(ru)
    return string

s = input("Enter the string:  ")
print(extract_numbers(s))