score1 = int(input("Enter the score for test 1: "))
score2 = int(input("Enter the score for test 2: "))
score3 = int(input("Enter the score for test 3: "))

average = (score1 + score2 + score3) / 3

print("The average of the three scores is: ", format(average, ".2f"))

if average >= 95 and score2 >= 95 and score3 >= 95:
    print("Congratulations!")
elif average >= 70:
    print("Still going!")
else:
    print("Dumbass!")