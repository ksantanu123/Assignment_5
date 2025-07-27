list =[]
x = []
for i in range(1,11):
    list.append(i)
print("Original list : ",list)

for i in range(0,5):
   x.append(list[i])

print(f"First five elements: {list[0:5]}")

print(f"Reversed Extracted elements: {x[::-1]}")
