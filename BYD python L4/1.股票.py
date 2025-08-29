prices=[10,12,15,15,16,18,20,19]

#找到三天连续上涨的日期

#1.
for i in [0,1,2,3,4,5,6,7,8]:
    if i>5:
        continue
    if prices[i]<prices[i+1]<prices[i+2]:
        print(i,i+1,i+2)

#2.
for i in [0,1,2,3,4,5]:
    if prices[i]<prices[i+1]<prices[i+2]:
        print(i,i+1,i+2)

#3.len
i=0
while i<len(prices)-2:
    if prices[i]<prices[i+1]<prices[i+2]:
        print(i,i+1,i+2)
    i=i+1

#4.
i=0
while i<=5:
    if prices[i]<prices[i+1]<prices[i+2]:
        print(i,i+1,i+2)
    i=i+1


