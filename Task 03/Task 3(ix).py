n = int(input(""))
lis_mass = input("").split()
lis_mass = list(map(int , lis_mass))
lis_mass.sort()
uniq = list(set(lis_mass))
n_duplicates = []
for i in uniq:
    n_duplicates.append(lis_mass.count(i))
tmp = n_duplicates.sort()
print(str(n_duplicates[len(n_duplicates) - 1]) + " " + str(len(n_duplicates)) )