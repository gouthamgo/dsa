my_variale = 10
another_variable='python'

is_active = True

def check():
    '''this is a function'''
    print('Testing to pass the argument')

def getOutput(num):
    return my_variale * num

check()
sum = getOutput(2)
print(f"The check is : {sum}")


garments= ["petite", "swimwear","checks"]


catgeories={
    "newin": "Latest",
    "total": 300,
    "locale":"AU"
}


for key in catgeories:
    print(f"Key : {key}")


for value in catgeories.values():
    print(f"Vlaue: {value}")

for key,value in catgeories.items():
    print(f"{key} : {value}")

for item in garments:
    print(f"{item}")







