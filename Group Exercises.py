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
            print(number) #I print a number to make sure that we give gifts to proper customers
        elif number % 5 == 0 and number % 3 != 0:
            print("Here is a free RULER!")
            print(number)
        elif number % 3 == 0 and number % 5 == 0:
            print("Free PEN and RULER for You!")
            print(number)
        else: pass
else: print('Invalid input. The amount of customers must be an integer number')