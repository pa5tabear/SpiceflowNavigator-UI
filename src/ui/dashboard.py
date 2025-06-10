import streamlit as st

from .status_bar import render_status_bar
from .content_feed import render_content_feed

SECTIONS = ["Goals", "Results", "Settings"]


def render_sidebar() -> str:
    """Render the sidebar navigation and return selected section."""
    st.sidebar.title("Navigation")
    return st.sidebar.radio("Go to", SECTIONS)


def render_dashboard() -> None:
    """Render the dashboard based on selected navigation section."""
    section = render_sidebar()
    render_status_bar()
    if section == "Goals":
        render_content_feed()
        st.write("Goals View")
    elif section == "Results":
        st.write("Results View")
    elif section == "Settings":
        st.write("Settings View")
