def sort_array(source_array):
    sorting = sorted([n for n in source_array if n % 2 == 1])
    for index, num in enumerate(source_array):
        if num % 2 == 0:
            sorting.insert(index, num)
    return sorting
