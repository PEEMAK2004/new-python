with open ('employees.txt', 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        print(f"Name: {lines[i].strip()}")
        print(f"ID number: {lines[i+1].strip()}")
        print(f"Department: {lines[i+2].strip()}")