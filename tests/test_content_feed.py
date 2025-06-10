# ruff: noqa: E402
from pathlib import Path
from types import ModuleType, SimpleNamespace
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


# Utility to create a dummy streamlit replacement
def _stub_st(captured: dict) -> ModuleType:
    st = ModuleType("streamlit")
    st.sidebar = SimpleNamespace(
        selectbox=lambda _label, opts: opts[0],
        radio=lambda _label, opts: opts[0],
        title=lambda text: captured.setdefault("title", text),
    )
    st.write = lambda *a, **k: captured.setdefault("writes", []).append(
        " ".join(str(x) for x in a)
    )
    st.set_page_config = lambda **k: None
    return st


from src.ui import content_feed, filters, content_card


def test_mock_content_basic():
    assert len(content_feed.MOCK_CONTENT) >= 10
    first = content_feed.MOCK_CONTENT[0]
    assert {"title", "source", "timestamp"} <= first.keys()


def test_filter_content():
    items = [
        {"title": "t1", "status": "New", "source": "A"},
        {"title": "t2", "status": "Done", "source": "B"},
    ]
    assert content_feed.filter_content(items, status="New") == [items[0]]
    assert content_feed.filter_content(items, source="B") == [items[1]]
    assert content_feed.filter_content(items, status="New", source="A") == [items[0]]


def test_render_content_feed(monkeypatch):
    cap: dict[str, object] = {}
    st = _stub_st(cap)
    first = content_feed.MOCK_CONTENT[0]
    monkeypatch.setattr(filters, "st", st)
    monkeypatch.setattr(
        filters, "render_filters", lambda _s, _p: (first["status"], first["source"])
    )
    rendered: list[dict] = []
    monkeypatch.setattr(
        content_card, "render_content_card", lambda c: rendered.append(c)
    )
    content_feed.render_content_feed()
    expected = content_feed.filter_content(
        content_feed.MOCK_CONTENT, first["status"], first["source"]
    )
    assert rendered == expected
