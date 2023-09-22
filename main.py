t1 = (1, 2)
print(type(t1))

l1 = ["maruthi", "mahendira", "aadi", "beny", "honda"]
print(l1)

for i in l1:
    if i == "honda":
        print(i.upper())
    else:
        print(i.title())

dict1 = {}
dict2 = {}
print(dict2.get("name", "invalid keyword"))