l1 = input("Enter a list of space separated numbers: ").split()
l = [int(x) for x in l1]

# Mean of the numbers
mean = sum(l)/len(l)

# Median of the numbers
l.sort()
if len(l) % 2 == 0:
    median1 = l[len(l)//2]
    median2 = l[len(l)//2 - 1]
    median = (median1 + median2)/2
else:
    median = l[len(l)//2]

# Mode of the numbers
mode = max(set(l), key = l.count)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
 
