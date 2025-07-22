import streamlit as st
import time

# --- Page Settings ---
st.set_page_config(page_title="Digital Marketing Quiz 2025", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
        body {
            background-color: #f0f6ff;
        }
        h1, h2, h3, .stTextInput > label {
            color: #004080;
        }
        .stButton button {
            background-color: #0a66c2;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5rem 1rem;
        }
        .stButton button:hover {
            background-color: #004a99;
        }
        .question-box {
            background-color: #ffffff;
            border: 1px solid #cce0ff;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
        .result-box {
            background-color: #eaf4ff;
            border-left: 6px solid #0073e6;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Quiz Data ---
questions = [
    # [same 10-question data here...]
    {
        "question": "What is the primary benefit of using AI in digital marketing?",
        "options": ["", "Reducing website traffic", "Automating repetitive tasks and personalizing user experiences", "Slowing down content delivery", "Limiting data collection"],
        "answer": "Automating repetitive tasks and personalizing user experiences"
    },
    {
        "question": "Which platform is best known for short-form video content marketing in 2025?",
        "options": ["", "Twitter", "LinkedIn", "TikTok", "Reddit"],
        "answer": "TikTok"
    },
    {
        "question": "What does PPC stand for in online advertising?",
        "options": ["", "Pay Per Conversion", "Post Promotion Campaign", "Pay Per Click", "Paid Page Content"],
        "answer": "Pay Per Click"
    },
    {
        "question": "Which of the following is NOT a Google Ads campaign type?",
        "options": ["", "Display", "Video", "Virtual Reality", "Search"],
        "answer": "Virtual Reality"
    },
    {
        "question": "In email marketing, what does a high bounce rate typically indicate?",
        "options": ["", "Successful delivery", "Incorrect or inactive email addresses", "High engagement", "Strong subject lines"],
        "answer": "Incorrect or inactive email addresses"
    },
    {
        "question": "What is “remarketing” in digital advertising?",
        "options": ["", "Targeting new audiences with your ads", "Reposting old blog content", "Showing ads to users who have previously visited your site", "Changing product pricing online"],
        "answer": "Showing ads to users who have previously visited your site"
    },
    {
        "question": "Which metric shows how many users left a website after viewing only one page?",
        "options": ["", "Conversion Rate", "Bounce Rate", "Cost Per Click", "Page Rank"],
        "answer": "Bounce Rate"
    },
    {
        "question": "What is the primary function of a content management system (CMS)?",
        "options": ["", "Editing photos", "Managing customer orders", "Creating and publishing digital content", "Sending automated messages"],
        "answer": "Creating and publishing digital content"
    },
    {
        "question": "Which of these strategies is best for improving organic search rankings?",
        "options": ["", "Buying followers", "Keyword stuffing", "Creating high-quality, relevant content", "Running paid ads"],
        "answer": "Creating high-quality, relevant content"
    },
    {
        "question": "What does a “conversion” usually mean in digital marketing?",
        "options": ["", "A user clicking on a social media post", "A website visitor becoming a lead or customer", "The number of video views", "A search engine indexing your site"],
        "answer": "A website visitor becoming a lead or customer"
    }
]

# --- Timer Configuration ---
QUIZ_DURATION_MINUTES = 5
QUIZ_DURATION_SECONDS = QUIZ_DURATION_MINUTES * 60

# --- Session State Initialization ---
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "user_answers" not in st.session_state:
    st.session_state.user_answers = [""] * len(questions)

# --- App Start ---
st.title("⏳ Digital Marketing Quiz 2025 with Timer")
name = st.text_input("👤 Enter your name to start the quiz:")

if name and not st.session_state.submitted:
    # Set timer start
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()

    # --- Time Calculation ---
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = QUIZ_DURATION_SECONDS - elapsed

    minutes = remaining // 60
    seconds = remaining % 60
    st.markdown(f"### ⏱️ Time Remaining: **{minutes:02d}:{seconds:02d}**")
    st.progress((QUIZ_DURATION_SECONDS - remaining) / QUIZ_DURATION_SECONDS)

    if remaining <= 0:
        st.error("⏰ Time's up! Submitting your quiz...")
        st.session_state.submitted = True

    # --- Display Questions ---
    if not st.session_state.submitted:
        for i, q in enumerate(questions):
            st.markdown(f"<div class='question-box'><strong>Q{i+1}:</strong> {q['question']}</div>", unsafe_allow_html=True)
            st.session_state.user_answers[i] = st.selectbox(
                "Choose your answer:",
                q["options"],
                index=q["options"].index(st.session_state.user_answers[i]) if st.session_state.user_answers[i] else 0,
                key=f"q{i}"
            )

        if st.button("🚀 Submit Quiz"):
            st.session_state.submitted = True

# --- Result Section ---
if st.session_state.submitted:
    score = 0
    incorrect = []

    for i, q in enumerate(questions):
        if st.session_state.user_answers[i] == q["answer"]:
            score += 1
        else:
            incorrect.append({
                "question": q["question"],
                "your_answer": st.session_state.user_answers[i],
                "correct_answer": q["answer"]
            })

    percent = (score / len(questions)) * 100
    st.markdown("---")
    st.markdown(f"<div class='result-box'><h3>🎯 Result for {name}</h3><p><strong>Score:</strong> {score} / {len(questions)}<br><strong>Percentage:</strong> {percent:.1f}%</p></div>", unsafe_allow_html=True)

    if incorrect:
        st.markdown("### ❌ Review Incorrect Answers")
        for item in incorrect:
            st.markdown(f"""
            <div class='result-box'>
                🔹 <strong>Question:</strong> {item['question']}  
                <br>❌ <strong>Your Answer:</strong> {item['your_answer']}  
                <br>✅ <strong>Correct Answer:</strong> {item['correct_answer']}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.balloons()
        st.success("🎉 Perfect score! You nailed it!")

# 👣 Floating Footer
from muthu_footer import add_footer
add_footer()
