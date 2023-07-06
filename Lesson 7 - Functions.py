'''Home work for the lesson 7'''

'''Task 1 - A simple function'''
users_answer = input('What is your favorite movie? ')
def favorite_movie(users_answer_arg):
    print(f'My favorite movie is named: {users_answer_arg}')

favorite_movie(users_answer)

'''Task 2 - Creating a dictionary'''

dictionary_of_countries ={}
def make_country(country_name, capital):
    dictionary_of_countries.update({country_name: capital, }) 
    return dictionary_of_countries

make_country('Finland', 'Helsinki')
make_country('Spain', 'Madrid')
make_country('Kenia', 'Nairobi')
print(dictionary_of_countries)

'''Task 3 - A simple calculator'''

def make_operation(arithmetic_operator, *args):
    if arithmetic_operator == '+':
        return sum(args)
    elif arithmetic_operator == '-':
        return args[0] - sum(args[1:])
    elif arithmetic_operator == '*':
        calculation_result = 1
        for item in args:
            calculation_result *= item
    elif arithmetic_operator == '/':
        calculation_result = args[0]
        for item in args[1:]:
            calculation_result /= item
    else:
        print('Incorrect argument')
        return None
    return calculation_result
operation_output = make_operation('+', 7, 7, 2)
print(operation_output)
operation_output = make_operation('-', 5, 5, -10, -20)
print(operation_output)
operation_output = make_operation('*', 7, 6)
print(operation_output)
operation_output = make_operation('/', 81, 9)
print(operation_output)