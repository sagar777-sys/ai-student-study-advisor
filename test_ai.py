from ai.parser import generate_ai_plan


query = """
I have Mathematics and Physics exams in 15 days.
Mathematics is weak and Physics is difficult.
I can study 4 hours daily.
"""


result = generate_ai_plan(
    query,
    days=15,
    hours_per_day=4,
    preparation=45,
    difficulty=75
)


print(result)