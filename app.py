"""Streamlit entry point for SpiceflowNavigator UI."""

import streamlit as st

from src.ui.dashboard import render_dashboard


def main() -> None:
    """Run the Streamlit application."""
    st.set_page_config(page_title="SpiceflowNavigator")
    render_dashboard()


if __name__ == "__main__":
    main()
