def activity_selection(start, finish):
    n = len(start)

    # sort both lists based on finish[]
    start, finish = zip(*sorted(zip(start, finish), key=lambda x: x[1]))
    start = list(start)
    finish = list(finish)

    print("Sorted Start :", start)
    print("Sorted Finish:", finish)

    # First activity is always selected
    print("Selected indices:")
    j = 0
    print(j)

    for i in range(1, n):
        if start[i] >= finish[j]:
            print(i)
            j = i
