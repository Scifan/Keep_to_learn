EN_CN_dictionary={
    "apple":"苹果",
    "banana":"香蕉",
    "grape":"葡萄"
}
print(EN_CN_dictionary["apple"])
print(EN_CN_dictionary.get("apple"))
print(EN_CN_dictionary.get("peach"))
#print(EN_CN_dictionary["peach"])没有的时候会报错，上面的一行不会↑

EN_CN_dictionary["apple"]="苹果儿"
print(EN_CN_dictionary)

EN_CN_dictionary["peach"]="桃子"
print(EN_CN_dictionary)

print(EN_CN_dictionary.keys())
print(EN_CN_dictionary.values())

print(EN_CN_dictionary.items())
for item in EN_CN_dictionary.items():
    print(item)
    print(type(EN_CN_dictionary.items()))
    print(type(item))

EN_CN_dictionary_pro={
    'apple'='大红苹果'
    }