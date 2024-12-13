def my_max(*args):
    if len(args) == 0:
        raise ValueError("No arguments provided.")
    maxi = args[0]
    for item in args[1:]:
        if item > maxi:
            maxi = item

    return maxi

print(my_max(*[3, 5, 7, 2, 9]))  # Output: 9
print(my_max(*{1, 4, 8, 3}))  # Output: 8
print(my_max(*(10, 20, 5, 15)))  # Output: 20
