fruits_with_duplicates = ["apple", "banana", "apple", "banana", "apple" , "kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"fruits after removing duplicates: {fruits_with_duplicates}")