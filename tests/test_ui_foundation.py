# ruff: noqa: E402
"""Tests for Streamlit UI foundation."""

from pathlib import Path
from types import ModuleType, SimpleNamespace
import pytest
import sys


def _create_stub_streamlit(captured: dict) -> ModuleType:
    st = ModuleType("streamlit")

    def radio(label: str, options: list[str]):
        captured.setdefault("options", options)
        return options[0]

    st.sidebar = SimpleNamespace(
        title=lambda text: captured.setdefault("title", text),
        radio=radio,
        selectbox=lambda label, opts: opts[0],
    )
    st.set_page_config = lambda **kwargs: None
    st.write = lambda *args, **kwargs: None
    return st


# Ensure repository root is on path and streamlit is stubbed before imports
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

captured_import: dict[str, object] = {}
sys.modules.setdefault("streamlit", _create_stub_streamlit(captured_import))

import app
from src.ui import dashboard


def _build_dummy_streamlit(captured: dict) -> ModuleType:
    return _create_stub_streamlit(captured)


def test_main_runs_with_navigation(monkeypatch):
    captured: dict[str, object] = {}
    dummy_st = _build_dummy_streamlit(captured)
    monkeypatch.setattr(app, "st", dummy_st)
    monkeypatch.setattr(dashboard, "st", dummy_st)

    app.main()

    assert captured.get("options") == ["Goals", "Results", "Settings"]


def test_render_sidebar(monkeypatch):
    captured: dict[str, object] = {}
    dummy_st = _build_dummy_streamlit(captured)
    monkeypatch.setattr(dashboard, "st", dummy_st)

    result = dashboard.render_sidebar()

    assert result == "Goals"
    assert captured.get("options") == ["Goals", "Results", "Settings"]


@pytest.mark.parametrize(
    "section,expected",
    [
        ("Goals", "Goals View"),
        ("Results", "Results View"),
        ("Settings", "Settings View"),
    ],
)
def test_render_dashboard_sections(monkeypatch, section: str, expected: str):
    captured: dict[str, object] = {}
    outputs: list[str] = []

    dummy_st = _build_dummy_streamlit(captured)
    dummy_st.sidebar.radio = lambda label, options: section
    dummy_st.write = lambda msg: outputs.append(msg)
    monkeypatch.setattr(dashboard, "st", dummy_st)

    dashboard.render_dashboard()

    assert outputs[-1] == expected
