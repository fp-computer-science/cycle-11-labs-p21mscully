# Author MRS 12/16/20

total = 0
while True:
    user_number = input("Enter a number:")
    if user_number == "-1":
        break
    else:
        total += int(user_number)


print("The sum of all the numbers enter is {0}".format(total))