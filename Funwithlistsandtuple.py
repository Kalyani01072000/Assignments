tuple1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

List2 =[]
List3 =[]

for t in tuple1:
    List2.append(t[1],)

List2.sort()

for l in List2:
    for q in tuple1:
        if l == int(q[1],):
            List3.append(q)

print(List3)