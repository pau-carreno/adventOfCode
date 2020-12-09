import re

first = 0
second = 1
letter = 2
password = 3

input = open('input.txt')
array = input.read().splitlines()

validPwd = 0

for pwd in array:
    pwdSplitted = re.split('-| |: ', pwd)

    pwd2Validate = pwdSplitted[password]

    firstIndex = int(pwdSplitted[first]) - 1
    secondIndex = int(pwdSplitted[second]) - 1

    firstMatch = pwd2Validate[firstIndex] == pwdSplitted[letter]
    secondMatch = pwd2Validate[secondIndex] == pwdSplitted[letter]
    if firstMatch ^ secondMatch: 
        validPwd += 1 

print(validPwd)