def calculate_daily_distribution(
    hours_per_day,
    intensity
):

    if intensity == "High Intensity":

        study_hours = max(
            1,
            hours_per_day - 1
        )

        revision = 1

    elif intensity == "Moderate Intensity":

        study_hours = max(
            1,
            hours_per_day - 0.5
        )

        revision = 0.5

    else:

        study_hours = max(
            1,
            hours_per_day
        )

        revision = 0.5

    return {
        "focused_study": study_hours,
        "revision": revision
    }


def get_focus_message(score):

    if score >= 75:
        return (
            "Focus strongly on difficult and weak topics "
            "with regular practice and revision."
        )

    elif score >= 50:
        return (
            "Maintain a balanced schedule between learning, "
            "practice and revision."
        )

    else:
        return (
            "Use a comfortable study schedule with "
            "consistent revision."
        )