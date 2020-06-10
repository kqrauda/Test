from collections import Counter

def check_number_not_descending(number_str):
    for i in range(len(number_str)-1):
        if  number_str[i] > number_str[i+1]:
            return False
    return True

def check_number(number_str):
    # first condition
   
    if not check_number_not_descending(number_str):
        return False

    # second condition
    counter = Counter(number_str)
    groups_count = 0
    for a in counter.values():
        if a >= 2:
            groups_count += 1

    return groups_count >= 2
matching_passwords = 0
for i in range(372**2, 809**2+1):
    if check_number(str(i)):
        print(i)

        matching_passwords += 1
       
print("matching_passwords",matching_passwords)
