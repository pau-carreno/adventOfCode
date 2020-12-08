import re

lowest = 0
highest = 1
letter = 2
password = 3

input = open('input.txt')
array = input.read().splitlines()

validPwd = 0

for pwd in array:
    pwdSplitted = re.split('-| |: ', pwd)
    appreanances = pwdSplitted[password].count(pwdSplitted[letter])
    if appreanances >= int(pwdSplitted[lowest]) and appreanances <= int(pwdSplitted[highest]):
        validPwd += 1

print(validPwd)