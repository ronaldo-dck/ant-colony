import matplotlib.pyplot as plt
import data
from numpy.random import random

fig = plt.figure()
ax = fig.add_subplot()

x = list()
y = list()
for i in range(data.nGrafo):
    x.append(random()*data.nGrafo*100)
    y.append(random()*data.nGrafo*100)
print(x[0], y[0])
print(x[1], y[1])

plt.plot(x, y, 'ro')
for num in range(data.nGrafo):
    ax.annotate(num, xy=(x[num],y[num]), textcoords='data')

def connectpoints(p):
    x1, x2 = x[p[0]], x[p[1]]
    y1, y2 = y[p[0]], y[p[1]]
    plt.plot([x1, x2], [y1, y2], 'k-')

conns = list()
for i in range(data.nGrafo):
    for j in range(i, data.nGrafo):
        if data.dist[i][j]:
            conns.append([i, j])

for con in conns:
    connectpoints(con)

plt.axis('equal')
plt.show()
plt.savefig("teste.svg", format="svg")
