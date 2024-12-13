l1 = ["CS-2001", "CS-2003", "MA-2001", "CS-2005"]
l2 = ["Python", "COA", "Mathematics", "Algorithm"]
l = []
for i in range(len(l1)):
    l.append(l1[i] + ":" + l2[i])
print(l)