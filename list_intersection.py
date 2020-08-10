def list_intersection(first: list, second: list) -> list:
    intersection = []

    first = sorted(first)
    second = sorted(second)
    i = 0
    j = 0

    while ((i < len(first)) and (j < len(second))):
        while ((first[i] < second[j]) and (i < len(first) - 1)):
            i = min(i + 1, len(first) - 1)

        while ((second[j] < first[i]) and (j < len(second) - 1)):
            j = min(j + 1, len(second) - 1)

        if first[i] == second[j]:
            intersection.append(first[i])
        i = i + 1
        j = j + 1

    return intersection


def assertEqual(actual, expected):
    if (actual == expected):
        print("!!!!!OK!!!! Actual = {0}, Expected={1}".format(
            actual, expected))
    else:
        print("!!!!BAD!!!! Actual = {0}, Expected={1}".format(
            actual, expected))


def test(first, second, expected):
    assertEqual(list_intersection(first, second), expected)


def main():
    test([1], [1], [1])
    test([1, 2], [2], [2])
    test([1, 2, 3, 4, 8], [4, 2], [2, 4])
    test([1, 2, 3, 4, 8], [8, 4, 3, 2, 1], [1, 2, 3, 4, 8])
    test([1, 2, 3, 4, 8], [9], [])


main()
