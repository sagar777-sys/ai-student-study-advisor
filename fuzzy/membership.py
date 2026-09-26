def low(value):
    if value <= 30:
        return 1.0
    elif value >= 60:
        return 0.0
    else:
        return (60 - value) / 30


def medium(value):
    if value <= 30 or value >= 80:
        return 0.0
    elif value <= 55:
        return (value - 30) / 25
    else:
        return (80 - value) / 25


def high(value):
    if value <= 50:
        return 0.0
    elif value >= 80:
        return 1.0
    else:
        return (value - 50) / 30