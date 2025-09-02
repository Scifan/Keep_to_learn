trs=[200,-50,300,-100,50,-20,100]

balances=sum(trs)

incomes_list=[]
expense_list=[]
for tr in trs:
    if tr>=0:
        incomes_list.append(tr)
    else:
        expense_list.append(tr)
print(balances)
print(incomes_list)
print(expense_list)
print(sorted(incomes_list,reverse=True))
print(sorted(expense_list))