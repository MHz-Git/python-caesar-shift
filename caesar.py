#-*-coding:utf8;-*-
#qpy:2
#qpy:console
a = raw_input('input: ')
b = raw_input('shift: ')
c = int(b)
l = list(a)
import string
alp = string.ascii_lowercase
let = list(alp+alp)
num = range(1,5)
code = dict(zip(let, num))
code2 = dict(zip(num, let))
for i in l:
    if i == " ":
        print " "
    else:
        k = code[i]
        s = code2[k+c]
        print s
