def replace_value(values, index, new_value):
    if 0 <= index < len(values):
        values[index] = new_value
    return None

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    smallest = min(values)
    largest = max(values)
    total_sum = sum(values)
    return (smallest, largest, total_sum)

days = int(input("Enter the number of days: "))

original = []
for i in range(days):
    cooking_time = int(input("Enter cooking time in minutes: "))
    original.append(cooking_time)

updated = original[:]

index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new cooking time: "))
replace_value(updated, index, new_value)

target = int(input("Enter the cooking time to search for: "))

first_index = find_first(updated, target)
matching_values = updated.count(target)

minimum, maximum, total = summarize(updated)
sorted_list = sorted(updated)

print()
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum cooking time: {minimum} minutes")
print(f"Maximum cooking time: {maximum} minutes")
print(f"Total cooking time: {total} minutes")

if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {matching_values}")