from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    respond = {}
    for user in users:
        transformed_date = datetime(
            date.today().year, user["birthday"].month, user["birthday"].day).date()
        if transformed_date < date.today():
            transformed_date = datetime(
                date.today().year + 1, user["birthday"].month, user["birthday"].day).date()
        if transformed_date >= date.today():
            if transformed_date - date.today() <= timedelta(days=6):
                if transformed_date.weekday() >= 5:
                    if "Monday" in respond:
                        respond["Monday"].append(user["name"])
                    else:
                        respond["Monday"] = [user["name"]]
                else:
                    if f"{transformed_date:%A}" in respond:
                        respond[f"{transformed_date:%A}"].append(user["name"])
                    else:
                        respond[f"{transformed_date:%A}"] = [user["name"]]
    return respond


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
