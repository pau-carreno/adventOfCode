input = open('input.txt')
array = input.read().splitlines()

found = False
count = 0

for i in range(len(array)): 
    tmp = int(array [i])
    for j in range(i, len(array)):
        tmp2 = int(array[j])
        if (tmp + tmp2 == 2020):
            print(tmp * tmp2)
            found = True
        if found: break
    if found: break