import streamlit as st
import requests

st.title("Skin Care Assistant")

skin_type = st.selectbox("Skin Type", ["Oily", "Dry", "Combination"])
symptoms = st.text_area("Describe your skin problem")

if st.button("Analyze"):
    res = requests.post("http://127.0.0.1:8000/analyze", json={
        "skin_type": skin_type,
        "symptoms": symptoms
    }).json()

    st.subheader("Diagnosis")
    st.write(res["diagnosis"])

    st.subheader("Routine")
    st.write(res["routine"])


feedback = st.text_area("Follow-up feedback")

if st.button("Update Routine"):
    res = requests.post("http://127.0.0.1:8000/followup", json={
        "feedback": feedback
    }).json()

    st.write(res["updated_routine"])
