from datetime import datetime
def get_days_from_today(date: str) -> int:
        today = datetime.today().date()
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        return (today-target_date).days
while True:
    user_input = input("Enter the date format: YYYY-MM-DD: ")
    try:
        result = get_days_from_today(user_input)
        print(result)
        break
    except ValueError:
        print("Wrong format. Enter the date format: YYYY-MM-DD.")
