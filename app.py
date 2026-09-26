import streamlit as st

from ai.parser import generate_ai_plan
from fuzzy.inference import get_study_intensity
from utils.study_plan import (
    calculate_daily_distribution,
    get_focus_message
)


st.set_page_config(
    page_title="AI Study Plan Generator",
    page_icon="📚",
    layout="centered"
)


st.title("📚 AI Study Plan Generator")

st.write(
    "Generate a personalized study plan using "
    "AI + LangChain + Fuzzy Logic."
)

st.divider()


st.subheader("🧑‍🎓 Tell Us About Your Study Goals")


student_query = st.text_area(
    "Describe your study requirements:",
    placeholder=(
        "Example: I have Mathematics, Physics and Chemistry "
        "exams in 20 days. Mathematics is my weakest subject. "
        "Physics is difficult and I can study 5 hours daily."
    ),
    height=150
)


col1, col2 = st.columns(2)


with col1:

    days = st.number_input(
        "📅 Days Available",
        min_value=1,
        max_value=365,
        value=20
    )

    preparation = st.slider(
        "📖 Current Preparation",
        min_value=0,
        max_value=100,
        value=50
    )


with col2:

    hours_per_day = st.number_input(
        "⏰ Study Hours Per Day",
        min_value=1.0,
        max_value=16.0,
        value=4.0,
        step=0.5
    )

    difficulty = st.slider(
        "🧠 Subject Difficulty",
        min_value=0,
        max_value=100,
        value=60
    )


st.divider()


if st.button(
    "🚀 Generate My Study Plan",
    use_container_width=True
):

    if not student_query.strip():

        st.warning(
            "Please describe your study requirements."
        )

    else:

        with st.spinner(
            "🤖 AI is generating your study plan..."
        ):

            try:

                # FUZZY LOGIC
                fuzzy_result = get_study_intensity(
                    preparation,
                    difficulty,
                    hours_per_day
                )

                daily_distribution = (
                    calculate_daily_distribution(
                        hours_per_day,
                        fuzzy_result["level"]
                    )
                )

                focus_message = get_focus_message(
                    fuzzy_result["score"]
                )


                # AI
                ai_plan = generate_ai_plan(
                    student_query,
                    days,
                    hours_per_day,
                    preparation,
                    difficulty
                )


                st.success(
                    "Your personalized study plan is ready!"
                )


                st.subheader(
                    "🧠 Fuzzy Logic Assessment"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Study Intensity",
                        f"{fuzzy_result['score']}/100"
                    )

                with col2:

                    st.metric(
                        "Intensity Level",
                        fuzzy_result["level"]
                    )


                st.info(focus_message)


                st.subheader(
                    "⏱️ Recommended Daily Distribution"
                )

                st.write(
                    f"📚 Focused Study: "
                    f"**{daily_distribution['focused_study']} hours**"
                )

                st.write(
                    f"🔄 Revision: "
                    f"**{daily_distribution['revision']} hours**"
                )


                st.subheader(
                    "🤖 AI Generated Study Plan"
                )

                st.markdown(ai_plan)


            except Exception as e:

                st.error(
                    "Unable to generate the study plan."
                )

                st.info(
                    "Please check your Gemini API key "
                    "and installed dependencies."
                )

                st.exception(e)