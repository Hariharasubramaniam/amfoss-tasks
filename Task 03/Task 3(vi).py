lis = input("")
lis_devpo = list(map(int , input("").split()))
lis_devpo.sort()
lis_devpo2 = lis_devpo.copy()
lis_psolvpo = list(map(int , input("").split()))
lis_psolvpo.sort()
overpo = []
for i in lis_psolvpo:
    for j in lis_devpo:
        if i > j:
            overpo.append(i)
            lis_devpo.remove(j)
            break
        if i < j:
            continue
if len(overpo) < len(lis_devpo2):
    print("NO")
    exit()
else :
    power = 0
    for i in  overpo:
        power +=i
    print("YES")
    print(power)