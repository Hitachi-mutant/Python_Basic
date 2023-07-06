'''Home work for the lesson 6'''

'''Task 1 - Unique words as keys and the number of occurrences as values'''
inputed_sentence = input('Enter a random sentence: ')
list_of_words_from_string = inputed_sentence.split(' ')
dict_with_words_and_occurrences = {}

for item in list_of_words_from_string:
    dict_with_words_and_occurrences[item] = dict_with_words_and_occurrences.get(item, 0) + 1

# for item in list_of_words_from_string:       # This method also works
#     if item not in dict_with_words_and_occurrences:
#         dict_with_words_and_occurrences[item] = list_of_words_from_string.count(item)

print(dict_with_words_and_occurrences)


'''Task 2 - Total price of the stock'''

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

for fruit in stock:
    total_price_of_stock = float(prices[fruit]) * float(stock[fruit])
    print(total_price_of_stock)


'''Task 3 - List comprehension exercise'''

numbers = [1, 2, 3, 4, 5]
# list_of_numbers_and_squared_numbers = [] # Here I used cycles
# for num1 in numbers:
#     num2 = num1 **2
#     tuple_of_numbers = ()
#     tuple_of_numbers += (num1,)
#     tuple_of_numbers += (num2,)
#     list_of_numbers_and_squared_numbers.append(tuple_of_numbers)
    
list_of_numbers_and_squared_numbers = [(num1, num1 ** 2) for num1 in numbers] # Here is a list comprehension 
print(list_of_numbers_and_squared_numbers)


'''Task 4 - Days of the week list'''

week_days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# week_days_dict, week_days_dict_revert = {}, {}      # Doing in a simple way
# for day in week_days_list:
#     week_days_dict[week_days_list.index(day) + 1] = day
#     week_days_dict_revert[day] = week_days_list.index(day) + 1

week_days_dict = {index + 1: day for index, day in enumerate(week_days_list)}     # Doing properly
week_days_dict_revert = {day: index + 1 for index, day in enumerate(week_days_list)}

print(week_days_dict)
print('\n')
print(week_days_dict_revert)