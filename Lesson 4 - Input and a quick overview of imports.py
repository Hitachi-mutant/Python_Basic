'''Home work for the lesson 4'''

'''Task 1 - The Guessing Game'''

import random
random_number = random.randint(1, 10)
user_answer = input('Guess a number between 1 and 10: ')
if user_answer == random_number:
    print('You guessed Right!')
else:
    print('No, this is wrong. The right number was: ' + str(random_number))

'''Task 2 - The birthday greeting program'''

users_name = input('Enter your name: ')
users_age = float(input('Enter your age: '))

if users_age:
    users_age = int(users_age) + 1
    print(f'Hello {users_name}, on your next birthday you’ll be {users_age} years')
else:
    print('Enter your proper age')

'''Task 3 - String with characters combination'''

import random   #we imported this earlier, but just in case this module will be run separately

user_string_for_combination = input("Enter a string: ")
for item in range(5):
    new_random_string = ''.join(random.sample(user_string_for_combination, len(user_string_for_combination))) #we use .join to make it a string, not a list
    print(new_random_string)