score1 = int(input("Enter your first score: "))
score2 = int(input("Enter your first score: "))
score3 = int(input("Enter your first score: "))

average = ((score1 + score2 + score3) / 3)

print("the areage of the three scores is: ", format(average, ".2f"))

if average >= 95:
    print("congaratulation")
elif average >= 70:
    print("still going")
else: print("dumbass")
