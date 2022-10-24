a = []
print("nhap mang gom 5 so")
for i in range(5):
    a.append(int(input()))

b = max(a)
c = min(a)
t_min = []
t_max = []

for i in range(5):
    if b != a[i]:
        t_min.append(a[i])
    if a[i] != c:
        t_max.append(a[i])

for i in range(4):
    if i == 3:
        print(str(t_min[i]) + "= " + str(sum(t_min)))
    else:
        print(str(t_min[i]) + " + ", end=' ')
for i in range(4):
    if i == 3:
        print(str(t_max[i]) + "= " + str(sum(t_max)))
    else:
        print(str(t_max[i]) + " + ", end=' ')
