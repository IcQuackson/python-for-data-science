
def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None,
    return the items that are true.
    """
    if function is None:
        return [item for item in iterable if item]
    if function is not None and not callable(function):
        raise TypeError(f"{type(function).__name__} object is not callable")

    return [item for item in iterable if function(item)]


def test():
    data = (0, 1, "", "hi", None, True)

    print("Original filter(None,...):", list(filter(None, data)))
    print("ft_filter(None,...):", ft_filter(None, data))

    print("Original filter(evens):",
          list(filter(lambda n: n % 2 == 0, (1, 2, 3, 4, 5))))
    print("ft_filter(evens):",
          ft_filter(lambda n: n % 2 == 0, (1, 2, 3, 4, 5)))


def main():
    """
    main
    """
    # test()
    pass


if __name__ == "__main__":
    main()
