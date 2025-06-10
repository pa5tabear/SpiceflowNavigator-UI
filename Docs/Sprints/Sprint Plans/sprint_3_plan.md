---
number:          3
title:           "Real-time Agent Dashboard Foundation"
goal:            "Implement real-time agent status indicators and basic content feed structure"
timebox_minutes: 60          # wall-clock limit Codex may spend
loc_budget:      120         # net new/changed lines allowed
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_realtime_foundation"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 3 · Real-time Agent Dashboard Foundation

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

**Goal**: Implement real-time agent status indicators and basic content feed structure

**Why now**: Establishes foundation for world-class content intelligence dashboard with live agent communication - core to SpiceflowNavigator's 4-Agent Architecture vision.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|------------------------|-----------------------------------|
| 1 | Create real-time status bar with agent indicators | Status bar shows Navigator-Ingest/Strategy/Pipeline status; `pytest -k test_realtime_foundation` green |
| 2 | Build basic content feed structure | Content feed displays placeholder cards with status indicators and real-time updates |
| 3 | Implement WebSocket connection foundation | WebSocket client connects to mock agent events; status updates trigger UI changes |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|------------|--------------|------------------|
| `src/ui/status_bar.py` | Real-time status indicators | Agent status data → Status badge UI |
| `src/ui/content_feed.py` | Content feed with live updates | Content items → Interactive feed cards |
| `src/websocket/client.py` | WebSocket connection handler | Agent events → UI state updates |
| `src/ui/dashboard.py` | Updated with status bar integration | Navigation → Dashboard with live status |

## 4 · Success Metrics (CI-Enforced)

- Green CI badge for branch `sprint-3`
- `scripts/ci/check_loc_budget.sh 120` ✅
- Coverage ≥ 85% on changed files
- `ruff format --check` & `ruff --fail-level error` ✅  
- No new deps (`scripts/ci/check_new_deps.sh`) ✅
- Golden-Path script passes iff `require_golden_path = false`

## 5 · Codex Workflow (MUST follow)

1. Think privately (outline in comments)
2. Add failing test matching `test_realtime_foundation`
3. Implement code to pass test within `loc_budget`
4. Run all CI checks locally
5. Self-Review Checklist (below)
6. Open PR to `sprint-3` branch

### Self-Review Checklist (5-point)
☐ All tests green locally  
☐ No binary files, no new deps  
☐ LOC delta ≤ 120  
☐ Docs updated only for shipped features  
☐ Commit message begins `feat(s3):` or `fix(s3):`  

(Fail → iterate once, else open PR.)

## 6 · Guard-Rails & Refusals

- Repo uses linear history & merge-queue – Codex must respect
- Hard-refuse tasks that violate guard-rails; respond `REFUSE: <reason>`
- Root-cause analysis file `Docs/Sprints/RCAs/rca_s3.md` is mandatory if CI fails at any point

## 7 · Post-Sprint Review Hooks (for Cursor)

- Cursor will create `sprint_3_review.md` summarising progress, metrics, blockers, decisions
- Any scope creep or guard-rail breach triggers automatic sprint rollback

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ↑ • ✅ No guard-rail hits • ✅ Honest docs

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 