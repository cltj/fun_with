def merge_sort(list):
    """
    Sort a list in a ascending order
    Returns a new sorted list
    
    Devide: Find the midpoint of the list and devide into sublist
    Conquer: Recursively sort the sublist created in the previous step
    Combine: Merge the sorted sublist created in the previous step 

    Takes overall O(kn log n) time
    """

    # Basecase/Stoping condition (Simplest condition that satisfys the end result )
    # Two possible values that exist, either a single list or an empty list
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    """
    Devide the unsorted list at midpoint into sublist
    Returns two sublists - left and right

    Takes overall O(k log n) time
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists - sorting them in the process
    Returns a new merged list

    Takes overall O(n) time (linear time)
    """        

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])



alist = [2,7,3,9,1,7,21,54,23,15,17,12,14]
l = merge_sort(alist)
print(l) 
print(verify_sorted(alist)) # Should return false = not sorted
print(verify_sorted(l)) # Should return true = sorted
