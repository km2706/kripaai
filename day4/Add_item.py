temp = [11,22,33,44,55,66]
# append item to list

#  1. get length of list
length = len(temp)

print(length)

# 2. take data/item to append in list

data = input("enter data to append:")

# 3. loop through list
count= 0
for i in temp:
    print(f"{count}: {i}")
    count += 1
    temp[length] = data

# 4. print final list
print(temp)