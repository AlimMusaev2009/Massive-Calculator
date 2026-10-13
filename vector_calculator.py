import numpy as np

v1 = []
v2 = []
output = []

s = str(input("значения первого вектора (через зарятую):"))
v1 += s.split(',')
for i in range(len(v1)):
    output += int(v1[i])
v1 = output
output = []
s = str(input("значения первого вектора (через зарятую):"))
v2 += s.split(',')
for i in range(len(v2)):
    output += int(v2[i])
v2 = output
output = []
if len(v1) != len(v2) or len(v1) == 4:
    print("ОНИ ДОЛЖНЫ БЫТЬ ОДИНАКОВЫЕ")

v1 = np.array(v1)
v2 = np.array(v2)

print("Сумма:", v1 + v2)
print("Умножение", v1 @ v2)
print("Совпадение", np.cross(v1, v2))
