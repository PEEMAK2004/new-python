animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]
first_dog_index = animals.index("dog")
print(f"Index of 'dog': {first_dog_index}")

# Using index () to find the second occurrence of "dog"
second_dog_index = animals.index("dog", first_dog_index + 1)
print(f"The second occurrence of 'dog' is at index: {second_dog_index}")
# Output: The second occurrence of 'dog' is at index: 4

