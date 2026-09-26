from utils.study_plan import (
    calculate_daily_distribution,
    get_focus_message
)


result = calculate_daily_distribution(
    hours_per_day=5,
    intensity="High Intensity"
)

print(result)

print(
    get_focus_message(80)
)