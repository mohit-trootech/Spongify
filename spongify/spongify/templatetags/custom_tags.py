from django.template import Library
from django.utils.timezone import now

register = Library()


@register.simple_tag
def period_of_day(*args):
    "Return Period of Day"
    from pytz import timezone

    tz = timezone("Asia/Kolkata")
    time = now().astimezone(tz=tz).time().hour
    if time >= 5 and time <= 11:
        return "Morning"
    elif time >= 12 and time <= 17:
        return "Afternoon"
    elif time >= 18 and time <= 22:
        return "Evening"
    else:
        return "Night"
