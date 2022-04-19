def random_list(n):
    """create a random list of integers"""
    import random
    lst = []
    for i in range(n):
        lst.append(random.randint(1, 10))
    return lst


def sort_list(lst):
    """sort a list of integers"""
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def count_x(lst, x):
    """conut the number of times x appears in lst"""
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count


def search_list(x):
    """search a list of integers for x"""
    lst = random_list(10)
    print(count_x(lst, x))


ranList = random_list(10)
print(ranList)
sortLst = sort_list(ranList)
print(sortLst)
searchLst = search_list(5)
print(searchLst)

