def week_days(day):
    match day:
        case 1:
            return "Saturday"
        case 2:
            return "Sunday"
        case 3:
            return "Monday"
        case 4:
            return "Tuesday"
        case 5:
            return "Wednesday"
        case 6:
            return "Thursday"
        case 7:
            return "Friday"
        case _:
            return "Thats Not A Valid Day :  "
def get_type(day_name):
    match day_name:
            case "Thursday" | "Friday":
                return "WeekEnd"
            case "Saturday" | "Sunday" | "Monday" | "Tuesday" | "Wednesday":
                return "WeekDay"
            case _:
                return "Thats Not A Valid Day :  "

def week_calc():
    while True:
        try:
            user_input = input("Enter A Number To Know What day Of The Weeek It Is : ")
            day = int(user_input)
            result = week_days(day)
            type_result = get_type(result)
            print(f"Day {user_input} Is : {result}\nAnd Its {type_result}")
        except ValueError:
            print("Thats Not A Number..!")
week_calc()