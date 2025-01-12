T1 = 1340709143539
T2 = 1509243312196
T3 = 1705974408753
T4 = 2426049140989
c = 1
m = 1
while True:
    m += 1
    for i in range(100):
        temp = T1
        for b in range(i):
            T1 = (T1 + temp)%m
    if T1 == T2:
        print(m,i)
    