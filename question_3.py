import numpy as np
import re
import operator

k = 100
beta = 0.8
M = np.zeros((int(k), int(k)))
deg = {}
with open(r"C:\Users\harsh\Documents\550 Homework MDM\homework2\data\graph.txt") as f:
    data = f.read().splitlines()
for l in data:
    e = re.split(r'\t+', l)
    i = int(e[0]) - 1
    j = int(e[1]) - 1
    if M[j, i] == 0:
        M[j, i] = 1
        deg.update({i: deg.get(i, 0) + 1})
for key in deg.keys():
    for i in range(0, int(k)):
        M[key, i] = M[key, i] / deg.get(i)

s = np.full((int(k), 1), 1 / k)
A = np.full((int(k), 1), 1.0)

for i in range(0, 30):
    s = ((1 - beta) / k) * A + beta * np.dot(M, s)

rank_dict = {}
for i in range(0, int(k)):
    rank_dict.update({i: s[i]})

dict_sort = sorted(rank_dict.items(), key=operator.itemgetter(1))

print("Top 5 is")
for i in range(int(k) - 1, int(k) - 6, -1):
    print( dict_sort[i][0] + 1, dict_sort[i][1])
print("Bottom 5 is")
for i in range(0, 5):
    print(dict_sort[i][0] + 1, dict_sort[i][1])
