# import re
# txt="The rain in spain by"
# x=re.search("^The . *spain$",txt)
# print(x)


#program 2
import re
txt="The rain in spain by"
x=re.search("^[A-T][c-r]*",txt)
print(x)


#program 3
import re
txt="The rain in spain by"
x=re.split("\s",txt,1)
print(x)

y=re.sub("\s","9",txt,2)
print(y)