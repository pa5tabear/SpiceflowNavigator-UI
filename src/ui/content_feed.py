"""Interactive content feed with filtering."""

from __future__ import annotations
from typing import Iterable
from . import content_card, filters

MOCK_CONTENT: list[dict[str, str]] = [
    {
        "title": f"Article {i}",
        "source": f"Source {i % 3 + 1}",
        "timestamp": f"2025-06-{i:02d}",
        "status": "New" if i % 2 == 0 else "Reviewed",
        "summary": "Lorem ipsum dolor sit amet.",
    }
    for i in range(1, 11)
]


def filter_content(
    items: Iterable[dict[str, str]],
    status: str | None = None,
    source: str | None = None,
) -> list[dict[str, str]]:
    """Return items matching provided status and source."""
    result = []
    for item in items:
        if status and status != "All" and item.get("status") != status:
            continue
        if source and source != "All" and item.get("source") != source:
            continue
        result.append(item)
    return result


def render_content_feed() -> None:
    """Render content feed with filtering controls."""
    statuses = sorted({c["status"] for c in MOCK_CONTENT})
    sources = sorted({c["source"] for c in MOCK_CONTENT})
    status_sel, source_sel = filters.render_filters(statuses, sources)
    filtered = filter_content(MOCK_CONTENT, status_sel, source_sel)
    for item in filtered:
        content_card.render_content_card(item)
