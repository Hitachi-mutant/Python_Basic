'''===== Tasks from Lesson 2 ====='''


'''Task #1: Email templates - Вам потрібно запропонувати замовнику декілька варіантів 
створення електронних пошт для його працівників. 
Реалізуйте функціонал генерування пошт
(з 3-ма варіантами, як приклад- taras.shevchenko@kobzar.com, tshev@kobzar.com і тд).'''

first_name = "taras" #it should be input from user
last_name = "shevchenko"
template_with_full_name = first_name + "." + last_name + "@kobzar.com"
template_with_initials = first_name[0] + last_name[0:4] + "@kobzar.com"
template_with_last_name = last_name + "_" + first_name[::-1] + "@kobzar.com"
print(template_with_full_name)
print(template_with_initials)
print(template_with_last_name)


'''Task #2 - ATB cashier: Ви - злий касир в АТБ і продаєте алкогольні напої лише особам старше 18 років.
Людям, старше 14 років і молодше 18 років, ви продаєте лише енергетичні напої. Всім решта - будь-що.
Напишіть функціонал на пайтоні, який реалізує цей алгоритм.'''

customer = 180 #it should be input from user
if customer < 14:
    print("No alchohol or energy drinks for you!")
elif customer >= 14 and customer < 18:
    print("We can sell you energy drinks")
elif customer >= 18:
    print("We can sell you alchohol")
else:
    pass


'''Task #3 - Remove symbols ; and %: Ви працюєте на проекті, який займається тим, що опрацьовує дані 
по платежах клієнтів від різних платіжних систем. Дані зберігаються в csv-файлах на Linux сервері.
При перекидуванні даних на Windows сервер виявилось, що віндовс додає специфічні символи 
на позначення початку (";") і закінчення стрічки ("%") з зашифрованим Transaction ID
(було "yu7i9om0iymn", стало ";yu7i9om0iymn%"). Це критичний баг для проекту.
Реалізуйте механізм на пайтоні, який буде видаляти непотрібні символи з початку і кінця Transaction ID.'''

csv_file = ['Client first name', 'Client last name', ';Transaction ID%', 'Transaction velue', 'Address of the sender', 'Address of the receiver']
for item in range(len(csv_file)):
    if 'Transaction ID' in csv_file[item]:
        csv_file[item] = csv_file[item].replace(';', "").replace('%', "")
print(csv_file)


'''Task #4 - Remove random & symbol: Умова та ж сама, але тепер віндовс рандомно додає знак 
"&" в будь-яку позицію в стрічці Transaction ID (Було "yu7i9om0iymn", стало "yu&7i9om&0iym&n").
Реалізуйте функціонал, який буде видаляти знак "&" зі стрічки.'''

csv_file = ['Client first nam&e', 'Client last name', 'Transaction ID', 'Tran&saction velue', 'Address& of the sender', 'Address of the receiver']
for item in range(len(csv_file)):
    if '&' in csv_file[item]:
        csv_file[item] = csv_file[item].replace('&', "")
print(csv_file)



'''===== Tasks from Lesson 3 ====='''


'''Task #1 - Email templates :Реалізуйте функціонал генерування пошт для компанії "kobzar.com",
де користувач повинен самостійно вводити своє ім'я і прізвище з терміналу.'''

first_name_input = input('Enter your First Name')
last_name_input = input('Enter your Last Name')
print(f'Your generated email: {first_name_input}.{last_name_input}@kobzar.com')


'''Task #2 - Call me back: Ви - настирливий продавець і коли хтось відвідує ваш сайт онлайн-магазину, 
ви запитуєте 5 разів у користувача, чи потрібно йому передзвонити. 
На 6-ий раз ви нарешті лишаєте покупця в спокої і бажаєте йому гарних покупок.'''

i = 0
while i < 5:
    answer = input("Would you like me to call you back? - y/n  ")
    if answer == "y":
        print('We will call you back')
        break
    elif answer == 'n':
        print('We will not bother you anymore')
        break
    i += 1
else: print('Have a good day then')


'''Task #3 - more pushy salesman: Ви - тепер ще більш настирливий продавець і коли користувач відвідує ваш сайт, 
ви прямо таки постійно питаєте у нього, чи потрібно йому передзвонити для формування замовлення. 
Допоки користувач не натиснув кнопку "ні, дякую", ви постійно нагадуватимете йому про дзвінок.
*під натисканням кнопки ми зараз маємо на увазі ввід користувача з терміналу'''

while True:
    answer = input("Would you like me to call you back? - y/n  ")
    if answer == "y":
        print('We will call you back')
        break
    elif answer == 'n':
        print('We will not bother you anymore')
        break


'''Task #4 - Free pens and rulers: Ви - власник онлайн магазину канцтоварів.
Кожному 3-му покупцю ви обіцяєте в подарунок ручку до замовлення, а кожному 5-му - лінійку.
*розгляньте випадок, коли покупець може бути і 3-ій і 5-им (75-ий покупець, до прикладу).
*для проходження по всій кількості покупців використайте range() ф-ю в циклі for. Кількість покупців ви можете задати вручну, 
або скористатись ф-єю input() і ввести к-сть з терміналу
*Додайте функціонал на випадок, якщо користувач промахнувся по клавіатурі і ввів замість числа якусь абракадабру (ф-я isdigit())'''

amount = input('Please enter the amount of customers: ')
if amount.isdigit():
    amount = int(amount)
    numbers = range(1, amount)
    for number in numbers:
        if number % 3 == 0 and number % 5 != 0:
            print("Here is a free PEN!")
            print(number) # I print a number to make sure that we give gifts to proper customers
        elif number % 5 == 0 and number % 3 != 0:
            print("Here is a free RULER!")
            print(number)
        elif number % 3 == 0 and number % 5 == 0:
            print("Free PEN and RULER for You!")
            print(number)
        else: pass
else: print('Invalid input. The amount of customers must be an integer number')



'''===== Tasks from Lesson 4 ====='''


'''Task #1 - Infinite string Calculater: Запрограмуйте програму калькулятор, яка буде приймати від 
користувача введення 2-х чисел та вид математичної операції (+, -, *, /). 
Виведіть результат операції та продовжуйте виконання калькулятора, поки користувач не введе символ "q" для виходу.'''

'''while True:      #The task has to be commented because it is an infinite loop
    first_number = input('Enter the first number: ')
    if first_number == 'q':
        exit()
    second_number = input('Enter the second number: ')
    if second_number == 'q':
        exit()
    operation_sign = input('Enter operation sign: ')
    if operation_sign == 'q':
        exit()

    if first_number.isdigit() and second_number.isdigit():
        first_number = int(first_number)
        second_number = int(second_number)
        if operation_sign == '-':
            output = first_number - second_number
        elif operation_sign == '+':
            output = first_number + second_number
        elif operation_sign == '*':
            output = first_number * second_number
        elif operation_sign == '/':
            output = first_number / second_number
        print(output)'''


'''Task #2 - List of employee emails:"Знову генеруємо пошту для працівника, але тепер всі дані містяться в списку
[""name"", ""surname"", ""domain""]"'''

input_firs_name = input('Enter your First Name: ')
input_last_name = input('Enter your Last Name: ')
list_of_employees = []
list_of_employees.append(input_firs_name)
list_of_employees.append(input_last_name)
list_of_employees.append('@kobzar.com')
employee_email = list_of_employees[0] + '.' + list_of_employees[1] + list_of_employees[2]
print(employee_email)


'''Task #3 - Emails in nested lists:"Те ж саме завдання із генеруванням пошти, але тепер у вас декілька працівників (нехай буде 5). 
Спробуйте використати вкладені списки" '''

i = 1
while i <= 3:
    input_firs_name = input('Enter your First Name: ')
    input_last_name = input('Enter your Last Name: ')
    if i == 1:
        employee_data_1 = [input_firs_name, input_last_name, '@kobzar.com']
    elif i == 2:
        employee_data_2 = [input_firs_name, input_last_name, '@kobzar.com']
    elif i == 3:
        employee_data_3 = [input_firs_name, input_last_name, '@kobzar.com']
    i += 1

all_employees = [employee_data_1, employee_data_2, employee_data_3]
print(all_employees)
        # The easy way
'''employee_email_1 = all_employees[0][0] + '.' + all_employees[0][1] + all_employees[0][2]
print(employee_email_1)
employee_email_2 = all_employees[1][0] + '.' + all_employees[1][1] + all_employees[1][2]
print(employee_email_2)
employee_email_3 = all_employees[2][0] + '.' + all_employees[2][1] + all_employees[2][2]
print(employee_email_3)'''

for list_of_employee_emails in all_employees:
    employee_email = '' + list_of_employee_emails[0] + list_of_employee_emails[1] + list_of_employee_emails[2]
    print(employee_email)


'''Task #4 - Warehouse management systems:Створіть програму для керування списком продуктів в інтернет-магазині. 
Кожен продукт може мати назву, ціну та кількість на складі. Реалізуйте можливість користувачу 
додавати нові продукти, оновлювати інформацію про продукти та виводити список доступних 
продуктів за певними критеріями (наприклад, за ціною або наявністю на складі). '''

# Basic data
warehouse_list = [
    {
    'Product Name' : 'T-shirt',
    'Product Price - $' : 15,
    'In stock' : 54,
    'Product ID' : 1,
    },
    {
    'Product Name' : 'Pants',
    'Product Price - $' : 9,
    'In stock' : 0,
    'Product ID' : 2,
    },
    {
    'Product Name' : 'Jeans',
    'Product Price - $' : 26,
    'In stock' : 80,
    'Product ID' : 3,
    }
]

# Data for a new product
product_name = input('Enter Product Name: ')
product_price = input('Enter Product Price ($): ')
product_stock = input('Enter Product amount in Stock: ')

new_item_to_add = {
'Product Name' : product_name,
'Product Price - $' : product_price,
'In stock' : product_stock,
'Product ID' : len(warehouse_list)+1,
}

# Adding the new product to the list
warehouse_list.append(new_item_to_add)
print(warehouse_list)

# Editing the data in the warehouse_list
product_id_to_edit = int(input('Choose the ID of the product you want to edit: '))
for item in warehouse_list:
    if item['Product ID'] == product_id_to_edit:
        new_product_name = input('Enter new product Name: ')
        new_product_price = input('Enter new product Price: ')
        new_product_stock = input('Enter new product amount in Stock: ')
        item['Product Name'] = new_product_name
        item['Product Price - $'] = new_product_price
        item['In stock'] = new_product_stock
        break
    else:
        print('Incorrect ID. There are only IDs from 1 to ' + str(len(warehouse_list)))
        break
        
print(warehouse_list)

# Only print products which we have in our warehouse
products_we_have_in_stock = [item for item in warehouse_list if item['In stock'] != 0]
print(products_we_have_in_stock)

# Only print products that are cheeper than X dollars
max_price = int(input('Enter the MAX price of the product: '))
products_less_than_MAX_price = [item for item in warehouse_list if item['Product Price - $'] <= max_price]
print(products_less_than_MAX_price)


'''Task #4 - Task list management: Напишіть програму для керування списком завдань. 
Кожне завдання може мати назву, опис, пріоритет та статус (наприклад, "виконується", "в очікуванні", "завершено"). 
Реалізуйте можливість додавання нових завдань, оновлення статусу завдань та виведення списку завдань за пріоритетом.'''

# Basic data
list_of_tasks = [
    {
    'Task Name' : 'Digital Detox Challenge',
    'Task Description' : 'Disconnect from digital devices and enjoy a tech-free day.',
    'Priority' : 1,             # From 1 to 5, where 1 is the highest
    'Status' : 'in progress',   # "in progress", "pending", "completed"
    },
    {
    'Task Name' : 'Home Clean-Up',
    'Task Description' : 'Dedicate a day to deep clean your living space: dusting, vacuuming, mopping, and organizing.',
    'Priority' : 3,
    'Status' : 'completed',
    },
    {
    'Task Name' : 'Fitness Challenge',
    'Task Description' : 'Engage in a 30-minute workout session to boost your physical well-being.',
    'Priority' : 2,
    'Status' : 'pending',
    }
]

# Input data for a new task and add the new task to the list
task_name = input('Enter Task Name: ')
task_description = input('Enter Task Description: ')
task_priority = input('Enter Task Priority: ')
task_status = input('Enter Task Status: ')

new_item_to_add = {
'Task Name' : task_name,
'Task Description' : task_description,
'Priority' : task_priority,
'Status' : task_status,
}

list_of_tasks.append(new_item_to_add)
print(list_of_tasks)

# Editing the status of the task
task_name_to_edit = input('Choose the Name of the task you want to edit: ')
for item in list_of_tasks:
    if item['Task Name'] == task_name_to_edit:
        new_task_status = input('Enter new Task Status: ')
        item['Status'] = new_task_status
        break
else:
    print('Incorrect Task Name')
        
print(list_of_tasks)

# List of tasks by priority
tasks_by_priority = []

for priority in range(1, 6):  # Our priorities range from 1 to 5
    for task in list_of_tasks:
        if task['Priority'] == priority:
            tasks_by_priority.append(task)

print(tasks_by_priority)


'''===== Tasks from Lesson 5 ====='''


'''Task 6 - Students Jurnal: Напишіть програму для керування студентськими оцінками. Реалізуйте можливість додавання оцінок, 
видалення оцінок, обчислення середнього балу студента та виведення списку студентів з їх оцінками.'''

# Basic data
students_jurnal = {'Savchenko' : 4, 'Hunko' : 3, 'Terentiva' : 2, 'Dmytrenko' : 3,}
choose_student = input('Choose a student: ')
new_grade = int(input('Enter a grade: '))

for student in students_jurnal:
    if student == choose_student:
        students_jurnal[student] = new_grade
        break
else:
    print('There is no such student in our jurnal')

# Calculate avarage
avarage_grade = 0
for student in students_jurnal:
    avarage_grade = (avarage_grade + students_jurnal[student])

avarage_grade = avarage_grade / len(students_jurnal)
print('Avarage grade of our class: ' + str(avarage_grade))
print(students_jurnal)


'''Task 7 - Restaurant orders: Створіть програму для управління замовленнями в ресторані. 
Використовуйте список (list) для зберігання замовлень, де кожне замовлення представлене 
як кортеж (tuple) з назвою страви і ціною. Реалізуйте можливість додавання нових замовлень, 
видалення замовлень і розрахунку загальної суми замовлення.'''

full_menu = {'TOP_GUN' : 5, 'DIAMOND' : 8, 'GOLDEN_GATE' : 9, 'SECRET_WISH' : 4,}

main_clients_order = input('What would you like to order? ')
additional_clients_order = input('Would you like enything else? ')

# Every order is a tuple
order_tuple = ()
for order in full_menu:
    if order == main_clients_order:
        order_tuple += (main_clients_order,)
    elif order == additional_clients_order:
        order_tuple += (additional_clients_order,) 

if order_tuple:
    print(order_tuple)
else:
    print('There is no such dish on the menu')

# Add new item or remove one
tweaking_oreder = input('Would you like to add or remove something? ("+" - to add, "-" - to remove): ')
if tweaking_oreder == '+':
    add_new_dish = input('What would you like to add? ')
    for order in full_menu:
        if order == add_new_dish:
            order_tuple += (add_new_dish,)    
elif tweaking_oreder == '-':
    remove_from_order = input('What would you like to remove? ')
    for order in full_menu:
        if order == remove_from_order:
            order_tuple = tuple(item for item in order_tuple if item != remove_from_order)
else:
    print('Please add or remove a dish')
if order_tuple:
    print(order_tuple)

# The price of the order
price_of_the_order = 0
for dish in order_tuple:
    if dish in full_menu:
        price_of_the_order += full_menu[dish]
print(price_of_the_order)


'''Task 8 - On-line store statistics: У вас є дані по покупкам, здійсненим у вашому онлайн-магазині. 
Вам потрібно реалізувати функціонал, який надасть базову статистику по здійсненим покупкам. 
Надайте дані по наступним моментах:
- Які 3 продукти ваші клієнти купують найчастіше
- Які 3 продукти ваші клієнти купують найрідше?
- Скільки разів клієнти купували кожен з ваших продуктів?
'''

awesome_CPUs_store = {
    'INTEL Core i5 11400F' : {'Price, $' : 499, 'Stock' : 34, 'Sold' : 5,},
    'INTEL Pentium G6405' : {'Price, $' : 537, 'Stock' : 21, 'Sold' : 3,},
    'AMD Ryzen 5 3600' : {'Price, $' : 318, 'Stock' : 42, 'Sold' : 7,},
    'AMD Ryzen 7 5700X' : {'Price, $' : 819, 'Stock' : 51, 'Sold' : 11,},
    }

# продукти ваші клієнти купують найчастіше
def most_popular_product(cpu_store):
    # sold_values = []
    # for product in cpu_store:
    #     sold_values.append(cpu_store[product]['Sold'])
    # return max(sold_values)
    return max(product['Sold'] for product in cpu_store.values())

max_sold = most_popular_product(awesome_CPUs_store)
print(max_sold)

# продукти ваші клієнти купують найрідше
def most_unpopular_product(cpu_store):
    return min(product['Sold'] for product in cpu_store.values())

min_sold = most_unpopular_product(awesome_CPUs_store)
print(min_sold)

# Скільки разів клієнти купували кожен з ваших продуктів
print('Our total sales: ')
def total_sales(cpu_store):
    all_product_sales = {}
    for item, product in cpu_store.items():
        all_product_sales[item] = product['Sold']
    return all_product_sales

products_sold = total_sales(awesome_CPUs_store)
print(products_sold)
