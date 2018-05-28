def swap_max_min(lst):
    index_min = lst.index(min(lst))
    index_max = lst.index(max(lst))
    temp_min = lst[index_min]
    temp_max = lst[index_max]
    lst[index_min] = temp_max
    lst[index_max] = temp_min
    print(lst)
    return lst # for testing


