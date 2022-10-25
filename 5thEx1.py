def main():
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    """list1 = [int(x) for x in input()]
    list2 = [int(x) for x in input()]"""
    list1 = set(list1)
    list2 = set(list2)
    print(list1.intersection(list2), len(list1.intersection(list2)))
    print(list1.union(list2) - list1.intersection(list2), len(list1.union(list2) - list1.intersection(list2)))
    print(list1-list2, len(list1-list2))
    print(list2-list1, len(list2-list1))

if __name__ == "__main__":
    main()