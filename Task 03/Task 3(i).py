lis = input("").split()
n_girl = int(lis[0])
r_Sande = int(lis[1])
times = 0
win_times = 0
times2 = 0
number = []
while n_girl % 2 == 0:
    times += 1
    n_girl /= 2
for i in range(1 , r_Sande + 1):
    times2 = 0
    j = i
    while j % 2 == 0:
        j /= 2
        times2 += 1
    if times2 < times:
        win_times += 1
        number.append(int(i))

print(win_times)
print(' '.join(list(map(str , number))))