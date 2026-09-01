import struct 
record_format = 'i20sif'  # Define the format for the record
record_size = struct.calcsize(record_format)  # Calculate the size of the record
with open('records.bin', 'rb') as file:

    file.seek(record_size)  

    data = file.read(record_size)
    record = struct.unpack(record_format, data)
    record = (record[0], record[1].decode('utf-8').rstrip('\x00'), record[2], record[3])
    print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]}")