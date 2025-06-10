# ruff: noqa: E402
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tests.test_ui_foundation import _build_dummy_streamlit
from src.models import goal
from src.ui import dashboard


def test_goal_crud(tmp_path, monkeypatch):
    file = tmp_path / "goals.json"
    monkeypatch.setattr(goal, "GOALS_FILE", file)
    g = goal.create_goal("A", "desc", path=file)
    assert goal.load_goals(file)[0].id == g.id
    goal.update_goal(g.id, title="B", path=file)
    assert goal.load_goals(file)[0].title == "B"
    goal.delete_goal(g.id, path=file)
    assert goal.load_goals(file) == []


def test_dashboard_uses_goal_view(monkeypatch):
    captured = {}
    dummy_st = _build_dummy_streamlit(captured)
    dummy_st.sidebar.radio = lambda label, options: "Goals"
    monkeypatch.setattr(dashboard, "st", dummy_st)
    called = []
    monkeypatch.setattr(dashboard, "render_goals", lambda: called.append(True))
    dashboard.render_dashboard()
    assert called
