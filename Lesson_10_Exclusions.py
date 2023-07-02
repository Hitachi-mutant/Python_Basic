'''Home work for the lesson 10 - Errors and Exceptions '''

'''Task 1 - Write a function called oops that explicitly raises an IndexError'''
my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2, 'c': 3}
def oops(arg_list):
    return arg_list[len(arg_list)]  # Add len(arg_list)-1 to escape the IndexError

try:
    def call_oops():
        result = oops(my_list)
        return print(result)
    call_oops()
    print(my_dict['d'])
except IndexError:
    print('Here is your IndexError')
except KeyError:
    print('Here is your KeyError')


'''Task 2 - construct a try-except block which raises an exception 
if the two values given by the input function were not numbers'''

a = (input('Enter number A:  '))
b = (input('Enter number B:  '))

try:
    def calc_a_b(arg_a, arg_b):
        result = int(arg_a) **2 / int(arg_b)
        return result
    print(calc_a_b(a, b))
except ValueError:
    print('Please, input integer numbers!')
except ZeroDivisionError:
    print('You can not divide by 0!')