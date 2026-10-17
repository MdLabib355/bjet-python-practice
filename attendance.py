att_list = [True, False, True, True, False]
amount = 0

for count in att_list:
    if count:
        amount += 1

print("Total days attended:", amount)
if amount >= 4:
    print("Great job! Your attendance is excellent.")
else:
    print("Warning: You missed too many classes this week!")