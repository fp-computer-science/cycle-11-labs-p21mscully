# Author MRS 12/16/20

def double_stuff(lst):
    for index, value in enumerate(lst):
        lst[index] = 2 * value
    return lst


print(double_stuff([1, 2, 3, 4]) == [2, 4, 6, 8])