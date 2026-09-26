from fuzzy.rules import calculate_study_intensity


def get_study_intensity(
    preparation,
    difficulty,
    hours_per_day
):

    score = calculate_study_intensity(
        preparation,
        difficulty,
        hours_per_day
    )

    if score >= 75:
        level = "High Intensity"

    elif score >= 50:
        level = "Moderate Intensity"

    else:
        level = "Low Intensity"

    return {
        "score": score,
        "level": level
    }