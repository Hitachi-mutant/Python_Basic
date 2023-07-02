'''Home work for the lesson 7 - Modules and standard library'''

'''Task 1 - Imports practice'''

# import my_modules

# print(my_modules.not_the_best_result(my_modules.self_assessment_tests))


# '''Task 2 - The sys module'''

# import sys

# # parameter 'r' to write the path as it is without the need for escaping '\'
# modules_folder = r'C:\Users\alexs\Python\Modules_and_Packages\inner_modules' 
# sys.path.append(modules_folder)
# print(sys.path)
# sys.path.remove(modules_folder)
# print(sys.path)


'''Task 3 - Basics, import, work with os module'''

import mymod

file_path = r'C:\Users\alexs\Python\Modules_and_Packages\file_with_text.txt'
another_file_to_count = 'nestle_employee_1.csv'
#input_file_to_count = 'Modules_and_Packages/mymod.py'   # I can run this on mymod.py, the test opens the file twice

with open(file_path) as file:
    line_count = mymod.count_lines(file)                            # 1 - count_lines(file_with_text.txt)
    char_count = mymod.count_chars(file)                            # 2 - count_chars(file_with_text.txt)

with open(another_file_to_count) as file:
    test_char_count, test_line_count = mymod.count_any_file(file)   # 3 - test(file_with_text.txt)

print("Line count:", line_count)
print("Character count:", char_count)
print("Test Line count:", test_line_count)
print("Test Character count:", test_char_count)

# Does your PYTHONPATH need to include the directory where you created mymod.py?
# No, because this file is in the same folder