"""Filtering controls for content feed."""

from __future__ import annotations

import streamlit as st


def render_filters(statuses: list[str], sources: list[str]) -> tuple[str, str]:
    """Return selected status and source options."""
    status = st.sidebar.selectbox("Status", ["All"] + statuses)
    source = st.sidebar.selectbox("Source", ["All"] + sources)
    return status, source
