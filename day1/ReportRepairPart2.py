input = open('input.txt')
array = input.read().splitlines()

found = False
count = 0

for i in range(len(array)):
    tmp = int(array[i])
    for j in range(i, len(array)):
        tmp2 = int(array[j])
        for k in range(j, len(array)):
            tmp3 = int(array[k])
            if (tmp + tmp2 + tmp3 == 2020):
                print(tmp * tmp2 * tmp3)