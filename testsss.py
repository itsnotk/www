lst = [23, 94, 24, 49, 85, 29, 47, 90]

for i in range(len(lst)):
    for j in range((len(lst)-1)):
        if lst[j] > lst[j+1]:
            lst[j], ist[j+1] = lst[j+1], lst[j]

print(lst)
