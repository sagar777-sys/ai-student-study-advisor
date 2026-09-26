from fuzzy.inference import get_study_intensity


result = get_study_intensity(
    preparation=40,
    difficulty=80,
    hours_per_day=4
)

print(result)