def calculate_study_intensity(
    preparation,
    difficulty,
    hours_per_day
):

    intensity = 50

    # Preparation
    if preparation < 40:
        intensity += 25
    elif preparation < 70:
        intensity += 10
    else:
        intensity -= 5

    # Difficulty
    if difficulty >= 70:
        intensity += 20
    elif difficulty >= 50:
        intensity += 10

    # Available time
    if hours_per_day < 2:
        intensity += 15
    elif hours_per_day >= 5:
        intensity -= 5

    return max(0, min(100, intensity))