s1 = input("Enter the first point(space-separated): ")
l1 = [int(x) for x in s1.split()]
s2 = input("Enter the second point(space-separated): ")
l2 = [int(x) for x in s2.split()]
slope = (l2[1]-l1[1])/(l2[0]-l1[0])
constant = l1[1]-slope*l1[0]
if(constant>0):
    s = f"y = {slope}*x + {constant}"
else:
    s = f"y = {slope}*x + {constant}"
print(s)