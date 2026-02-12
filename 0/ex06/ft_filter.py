
def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None,
    return the items that are true.
    """
    if function is None:
        return [item for item in iterable if function(item)]

    return [item for item in iterable if function(item)]


def test():
    """
    Tests ft_filter() and compares with original filter()
    """
    print("Original filter(): " +
          str(list(filter(lambda n: n % 2 == 0, (1, 2, 3, 4, 5)))))
    print("ft_filter(): " +
          str(ft_filter(lambda n: n % 2 == 0, (1, 2, 3, 4, 5))))


def main():
    """
    main
    """
    # test()
    pass


if __name__ == "__main__":
    main()
