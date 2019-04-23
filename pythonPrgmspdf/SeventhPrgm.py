def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False


print(is_group_member([12, 6, 1, 3], 6))
print(is_group_member([5, 8, 3], -1))
