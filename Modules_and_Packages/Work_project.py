'''On-line store statistics: У вас є дані по покупкам, здійсненим у вашому онлайн-магазині. 
Вам потрібно реалізувати функціонал, який надасть базову статистику по здійсненим покупкам. 
Надайте дані по наступним моментах:
- Які 3 продукти ваші клієнти купують найчастіше
- Які 3 продукти ваші клієнти купують найрідше?
- Скільки разів клієнти купували кожен з ваших продуктів?
'''

import my_modules
import inner_modules.additional_modules
#from  my_modules import most_unpopular_product # Just to demonstrate another way
#from inner_modules.additional_modules import total_sales   # Just to demonstrate another way


awesome_CPUs_store = {
    'INTEL Core i5 11400F' : {'Price, $' : 499, 'Stock' : 34, 'Sold' : 5,},
    'INTEL Pentium G6405' : {'Price, $' : 537, 'Stock' : 21, 'Sold' : 3,},
    'AMD Ryzen 5 3600' : {'Price, $' : 318, 'Stock' : 42, 'Sold' : 7,},
    'AMD Ryzen 7 5700X' : {'Price, $' : 819, 'Stock' : 51, 'Sold' : 11,},
    }


# продукти ваші клієнти купують найчастіше
max_sold = my_modules.most_popular_product(awesome_CPUs_store)
print(max_sold)

# продукти ваші клієнти купують найрідше
min_sold = my_modules.most_unpopular_product(awesome_CPUs_store)
print(min_sold)

# Скільки разів клієнти купували кожен з ваших продуктів
products_sold = inner_modules.additional_modules.total_sales(awesome_CPUs_store)
print(products_sold)


'''Напишіть програму для керування розкладом занять студентів. 
Використовуйте список (list) для зберігання інформації про заняття, 
де кожне заняття представлене як кортеж (tuple) з назвою предмету і 
часом проведення (це може бути як і день, так і конкретна година - 
вибирайте як вам зручніше). Реалізуйте можливість додавання нових занять, 
видалення занять і виведення розкладу занять за допомогою циклу for.'''

student_schedule = [('Chemistry', 'Monday', '11-00'), ('Physics', 'Tuesday', '9-00')]

# Adding lesson
name_of_discipline_to_add = ('Mathematics', 'Friday', '10-00')
print(my_modules.adding_lessons(student_schedule, name_of_discipline_to_add))

# Removing lesson
name_of_discipline_to_remove = 'Chemistry'

print(inner_modules.additional_modules.removing_lessons(student_schedule, name_of_discipline_to_remove))

# Show a full schedule
print([f'On {lesson[1]} at {lesson[2]} - {lesson[0]}' for lesson in student_schedule])
