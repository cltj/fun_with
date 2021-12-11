lst=[]
def linear_search(lst, target):
    """
    Returns the index position of target if found, else returns None
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers,6)
verify(result)