import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "Model",
    "student_performance_model.pkl"
)

saved_data = joblib.load(MODEL_PATH)

model = saved_data["model"]
encoders = saved_data["encoders"]

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Prediction System")
st.markdown("AI/ML Summer Internship 2026 Capstone Project")

st.divider()

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ['F', 'M']
    )

    nationality = st.selectbox(
        "Nationality",
        ['Egypt','Iran','Iraq','Jordan','KW',
         'Lybia','Morocco','Palestine',
         'SaudiArabia','Syria','Tunis',
         'USA','lebanon','venzuela']
    )

    place_of_birth = st.selectbox(
        "Place of Birth",
        ['Egypt','Iran','Iraq','Jordan','KuwaIT',
         'Lybia','Morocco','Palestine',
         'SaudiArabia','Syria','Tunis',
         'USA','lebanon','venzuela']
    )

    stage = st.selectbox(
        "Stage",
        ['HighSchool','MiddleSchool','lowerlevel']
    )

    grade = st.selectbox(
        "Grade",
        ['G-02','G-04','G-05','G-06',
         'G-07','G-08','G-09',
         'G-10','G-11','G-12']
    )

    section = st.selectbox(
        "Section",
        ['A','B','C']
    )

    topic = st.selectbox(
        "Topic",
        ['Arabic','Biology','Chemistry',
         'English','French','Geology',
         'History','IT','Math',
         'Quran','Science','Spanish']
    )

with col2:

    semester = st.selectbox(
        "Semester",
        ['F','S']
    )

    relation = st.selectbox(
        "Relation",
        ['Father','Mum']
    )

    raisedhands = st.slider(
        "Raised Hands",
        0,100,50
    )

    visited_resources = st.slider(
        "Visited Resources",
        0,100,50
    )

    announcements = st.slider(
        "Announcements Viewed",
        0,100,50
    )

    discussion = st.slider(
        "Discussion Participation",
        0,100,50
    )

    parent_survey = st.selectbox(
        "Parent Answering Survey",
        ['No','Yes']
    )

    parent_satisfaction = st.selectbox(
        "Parent School Satisfaction",
        ['Bad','Good']
    )

    absence_days = st.selectbox(
        "Student Absence Days",
        ['Above-7','Under-7']
    )

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button("Predict Performance"):

    input_df = pd.DataFrame({

        'gender':[gender],
        'NationalITy':[nationality],
        'PlaceofBirth':[place_of_birth],
        'StageID':[stage],
        'GradeID':[grade],
        'SectionID':[section],
        'Topic':[topic],
        'Semester':[semester],
        'Relation':[relation],
        'raisedhands':[raisedhands],
        'VisITedResources':[visited_resources],
        'AnnouncementsView':[announcements],
        'Discussion':[discussion],
        'ParentAnsweringSurvey':[parent_survey],
        'ParentschoolSatisfaction':[parent_satisfaction],
        'StudentAbsenceDays':[absence_days]
    })

    # Encode categorical values

    categorical_columns = [
        'gender',
        'NationalITy',
        'PlaceofBirth',
        'StageID',
        'GradeID',
        'SectionID',
        'Topic',
        'Semester',
        'Relation',
        'ParentAnsweringSurvey',
        'ParentschoolSatisfaction',
        'StudentAbsenceDays'
    ]

    for col in categorical_columns:

        encoder = encoders[col]

        input_df[col] = encoder.transform(
            input_df[col]
        )

    prediction = model.predict(input_df)[0]

    class_encoder = encoders["Class"]

    predicted_class = class_encoder.inverse_transform(
        [prediction]
    )[0]

    st.divider()

    if predicted_class == "H":

        st.success(
            "🏆 Predicted Performance: HIGH"
        )

    elif predicted_class == "M":

        st.warning(
            "📘 Predicted Performance: MEDIUM"
        )

    else:

        st.error(
            "📉 Predicted Performance: LOW"
        )

    st.subheader("Prediction Result")

    st.write(
        f"Predicted Class: {predicted_class}"
    )