#count list using recursion
#count_recursively([1, 2, 3]) -> 3

def count_recursively(lst):

    if len(lst) == 0:
        return 0

    return 1 + count_recursively(lst[1:])

print(count_recursively([1,2,3,4]))