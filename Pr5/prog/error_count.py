from math import sqrt
import matplotlib.pyplot as plt

file = open("output.txt", "r")

xyz = []

equ = []

for line in file:
    s = line.strip()
    if (s.startswith("(x,y,z)")):
        numbers = s.split("=")[1].strip()[1:-1].split(",")
        numbers = tuple(map(lambda s: float(s.strip()), numbers))
        xyz.append(numbers)

    if (s.startswith("RA")):
        ra = equ[5:17]
        equ.append(s)

equ.pop(0)
xyz.pop(0)


def diff(a, b):
    return (
        a[0] - b[0],
        a[1] - b[1],
        a[2] - b[2],
    )


x = []
y = []
z = []

for i in range(30):
    before = xyz[i*2]
    after = xyz[i*2+1]
    
    diffs = diff(before, after)
    x.append(diffs[0])
    y.append(diffs[1])
    z.append(diffs[2])


plt.plot(x, label='x')
plt.plot(y, label='y')
plt.plot(z, label='z')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid(True, "both")

plt.show()

