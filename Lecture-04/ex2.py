num_row = int(input("็How many rows: "))

for i in range(1, 101):
    print(f"{i:>3}", end=" ")
    if i % num_row == 0:
        print()
    
