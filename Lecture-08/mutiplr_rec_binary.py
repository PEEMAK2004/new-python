import struct

num_records = int(input("Enter the number of records to create: "))
with open('records.bin', 'wb') as file:
    for i in range(num_records):
        id_num = int(input("Enter ID: "))
        name = input(f"Enter name for record : ")
        age = int(input(f"Enter age for record : "))
        gpa = float(input(f"Enter GPA for record : "))
        
        # Pack the data into binary format
        data = struct.pack('i20sif', id_num, name.encode(), age, gpa)
        file.write(data)