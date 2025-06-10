# ruff: noqa: E402
from pathlib import Path
from types import ModuleType, SimpleNamespace
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pytest


def _stub_st(captured: dict) -> ModuleType:
    st = ModuleType("streamlit")
    st.sidebar = SimpleNamespace(
        title=lambda text: captured.setdefault("title", text),
        radio=lambda label, opts: captured.setdefault("options", opts) or opts[0],
        selectbox=lambda label, opts: opts[0],
    )
    st.set_page_config = lambda **k: None
    st.write = lambda *a, **k: captured.setdefault("writes", []).append(
        " ".join(str(x) for x in a)
    )
    return st


sys.modules.setdefault("streamlit", _stub_st({}))

import app
from src.ui import dashboard, status_bar, content_card


def test_render_status_bar(monkeypatch):
    cap: dict[str, object] = {}
    monkeypatch.setattr(status_bar, "st", _stub_st(cap))
    status_bar.render_status_bar()
    out = " ".join(cap["writes"]) if cap.get("writes") else ""
    assert "Navigator-Ingest" in out and "Strategy" in out and "Pipeline" in out


def test_render_content_card(monkeypatch):
    cap: dict[str, object] = {}
    monkeypatch.setattr(content_card, "st", _stub_st(cap))
    content_card.render_content_card(
        {"title": "Test", "status": "Idle", "summary": "All good"}
    )
    assert cap["writes"] == ["### Test", "Status: Idle", "All good"]


def test_dashboard_status_bar(monkeypatch):
    cap: dict[str, object] = {}
    st = _stub_st(cap)
    st.sidebar.radio = lambda _label, _opts: "Goals"
    monkeypatch.setattr(dashboard, "st", st)
    monkeypatch.setattr(status_bar, "st", st)
    dashboard.render_dashboard()
    assert "Navigator-Ingest" in cap["writes"][0]
    assert cap["writes"][-1] == "Goals View"


@pytest.mark.parametrize(
    "section,exp",
    [
        ("Goals", "Goals View"),
        ("Results", "Results View"),
        ("Settings", "Settings View"),
    ],
)
def test_dashboard_all(monkeypatch, section: str, exp: str):
    cap: dict[str, object] = {}
    st = _stub_st(cap)
    st.sidebar.radio = lambda _label, _opts: section
    st.write = lambda msg: cap.setdefault("writes", []).append(msg)
    monkeypatch.setattr(dashboard, "st", st)
    monkeypatch.setattr(status_bar, "st", st)
    dashboard.render_dashboard()
    assert cap["writes"][-1] == exp


def test_app_main(monkeypatch):
    cap: dict[str, object] = {}
    st = _stub_st(cap)
    st.sidebar.radio = lambda _label, opts: cap.setdefault("options", opts) or "Goals"
    monkeypatch.setattr(app, "st", st)
    monkeypatch.setattr(dashboard, "st", st)
    monkeypatch.setattr(status_bar, "st", st)
    app.main()
    assert "Navigator-Ingest" in " ".join(cap["writes"])
    assert cap["options"] == ["Goals", "Results", "Settings"]
