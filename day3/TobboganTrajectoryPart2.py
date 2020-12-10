import numpy as np

input = open('input.txt')
text = input.readlines()
text[:] = [line.replace('\n', '') for line in text]

colSize = len(text[0])
trees = [0, 0, 0, 0, 0]
slopes = [1, 3, 5, 7, 1]
index = [0, 0, 0, 0, 0]

for lineIndex, line in enumerate(text):
    for i in range(len(index)-1):
        if (line[index[i] % colSize] == '#'):
            trees[i] += 1
        index[i] += slopes[i]

    if (lineIndex % 2 == 0):
        if (line[index[-1] % colSize] == '#'):
            trees[-1] += 1
        index[-1] += slopes[-1]

print(np.prod(trees))
