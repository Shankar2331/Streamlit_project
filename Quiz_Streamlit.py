import streamlit as st

st.set_page_config(page_title="General Knowledge Quiz", page_icon="🧠")

st.title("General Knowledge Quiz")
st.write("Test your knowledge by answering the following questions!")

# Store score
score = 0

# Question 1
st.subheader("1. What is the largest ocean on Earth?")
q1 = st.radio(
    "Choose an option:",
    ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    key="q1"
)
if q1:
    if q1 == "Pacific Ocean":
        st.success("Correct! The Pacific Ocean is the largest.")
        score += 1
    else:
        st.error("Incorrect. The correct answer is: Pacific Ocean.")

# Question 2
st.subheader('2. Which planet is known as the "Red Planet"?')
q2 = st.radio(
    "Choose an option:",
    ["Jupiter", "Mars", "Venus", "Saturn"],
    key="q2"
)
if q2:
    if q2 == "Mars":
        st.success("Correct! Mars is called the Red Planet.")
        score += 1
    else:
        st.error("Incorrect. The correct answer is: Mars.")

# Question 3
st.subheader("3. What is the currency of Japan?")
q3 = st.radio(
    "Choose an option:",
    ["Won", "Yuan", "Yen", "Ringgit"],
    key="q3"
)
if q3:
    if q3 == "Yen":
        st.success("Correct! Japan uses the Yen.")
        score += 1
    else:
        st.error("Incorrect. The correct answer is: Yen.")

# Final score
if q1 and q2 and q3:
    st.markdown("---")
    st.subheader("🎉 Your Final Score")
    st.write(f"**{score} / 3**")
    if score == 3:
        st.balloons()
        st.success("Excellent work! You got all questions right! 🎉")
    elif score == 2:
        st.info("Good job! You got 2 out of 3.")
    else:
        st.warning("Keep practicing! You can do better next time.")

