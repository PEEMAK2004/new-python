x = 10
y = 20
z = 30

if x < y and y < z:
    print("x is less than y and y is less than z")
    #true and true = true
if x < y or y > z:
    print("x is less than y or y is greater than z")
    #true or false = true
if not (x > y):
    print("x is not greater than y")
    #true = opposite value = false