import streamlit as st
from ai_writer import spin_chapter, review_chapter



st.title("AI-Assisted Chapter Editor")

original = open("chapter.txt", "r", encoding="utf-8").read()

if st.button("AI Spin Chapter"):
    spun = spin_chapter(original)
    st.session_state["spun"] = spun

if "spun" in st.session_state:
    st.text_area("Spun Version", st.session_state["spun"], height=300)

    if st.button("AI Review"):
        reviewed = review_chapter(st.session_state["spun"])
        st.session_state["reviewed"] = reviewed

if "reviewed" in st.session_state:
    st.text_area("Reviewed Version", st.session_state["reviewed"], height=300)
    final = st.text_area("Final Human Edit", st.session_state["reviewed"], height=300)
    if st.button("Save Final Version"):
        with open("final.txt", "w", encoding="utf-8") as f:
            f.write(final)
        st.success("Final version saved!")
