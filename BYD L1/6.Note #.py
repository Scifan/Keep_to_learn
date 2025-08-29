#输入
age=int(input("Enter your age: "))
#预判断
if age<=0:
    print("The age is less than zero,please try again.")
else:
    #处理
    years = 35 - age
    print("Your left years: ", years)
    #判断
    if years >= 0:
        print("Congratulations, you have time left to work!")
    else:
        print("Sorry, you have no time left to work!")

