def format_date(date):
    return date.strftime("%Y-%m-%d %H:%M")


def date_format(date_time):
    return date_time.isoformat(timespec="seconds")
