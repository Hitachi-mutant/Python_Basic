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
a, b = -5, 8
print(a + b) #3
print(a - b) #-13
print(a / b) #-0.625
print(a * b) #-40
print(a ** b) #390625
print(a % b) #3
print(a // b) #-1


'''===== Tasks for our group ====='''

'''Task #1 - Email templates'''
first_name = "taras" #it should be input from user
last_name = "shevchenko"
template_with_full_name = first_name + "." + last_name + "@kobzar.com"
template_with_initials = first_name[0] + last_name[0:4] + "@kobzar.com"
template_with_last_name = last_name + "_" + first_name[::-1] + "@kobzar.com"
print(template_with_full_name)
print(template_with_initials)
print(template_with_last_name)

'''Task #2 - ATB cashier'''
customer = 180 #it should be input from user
if customer < 14:
    print("No alchohol or energy drinks for you!")
elif customer >= 14 and customer < 18:
    print("We can sell you energy drinks")
elif customer >= 18:
    print("We can sell you alchohol")
else:
    pass

'''Task #3 - Remove symbols ; and %'''
csv_file = []
