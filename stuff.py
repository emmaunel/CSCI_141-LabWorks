def array_diff(a, b):
    new_b = []
    temp_a = a
    if b == []:
        print(a)
    else:
        for i in b:
            for j in a:
                if j == i:
                    pass
                    # a.pop(i)
                    # temp_a = a
                else:
                    new_b.append(i)

    # print(temp_a)
    print(new_b)


print("Basic Tests")
array_diff([19, -11, -4, -12, 7, 0], [-20, -3, 6, 2, -14, 0, 3, 5])
# array_diff([1,2,2], [1])
# array_diff([1,2,2], [2])
# array_diff([1,2,2], [])
# # array_diff([], [1,2])