def example_a_plus_mode():
    # Open the file for reading and writing (appending to the end)
    with open('example_a+.txt', 'a+') as file:
        # Write some content to the file
        file.seek(0)

        content = file.read()
        print("Current content of the file:")
        print(content)

        file.write("Appending a new line added to the file.\n")

        file.seek(0)
        updated_content = file.read()
        print("\nUpdated content of the file:")
        print(updated_content)

example_a_plus_mode()
