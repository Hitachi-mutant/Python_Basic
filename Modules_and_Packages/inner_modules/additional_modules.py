print('Our total sales: ')
def total_sales(cpu_store):
    all_product_sales = {}
    for item, product in cpu_store.items():
        all_product_sales[item] = product['Sold']
    return all_product_sales


def removing_lessons(schedule, remove_subject):
    index = 0
    for item in schedule:
        if item[0] == remove_subject:
            schedule.pop(index)
        else:
            index += 1
    return schedule