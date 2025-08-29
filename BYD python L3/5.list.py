###
numbers=[1,2,3,4,5,6,7,8,9]
print(numbers,type(numbers))

###
list=["a","b","c",1,2,3]
print(list)

###
objects=["iPhone","iPad","Mac","Windows","Airpods"]
the_first_object=objects[-5]
print(the_first_object)

###
objects=["iPhone","iPad","Mac","Windows","Airpods"]
asub_objects=objects[1:3]
bsub_objects=objects[ :3]
csub_objects=objects[-2:]
print(asub_objects)
print(bsub_objects)
print(csub_objects)

###
my_list=["a","b","c",1,2,3.8,"abc",[1,2,3]]
print(my_list)
my_list.append('d')
my_list.insert(1,99)
print(my_list)
#extend→头接尾拼接两个列表
#append 列表进入另一个列表就是把被加入列表当作一个元素加入另一个列表的末尾
#还有好多删除修改查找的函数