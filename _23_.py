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
print(my_zip(l1,l2,l3,strct=False))
print(my_zip(l1,l2,l3,strct=True))

