import streamlit as st

SECTIONS = ["Goals", "Results", "Settings"]


def render_sidebar() -> str:
    """Render the sidebar navigation and return selected section."""
    st.sidebar.title("Navigation")
    return st.sidebar.radio("Go to", SECTIONS)


def render_dashboard() -> None:
    """Render the dashboard based on selected navigation section."""
    section = render_sidebar()
    if section == "Goals":
        st.write("Goals View")
    elif section == "Results":
        st.write("Results View")
    elif section == "Settings":
        st.write("Settings View")
