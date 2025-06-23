a = 10 
b = 3.5
print(a+b)
print(a**2)

name = "python"
print(name.upper())
# reverse the string
print(name[::-1]) 

is_ready = True
print(not is_ready)

# Lists (ordered, mutable)
categroies = ["newin", "clothing","clear"]
categroies.append("sale")
print(categroies[1])
print(categroies[-1])

# tuples(ordered, immutable)
point = (2,4)
print(point[0])

check = {"cat":"clothing", "size":23}

print(check["cat"])
print(check.get("grade","N/A"))

check["grade"]="A"

for key,vale in check.items():
    print(key,vale)

print(list(check.keys()))

s="lets check how i works"

words = s.split()
joined = "-".join(words)
print(words)
print(joined)



# with open("sample.txt","r") as f:
#     contents = f.read()


# with open("output.txt","w") as f:
#     f.write("checkng")


      
nums = [1,2,3,4]
print(list(map(lambda x: x * 2, nums)))

print(list(map(lambda x: x % 2, nums)))

names = ["a","b"]
scores=[80,5]

print(list(zip(names,scores)))

for i,value in enumerate(["a","b","c"]):
    print(i,value)

words = ["cc","re","tt"]
print(sorted(words,key=len))






