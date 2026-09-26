import streamlit as st

from ai.parser import generate_ai_plan
from fuzzy.inference import get_study_intensity
from utils.study_plan import (
    calculate_daily_distribution,
    get_focus_message
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Study Plan Generator",
    page_icon="📚",
    layout="centered"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #555;
        margin-bottom: 20px;
    }

    .plan-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #d9d9d9;
        background-color: #f8f9fa;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 650;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📚 AI Study Plan Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Generate a personalized study plan using '
    '<b>AI + LangChain + Fuzzy Logic</b>.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# USER INPUT
# ============================================================

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


# ============================================================
# INPUT CONTROLS
# ============================================================

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


# ============================================================
# FORMAT AI RESPONSE
# ============================================================

def format_ai_plan(plan):
    """
    Clean and format the AI generated study plan
    before displaying it in Streamlit.
    """

    if plan is None:
        return "No study plan was generated."

    # Convert response to string
    if isinstance(plan, str):
        text = plan
    else:
        text = str(plan)

    # Fix escaped new lines
    text = text.replace("\\r\\n", "\n")
    text = text.replace("\\n", "\n")
    text = text.replace("\\t", "\t")

    # Remove unnecessary Markdown code fences
    text = text.replace("```markdown", "")
    text = text.replace("```md", "")
    text = text.replace("```", "")

    # Remove excessive blank lines
    lines = text.splitlines()

    cleaned_lines = []
    previous_blank = False

    for line in lines:

        line = line.rstrip()

        if line.strip() == "":
            if not previous_blank:
                cleaned_lines.append("")
            previous_blank = True

        else:
            cleaned_lines.append(line)
            previous_blank = False

    text = "\n".join(cleaned_lines).strip()

    return text


# ============================================================
# GENERATE STUDY PLAN
# ============================================================

if st.button(
    "🚀 Generate My Study Plan",
    use_container_width=True
):

    if not student_query.strip():

        st.warning(
            "⚠️ Please describe your study requirements."
        )

    else:

        with st.spinner(
            "🤖 AI is generating your personalized study plan..."
        ):

            try:

                # ====================================================
                # FUZZY LOGIC
                # ====================================================

                fuzzy_result = get_study_intensity(
                    preparation,
                    difficulty,
                    hours_per_day
                )

                daily_distribution = calculate_daily_distribution(
                    hours_per_day,
                    fuzzy_result["level"]
                )

                focus_message = get_focus_message(
                    fuzzy_result["score"]
                )


                # ====================================================
                # AI STUDY PLAN
                # ====================================================

                ai_plan = generate_ai_plan(
                    student_query,
                    days,
                    hours_per_day,
                    preparation,
                    difficulty
                )


                # ====================================================
                # SUCCESS MESSAGE
                # ====================================================

                st.success(
                    "✅ Your personalized study plan is ready!"
                )


                # ====================================================
                # FUZZY LOGIC ASSESSMENT
                # ====================================================

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


                # ====================================================
                # DAILY DISTRIBUTION
                # ====================================================

                st.subheader(
                    "⏱️ Recommended Daily Distribution"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "📚 Focused Study",
                        f"{daily_distribution['focused_study']} hrs"
                    )

                with col2:

                    st.metric(
                        "🔄 Revision",
                        f"{daily_distribution['revision']} hrs"
                    )


                # ====================================================
                # AI GENERATED STUDY PLAN
                # ====================================================

                st.subheader(
                    "🤖 AI Generated Study Plan"
                )

                formatted_plan = format_ai_plan(ai_plan)


                # Display the AI response as proper Markdown
                with st.container(border=True):

                    st.markdown(
                        formatted_plan
                    )


                # ====================================================
                # FOOTER MESSAGE
                # ====================================================

                st.divider()

                st.caption(
                    "📚 Study consistently • Revise regularly • "
                    "Practice actively"
                )


            except Exception as e:

                st.error(
                    "❌ Unable to generate the study plan."
                )

                st.info(
                    "Please check your Gemini API key, "
                    "dependencies and application configuration."
                )

                # Useful during development/debugging
                with st.expander("🔧 Technical Error Details"):

                    st.exception(e)
