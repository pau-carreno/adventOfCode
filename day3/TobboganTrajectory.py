import numpy as np

input = open('input.txt')
text = input.readlines()
text[:] = [line.replace('\n','') for line in text]

colSize = len(text[0])
trees = 0
index = 0

for line in text:
    if (line[index%colSize] == '#'):
        trees +=1
    index += 3

print (trees)