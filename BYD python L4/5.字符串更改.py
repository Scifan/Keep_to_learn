str="I love Python "
upper_st=str.upper()
lower_st=str.lower()
capitalize_st=str.capitalize()
title_st=str.title()
print(upper_st)
print(lower_st)
print(capitalize_st)
print(title_st)

str="I love Python "
str.upper()
print(str)

strip_st=str.strip()
lstrip_st=str.lstrip()
rstrip_st=str.rstrip()
print(strip_st)
print(lstrip_st+"Oh!")
print(rstrip_st+"Oh!")

sentence="I love Python"
sen=sentence.replace("Python","Java")
print(sen)

data="apple,banana,cherry"
data.split(",")
print(data)