import string
from random import randint
str1=string.printable
for i in range(9):
 print(str1[randint(1,100)],end="")
