def buy_ticket_basic(day_in_week: int, hour: int, zigma: bool) -> int:
    price = 0
    if day_in_week == 1:
        price = 130
    elif day_in_week in (2, 3):
        price = 100
    elif day_in_week in (4, 5):
        price = 170
    else:
        price = 190

    if zigma:
        price += 20
    else:
        if hour < 12:
            price = max(price - 50, 80)
        elif hour > 20:
            price = max(price - 30, 100)

    return price


def buy_ticket_sfstudent(day_in_week: int, zigma: bool) -> int:
    price = 0
    if day_in_week in (1, 2, 3):
        price = 69
    elif day_in_week in (4, 5):
        price = 79
    else:
        price = 89

    if zigma:
        price += 40

    return price


def buy_ticket(
    day_in_week: int, hour: int, zigma: bool, sfplus_student: bool
) -> int:
    if sfplus_student:
        return buy_ticket_sfstudent(day_in_week, hour, zigma)

    return buy_ticket_basic(day_in_week, hour, zigma)
