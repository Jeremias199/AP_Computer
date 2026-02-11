months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def Get_Month(month_num):
    for i in range(len(months)):
        if i == month_num - 1:
            return months[i]
    return "Invalid number. Enter a number between 1-12"

User_Month = int(input("Type a month number:")) ; Result = Get_Month(User_Month)

print(Result)

