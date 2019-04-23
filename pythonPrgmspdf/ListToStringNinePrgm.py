def concatenate_list_data(con_list):
    result = ''
    for element in con_list:
        result += str(element)
    return result


print(concatenate_list_data([4, 8, 12, 6]))
