# Modules for Work_project

def most_popular_product(cpu_store):
    # sold_values = []
    # for product in cpu_store:
    #     sold_values.append(cpu_store[product]['Sold'])
    # return max(sold_values)
    return max(product['Sold'] for product in cpu_store.values())


def most_unpopular_product(cpu_store):
    return min(product['Sold'] for product in cpu_store.values())


def adding_lessons(schedule, add_subject):
    schedule.append(add_subject)
    return schedule
    

# Modules for Lesson 7

# Task 1 - Imports practice
self_assessment_tests = {
    'Variables and primitive data types' : 90,
    'Input and a quick overview of imports' : 88,
    'Lists, tuples and sets' : 100,
    'Dictionaries and the for loop operator' : 95,
    }

def not_the_best_result(test_results):
    my_grades = {grade : test_results[grade] for grade in test_results if test_results[grade] < 100}
    return my_grades












