def print_all(*args):
    for index, arg in enumerate(args):
        print(f"Argument {index + 1}: {arg}")

# Example usage
print_all("Python", 42, 3.14, True, [1, 2, 3], {"key": "value"})
