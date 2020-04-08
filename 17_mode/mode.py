import math


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dict_my = {num: nums.count(num) for num in nums}
    print(dict_my, 'my dict')
    max_value = max(dict_my.values())
    print(max_value, 'max value')
    # now we need to see at which index the highest value is at

    for (num, freq) in dict_my.items():
        if freq == max_value:
            print('found number with max freq', num)
            return num


print(mode([1, 2, 3, 4, 4, 5, 5, 5, 3, 2, 1, 22, 2, 99, 1, 1, 1, 1]))
