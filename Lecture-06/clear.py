nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in nested_list:
    sublist.clear()
print(f"Nested list after clearing: {nested_list}")
# Output: Nested list after clearing: [[], [], []]
#อยากเคลียร์ที่ละช่อง