'''Home work for the lesson 3'''

'''Task 1 - String manipulation'''
list_of_strings = ['helloworld', 'my', 'x']
for item in list_of_strings:
    if len(item) >= 2:
        new_string = item
        print(new_string[:2] + new_string[-2:])
    else:
        print('Empty String')

'''Task 2 - The valid phone number program'''
proper_phone_number = '191687312'

if len(proper_phone_number) != 10:
    print('Phone number should consist of 10 numbers')
elif proper_phone_number.isdigit() == False:
    print('Phone number should not contain any letters or special symbols')
else:
    print('Thank you! This is a valid phone number')

'''Task 3 - The math quiz program'''
mathematical_expression = 121
answer_from_user = input("Solve this problem: (11**2) = ")
if int(answer_from_user) == mathematical_expression:
    print('Answer is RIGHT!')
else:
    print('Answer is FALSE!')

'''Task 4 - The name check'''
stored_name = 'alex'
name_from_user = input("Enter your name: ")
if name_from_user.lower() == stored_name:
    print('The name is RIGHT')
else:
    print('This is a wrong name')