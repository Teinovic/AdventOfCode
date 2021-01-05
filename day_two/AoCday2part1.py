r = open('inputday2.txt').read().splitlines()
transition_list = []
transition_list1 = []
transition_list2 = []

def towards_a_wanted_list(arg):
    for element in arg:
        x = element.split(':')
        transition_list.append(x)

x = towards_a_wanted_list(r)

for element1, element2 in transition_list:
    x, y = element1.strip(), element2.strip()
    transition_list1.append(x.split('-'))
    transition_list2.append(y)

wanted_list = list(zip(transition_list1, transition_list2))

valid_pass = 0

for key, value in wanted_list:
    num_of_letters_lowest = int(key[0])
    num_of_letters_highest = int(key[1][0:2])
    letter_being_looked_for = key[1][-1]
    num_of_letters_in_pass = value.count(letter_being_looked_for)
    if num_of_letters_lowest <= num_of_letters_in_pass <= num_of_letters_highest:
        valid_pass += 1

print(valid_pass)
