def max_list_iter(int_list):  # must use iteration not recursion
    if int_list is None:
        raise ValueError
    if not int_list:
        return None
    big = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > big:
            big = int_list[i]
    return big
    # """finds the max of a list of numbers and returns the value (not the index)
    # If int_list is empty, returns None. If list is None, raises ValueError"""
    pass


def reverse_rec(int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    my_list = []
    if len(int_list) == 0:
        return my_list
    my_list.append(int_list[-1])
    my_list += reverse_rec(int_list[:-1])
    return my_list
    ##"""recursively reverses a list of numbers and returns the reversed list
    ##If list is None, raises ValueError"""
    pass


def bin_search(target, low, high, int_list):  # must use recursion
    if int_list is None:
        raise ValueError
    if not int_list:
        return None
    assert(low < high), 'Low is not greater than high'
    assert(0 <= low), 'Low not in range'
    assert(high <= len(int_list)), 'high cannot be greater than length of list'
    if target > int_list[high] or target < int_list[low]:
        return None
    if int_list[low] == target:
        return low
    if int_list[high] == target:
        return high
    if high >= 1:
        mid = 1 + (high - 1) // 2
        if int_list[mid] == target:
            return mid
        elif int_list[mid] > target:
            return bin_search(target, low, mid-1, int_list)
        else:
            return bin_search(target, mid+1, high, int_list)




    ## """searches for target in int_list[low..high] and returns index if found
    ##If target is not found returns None. If list is None, raises ValueError """
