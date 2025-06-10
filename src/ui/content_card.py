"""Content card component for Navigator UI."""

from __future__ import annotations

import streamlit as st


def render_content_card(content: dict[str, str]) -> None:
    """Display a simple content card with title, status, and summary."""
    st.write(f"### {content.get('title', '')}")
    st.write(f"Status: {content.get('status', '')}")
    st.write(content.get("summary", ""))
