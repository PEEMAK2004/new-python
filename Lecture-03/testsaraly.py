'''workhour_employee = int(input("Enter your work hours: "))
hourly_rate = float(input("Enter your hourly rate: "))
if workhour_employee > 40:
    overtime_hours = workhour_employee - 40
    overtime_pay = overtime_hours * hourly_rate * 1.5
    regular_pay = 40 * hourly_rate
    total_pay = regular_pay + overtime_pay
    print(f"Your total pay is: ${total_pay:.2f}")
else:
    total_pay = workhour_employee * hourly_rate
    print(f"Your total pay is: ${total_pay:.2f}") '''


'''workhour_employee = int(input("Enter you work hour : "))
hourly_rate = float(input("Enter your hourly rate: "))
    if workhour_employee > 60:
        overtime_hours = workhour_employee - 60
        overtime_pay = overtime_hours * hourly_rate * 1.75
        normalpay = 60* hourly_rate
        total_pay = normalpay + overtime_pay
        print(f"You Salary is : ${total_pay:.2f}")
    else:
        total_pay = workhour_employee * hourly_rate
        print(f"You Salary is : ${total_pay:.2f}")

# Get input from the user
work_hours = int(input("Enter your work hours: "))
hourly_rate = float(input("Enter your hourly rate: $"))

# Calculate salary
'if work_hours > 60:
    normal_hours = 60
    overtime_hours = work_hours - normal_hours

    normal_pay = normal_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.50

    total_pay = normal_pay + overtime_pay
else:
    total_pay = work_hours * hourly_rate

# Display result
print(f"Your salary is: ${total_pay:.2f}")

work_hours = int(input("Enter your work hours: "))
hourly_rate = float(input("Enter your hourly rate: $"))

work_hours <= 40:
    print(work_hours * hourly_rate)

    print((40 * hourly_rate) + ((work_hours - 40) * 1.5 * hourly_rate))'''