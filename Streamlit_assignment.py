import streamlit as st

st.title("Basic Python MCQ Quiz")

# Define questions and answers
questions = [
    {
        "question": "Which of these is the correct file extension for a Python file? ?",
        "options": [".pyth", ".pt", ".pyt", ".py"],
        "answer": ".py"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["deft", "def", "func", "function"],
        "answer": "def"
    }
]

# Keep track of question number
if "q_no" not in st.session_state:
    st.session_state.q_no = 0
    st.session_state.attempted = False
    st.session_state.result = ""

# Show current question
if st.session_state.q_no < len(questions):
    q = questions[st.session_state.q_no]
    st.subheader(f"Q{st.session_state.q_no + 1}: {q['question']}")
    selected = st.radio("Choose your answer:", q["options"], key=f"q{st.session_state.q_no}")

    if st.button("Submit Answer"):
        if selected == q["answer"]:
            st.session_state.result = "Correct!"
            st.success(st.session_state.result)
            st.session_state.q_no += 1
            st.session_state.attempted = False
            st.rerun()  # Refresh to show next question
        else:
            st.session_state.result = "Wrong. Try again."
            st.session_state.attempted = True

    if st.session_state.attempted:
        st.error(st.session_state.result)
else:
    st.success("🎉 You've completed the quiz sucessfully! Get ready for Week 2 🎉")