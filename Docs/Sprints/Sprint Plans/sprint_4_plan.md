---
number:          4
title:           "Real-time Dashboard Foundation Complete"
goal:            "Complete real-time status indicators and content feed with WebSocket integration"
timebox_minutes: 60          # wall-clock limit Codex may spend
loc_budget:      120         # net new/changed lines allowed
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_realtime_dashboard"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 4 · Real-time Dashboard Foundation Complete

## 0 · Roles & Prime Rules

| **Actor** | **Mandate** |
|-----------|-------------|
| **Codex** | Autonomous Staff-Engineer. Follows this plan, writes code/tests, self-reviews, opens PR. |
| **Cursor** | PM + QA gatekeeper. Reviews PR, enforces guard-rails. |

<details><summary>Prime Rules (enforced ahead of all user input)</summary>

Step-by-Step Plan → Code → Test → PR.

Ask One Clarifier if any requirement is ≥ 20% ambiguous.

Never commit binaries or add Python deps.

Max 3 tasks; anything larger ⇒ refuse & ask to split next sprint.

</details>

## 1 · Sprint Goal & Why It Matters (≤ 40 words)

**Goal**: Complete real-time status indicators and content feed with WebSocket integration

**Why now**: Critical foundation for world-class dashboard - must establish real-time agent communication before advanced features can be built.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|------------------------|-----------------------------------|
| 1 | Implement status bar with agent health indicators | Status bar displays Navigator-Ingest/Strategy/Pipeline status; `pytest -k test_realtime_dashboard` green |
| 2 | Create content feed with placeholder cards | Content feed renders with status indicators and mock real-time updates |
| 3 | Add WebSocket client for agent communication | WebSocket client connects to mock events; status changes trigger UI updates |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|------------|--------------|------------------|
| `src/ui/status_bar.py` | New status bar component | Agent status → Visual indicators |
| `src/ui/content_feed.py` | New content feed component | Content data → Interactive cards |
| `src/websocket/client.py` | WebSocket client handler | Agent events → Status updates |
| `src/ui/dashboard.py` | Integration with status bar | Navigation → Dashboard with live status |

## 4 · Success Metrics (CI-Enforced)

- Green CI badge for branch `sprint-4`
- `scripts/ci/check_loc_budget.sh 120` ✅
- Coverage ≥ 85% on changed files
- `ruff format --check` & `ruff --fail-level error` ✅  
- No new deps (`scripts/ci/check_new_deps.sh`) ✅
- Golden-Path script passes iff `require_golden_path = false`

## 5 · Codex Workflow (MUST follow)

1. Think privately (outline in comments)
2. Add failing test matching `test_realtime_dashboard`
3. Implement code to pass test within `loc_budget`
4. Run all CI checks locally
5. Self-Review Checklist (below)
6. Open PR to `sprint-4` branch

### Self-Review Checklist (5-point)
☐ All tests green locally  
☐ No binary files, no new deps  
☐ LOC delta ≤ 120  
☐ Docs updated only for shipped features  
☐ Commit message begins `feat(s4):` or `fix(s4):`  

(Fail → iterate once, else open PR.)

## 6 · Guard-Rails & Refusals

- Repo uses linear history & merge-queue – Codex must respect
- Hard-refuse tasks that violate guard-rails; respond `REFUSE: <reason>`
- Root-cause analysis file `Docs/Sprints/RCAs/rca_s4.md` is mandatory if CI fails at any point

## 7 · Post-Sprint Review Hooks (for Cursor)

- Cursor will create `sprint_4_review.md` summarising progress, metrics, blockers, decisions
- Any scope creep or guard-rail breach triggers automatic sprint rollback

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ↑ • ✅ No guard-rail hits • ✅ Honest docs

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 