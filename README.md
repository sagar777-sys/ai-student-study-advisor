# 📚 AI Study Plan Generator

An AI-powered study planning application that generates personalized study plans using LangChain, Google Gemini and Fuzzy Logic.

## 🎯 Objective

The project helps students create personalized study schedules based on their study goals, available time, preparation level and subject difficulty.

## 🤖 AI Component

Google Gemini with LangChain is used to:

- Understand natural-language student requirements
- Identify subjects and goals
- Identify weak areas
- Generate personalized study plans
- Provide revision and exam preparation suggestions

## 🧠 Fuzzy Logic Component

Fuzzy Logic is used to calculate study intensity based on:

- Current preparation
- Subject difficulty
- Available study hours

The system classifies the study requirement into:

- Low Intensity
- Moderate Intensity
- High Intensity

## 🛠 Technologies

- Python
- Streamlit
- LangChain
- Google Gemini
- Fuzzy Logic

## 📁 Project Structure

```text
ai-study-plan-generator/
│
├── ai/
├── fuzzy/
├── utils/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── test_ai.py
├── test_fuzzy.py
└── test_plan.py