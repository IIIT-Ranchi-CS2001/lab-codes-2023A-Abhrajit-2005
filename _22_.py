l1 = [x for x in input("Enter the customer names (space separated): ").split()]
l2 = [int(x) for x in input("Enter the customer ids (space separated): ").split()]
l3 = [int(x) for x in input("Enter the shopping points (space separated): ").split()]
l4 = []
for i in range(0, len(l1)):
    l4.append((l1[i],l2[i],l3[i]))
print(l4)
l5 = list(zip(l1,l2,l3))
print(l5)
l6 = sorted(l5)
print(l6)
