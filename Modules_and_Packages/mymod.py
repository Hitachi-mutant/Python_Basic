# count_lines(file_with_text.txt)
def count_lines(file_to_count):
    file_to_count.seek(0)
    result_count_lines = len(file_to_count.readlines())
    return result_count_lines

# count_chars(file_with_text.txt)
def count_chars(file_to_count):
    file_to_count.seek(0)
    result_count_characters = len(file_to_count.read())
    return result_count_characters

# test(file_with_text.txt)
def count_any_file(count_lines_and_chars):
    count_lines_and_chars.seek(0)
    result_char_count = count_chars(count_lines_and_chars)
    result_line_count = count_lines(count_lines_and_chars)
    return result_char_count, result_line_count