# Return the last letter of each number in the list

def end_letters(numbers):
    new_list = []
    for i in range(len(numbers)):
        n = str(numbers[i])
        new_list.append(n[len(n)-1])
    return new_list

print(end_letters([123, 456, 789, 568945]))