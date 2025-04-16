import streamlit as st
import pandas as pd
from datetime import datetime
from quiz import quiz_data
import json
import os

st.title("Python Quiz")

user_name = st.text_input("Enter your name to begin")

if user_name:
    user_answers = []
    score = 0

    # display each question
    for index, ques in enumerate(quiz_data):
        st.subheader(f"Q{index+1}: {ques["question"]}")
        user_choice = st.radio("Select your answer:", ques["options"], key=index)
        user_answers.append(
            {
                "question": ques["question"],
                "user_answer": user_choice,
                "correct_answer": ques["answer"],
                "is_correct": user_choice == ques["answer"],
            }
        )
    if st.button("Submit Quiz"):
        score = sum([1 for ans in user_answers if ans["is_correct"]])
        st.success(f"Your score is {score} out of {len(quiz_data)}")

        user_data = {
            "user": user_name,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "score": score,
            "total_question": len(quiz_data),
            "answers": user_answers,
        }

        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as file:
                data = json.load(file)
        else:
            data = []

        data.append(user_data)

        # saved updated user data
        with open("user_data.json", "w") as file:
            json.dump(data, file, indent=4)

        st.success("📝 Your answers have been saved.")

        # csv method
        # df = pd.DataFrame(user_answers)
        # df["user"] = user_name
        # df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # df.to_csv("user_anmswer.csv", mode="a", index=False, header=False)

        # st.write("your Answer:")
        # st.dataframe(df)
