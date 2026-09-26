from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os


def generate_study_plan(
    subjects,
    exam_goal,
    days,
    daily_hours,
    current_level,
    topics
):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0.4
    )

    prompt = ChatPromptTemplate.from_template("""
You are an expert AI Study Planner.

Create a practical and personalized study plan based on the student's information.

STUDENT INFORMATION:
Subjects: {subjects}
Exam / Goal: {exam_goal}
Number of days: {days}
Daily study hours: {daily_hours}
Current level: {current_level}
Topics to cover: {topics}

IMPORTANT RULES:
1. Create a realistic day-by-day study plan.
2. Do not overload the student.
3. Include breaks.
4. Include revision sessions.
5. Include practice/question-solving sessions.
6. Give more time to difficult subjects/topics.
7. Include a final revision before the exam.
8. Keep the plan achievable within the given daily study hours.
9. Do NOT write unnecessary explanations.
10. Use clean Markdown formatting.

RETURN EXACTLY IN THIS FORMAT:

# 🎯 Personalized Study Plan

## 📌 Study Strategy
Give 3-5 short points about the recommended strategy.

## 📚 Subject Priority
Create a table:

| Subject | Priority | Reason |
|---|---|---|

## 📅 Day-by-Day Plan

### Day 1
- **Session 1:** Topic — Duration
- **Session 2:** Topic — Duration
- **Session 3:** Topic — Duration
- **Revision:** Topic
- **Practice:** What to practice

Continue for every day.

## 🔄 Revision Strategy
Give a short revision strategy.

## 📝 Practice & Mock Tests
Mention when the student should solve questions, previous papers and mock tests.

## 💡 Personalized Tips
Give 5 useful tips specifically for this student.

Make sure the plan matches the number of days and daily study hours.
""")

    chain = prompt | llm

    response = chain.invoke({
        "subjects": subjects,
        "exam_goal": exam_goal,
        "days": days,
        "daily_hours": daily_hours,
        "current_level": current_level,
        "topics": topics
    })

    return response.content