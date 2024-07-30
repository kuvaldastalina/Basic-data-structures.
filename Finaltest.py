grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


sorted_students = sorted(students)
print(sorted_students)
a = len(grades)
s = 0

gurnal = []


for n in range(len(grades)):
    b = len(grades[n])
    s = 0

    for i in range(b):
        s += grades[n][i]

    t = s/b
    gurnal.append(t)
print(gurnal)

d = {}
for i in range(len(gurnal)):
    d[sorted_students[i]] = gurnal[i]

print(d)


