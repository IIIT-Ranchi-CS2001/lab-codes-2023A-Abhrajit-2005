def my_sort(l, key):
    def get_key(item):
        return item[key]
    n = len(l)
    for i in range(n):
        for j in range(0, n - i - 1):
            if get_key(l[j]) > get_key(l[j + 1]):
                l[j], l[j + 1] = l[j + 1], l[j]

    return l
def my_zip(name, id, points, strct=True):
    if strct:
        if not (len(name) == len(id) == len(points)):
            raise ValueError("All lists must be of equal length in strict mode.")
    mini = min(len(name), len(id), len(points))
    zipped = [(name[i], id[i], points[i]) for i in range(mini)]
    
    return zipped
l1 = [x for x in input("Enter the customer names (space separated): ").split()]
l2 = [int(x) for x in input("Enter the customer ids (space separated): ").split()]
l3 = [int(x) for x in input("Enter the shopping points (space separated): ").split()]
l4 = my_zip(l1,l2,l3,strct=True)
print(my_sort(l4,0))
print(my_sort(l4,1))
print(my_sort(l4,2))
