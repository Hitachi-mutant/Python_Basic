'''Home work for the lesson 5'''

'''Task 1 - The greatest number'''
import random
i = 0
list_of_random_numbers = []
while i < 10:
    random_number_element = random.randint(1, 100)
    list_of_random_numbers.append(random_number_element)
    i += 1
print(max(list_of_random_numbers))
print(list_of_random_numbers) #Show the list to make sure that MAX is picked properly

'''Task 2 - Exclusive common numbers'''

import random  #imported in Task 1
i = 0
list_of_random_numbers_1, list_of_random_numbers_2 = [], []
while i < 10:
    random_number_element_1 = random.randint(1, 40)
    random_number_element_2 = random.randint(1, 40)
    list_of_random_numbers_1.append(random_number_element_1)
    list_of_random_numbers_2.append(random_number_element_2)
    i += 1

#to use intersection method we have to convert lists into sets
common_integers = list(set(list_of_random_numbers_1).intersection(list_of_random_numbers_2))
print(common_integers)

'''Task 3 - Extracting numbers'''

list_from_1_to_100 = list(range(0,101))
divisible_by_7_and_not_5 = []
i = 0
while i < 100:
    if list_from_1_to_100[i] % 7 == 0 and list_from_1_to_100[i] % 5 != 0:
        divisible_by_7_and_not_5.append(list_from_1_to_100[i])
    i += 1
else: pass
print(divisible_by_7_and_not_5)