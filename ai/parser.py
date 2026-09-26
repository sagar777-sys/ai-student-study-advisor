import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_api_key():
    key = os.getenv("GEMINI_API_KEY")

    if key:
        return key

    try:
        import streamlit as st
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return None


def generate_ai_plan(
    student_query,
    days,
    hours_per_day,
    preparation,
    difficulty
):

    api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not configured."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=api_key,
        temperature=0.4
    )

    prompt = f"""
You are an AI Study Plan Generator.

Create a personalized study plan for a student.

Student's request:
{student_query}

Available study days: {days}
Study hours per day: {hours_per_day}
Current preparation level: {preparation}/100
Subject difficulty: {difficulty}/100

Your task:

1. Understand the student's subjects and goals.
2. Identify weak areas.
3. Suggest subject priorities.
4. Create a practical study schedule.
5. Include revision and practice sessions.
6. Include breaks.
7. Give exam preparation tips.

Return the answer in a clear format:

STUDENT ANALYSIS
...

SUBJECT PRIORITIES
...

DAILY STUDY PLAN
...

REVISION PLAN
...

EXAM TIPS
...

Keep the plan realistic and easy to follow.
"""

    response = llm.invoke(prompt)

    return response.content