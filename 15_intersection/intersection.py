def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    # return list(set(l1) & set(l2))
    return list(set(l1).intersection(l2))
    # return [val for val in l1 if val in l2]
    # return [val for val in l1 if l2.__contains__(val)]


print(intersection([1, 2, 3], [4, 1, 3, 5, 6]))
