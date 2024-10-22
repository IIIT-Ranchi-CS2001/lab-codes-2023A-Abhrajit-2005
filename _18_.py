singers = {"Santosh", "Arpit", "Ayansh", "Person1", "Person2"}
dancers = {"Simar","Ekam","Kartikey", "Person1", "Person2"}

# Set operations to generate all artist of the same class
print(singers.intersection(dancers))

# Set operations to generate allrounders of the class
print(singers.union(dancers))

# Set operations to generate dancers but not singers
print(dancers.difference(singers))

# Set operations to generate singers but not dancers
print(singers.difference(dancers))

# Set operations to generate dancers but not singers cum singers but not dancers
print((dancers.difference(singers)).union(singers.difference(dancers)))