# enumerate - takes a list and return a pair of (index, value)  for each item in the list 
intent = ["trust", "forward","transfer","check"]
for i, label in enumerate(intent):
    print(i,label)

lable2id = {label: i for i,label in enumerate(intent)}
print(lable2id)

