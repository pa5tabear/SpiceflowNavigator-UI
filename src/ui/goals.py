import streamlit as st
from src.models.goal import load_goals, create_goal, delete_goal


def render_goals() -> None:
    st.write("Goals View")
    goals = load_goals()
    for g in goals:
        cols = st.columns(2)
        cols[0].write(f"{g.title} ({g.status})")
        if cols[1].button("Delete", key=f"del-{g.id}"):
            delete_goal(g.id)
            st.experimental_rerun()
    title = st.text_input("Title")
    desc = st.text_area("Description")
    if st.button("Add Goal") and title:
        create_goal(title, desc)
        st.experimental_rerun()
