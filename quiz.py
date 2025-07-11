import streamlit as st

# 🎓 Title
st.title("🎯 Simple Quiz App")
st.write("Test your knowledge with this fun quiz! 🧠")

# 📝 Questions and Answers
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {``
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is 7 x 8?",
        "options": ["54", "56", "64", "58"],
        "answer": "56"
    }
]

# 🌟 Use session_state to persist score and answered questions
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = [False] * len(quiz)

# 📖 Loop through each question
for i, q in enumerate(quiz):
    st.subheader(f"Q{i+1}: {q['question']}")
    user_answer = st.radio(
        f"Choose your answer for Q{i+1}:",
        q['options'],
        key=f"question_{i}"
    )
    if st.button(f"Submit Answer for Q{i+1}", key=f"submit_{i}"):
        if st.session_state.answered[i]:
            st.warning("⚠️ You have already answered this question.")
        else:
            if user_answer == q['answer']:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! The correct answer was: {q['answer']}")
            st.session_state.answered[i] = True

st.write("---")

# 🏆 Show final score
if st.button("Show Final Score"):
    total_questions = len(quiz)
    st.info(f"Your final score: **{st.session_state.score} / {total_questions}** 🎉")
    if st.session_state.score == total_questions:
        st.balloons()
