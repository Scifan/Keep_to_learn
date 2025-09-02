money=int(input())
if money <= 5000:
    give_money=0
if money >= 5000 and money <= 10000:
    give_money=(money-5000)*0.03
if money >= 10000 and money <= 20000:
    give_money=(money-10000)*0.1+5000*0.03
if money >= 20000:
    give_money=(money-20000)*0.2+5000*0.03+10000*0.1
print(give_money)