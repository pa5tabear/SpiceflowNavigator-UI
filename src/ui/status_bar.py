"""Static status bar component for Navigator UI."""

import streamlit as st

STATUSES = {
    "Navigator-Ingest": "Idle",
    "Strategy": "Idle",
    "Pipeline": "Idle",
}


def render_status_bar() -> None:
    """Display fixed agent status information."""
    status_line = " | ".join(f"{name}: {state}" for name, state in STATUSES.items())
    st.write(status_line)
