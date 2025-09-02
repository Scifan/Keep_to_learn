message="明天要是开学天气不好，我就使用暴力应对！"
sens=input("请输入敏感词: ")
x=message.find(sens)
new_message=message[:x]+len(sens)*"*"+message[x+len(sens):]
#new_message=message.replace(sens,"*"*len(sens))
print(new_message)