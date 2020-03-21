import time

# Import quicksort
def quicksort(items):
    if len(items) <= 1:
        return items
    # 1. Select the last element as the pivot.
    pivot = items[-1]
    left = []
    right = []
    for i in range(len(items) - 1):
        item = items[i]
        if item < pivot:
            # 2. Move all elements smaller than the pivot to the left.
            left.append(item)
        else:
            # 3. Move all elements greater than the pivot to the right.
            right.append(item)
    #print(f"LEFT: {left}, PIVOT: {pivot}, RIGHT: {right}")
    # 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
    return quicksort(left) + [pivot] + quicksort(right)
 ###################### End of imported sort code ############################

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Solution using dictionary
# first_dict = {}
# for name in names_1:
#   first_dict[name] = 0
# for name in names_2:
#   if name in first_dict:
#     duplicates.append(name)

def find_dups(list_1, list_2):
    i = j = 0
    duplicates = []

    while i < len(list_1) and j < len(list_2):
        if list_1[i] > list_2[j]:
            j += 1
        elif list_1[i] < list_2[j]:
            i += 1
        elif list_1[i] == list_2[j]:
            duplicates.append(list_1[i])
            i += 1
            j += 1

    return duplicates



duplicates = find_dups(quicksort(names_1), quicksort(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
