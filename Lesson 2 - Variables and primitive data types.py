'''Home work for the lesson 2'''

'''Task #1 - The greeting program'''
import datetime
name = 'Alex'
date = datetime.date.today().strftime('%A') #Dynamic day is more fun
print(f"Good day {name}! {date} is a perfect day to learn some python.")
good_day_output = "Good day {name}! {date} is a perfect day to learn some python.".format(name = name, date = date)
print(good_day_output)

'''Task #2 - Manipulate strings'''
first_name = 'Alex'
last_name = 'Green'
print('Hello ' + first_name + ' ' + last_name + '! May this ' + date + ' will be great!')

'''Task #3 - Using python as a calculator'''
a, b = 15, 8
print(a + b) #Addition
print(a - b) #Subtraction
print(a / b) #Division
print(a * b) #Multiplication
print(a ** b) #Exponent (Power)
print(a % b) #Modulus
print(a // b) #Floor division