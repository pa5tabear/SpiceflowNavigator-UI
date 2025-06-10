---
number:          5
title:           "Basic Status Display Foundation"
goal:            "Implement simple status indicators and content cards without real-time features"
timebox_minutes: 60          # wall-clock limit Codex may spend
loc_budget:      120         # net new/changed lines allowed
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_basic_status"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 5 · Basic Status Display Foundation

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

**Goal**: Implement simple status indicators and content cards without real-time features

**Why now**: Break delivery deadlock by simplifying scope - establish basic UI foundation before attempting real-time complexity.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|------------------------|-----------------------------------|
| 1 | Create static status bar with mock agent status | Status bar displays fixed Navigator-Ingest/Strategy/Pipeline indicators; `pytest -k test_basic_status` green |
| 2 | Build basic content card component | Content card displays title, status, and summary with Streamlit components |
| 3 | Integrate status bar into main dashboard | Dashboard shows status bar above existing navigation |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|------------|--------------|------------------|
| `src/ui/status_bar.py` | Static status bar component | None → Fixed status indicators |
| `src/ui/content_card.py` | Basic content card component | Content dict → Formatted card display |
| `src/ui/dashboard.py` | Integration with status bar | Navigation → Dashboard with status header |
| `tests/test_basic_status.py` | Basic status tests | Test functions → Status display validation |

## 4 · Success Metrics (CI-Enforced)

- Green CI badge for branch `sprint-5`
- `scripts/ci/check_loc_budget.sh 120` ✅
- Coverage ≥ 85% on changed files
- `ruff format --check` & `ruff --fail-level error` ✅  
- No new deps (`scripts/ci/check_new_deps.sh`) ✅
- Golden-Path script passes iff `require_golden_path = false`

## 5 · Codex Workflow (MUST follow)

1. Think privately (outline in comments)
2. Add failing test matching `test_basic_status`
3. Implement code to pass test within `loc_budget`
4. Run all CI checks locally
5. Self-Review Checklist (below)
6. Open PR to `sprint-5` branch

### Self-Review Checklist (5-point)
☐ All tests green locally  
☐ No binary files, no new deps  
☐ LOC delta ≤ 120  
☐ Docs updated only for shipped features  
☐ Commit message begins `feat(s5):` or `fix(s5):`  

(Fail → iterate once, else open PR.)

## 6 · Guard-Rails & Refusals

- Repo uses linear history & merge-queue – Codex must respect
- Hard-refuse tasks that violate guard-rails; respond `REFUSE: <reason>`
- Root-cause analysis file `Docs/Sprints/RCAs/rca_s5.md` is mandatory if CI fails at any point

## 7 · Post-Sprint Review Hooks (for Cursor)

- Cursor will create `sprint_5_review.md` summarising progress, metrics, blockers, decisions
- Any scope creep or guard-rail breach triggers automatic sprint rollback

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ↑ • ✅ No guard-rail hits • ✅ Honest docs

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 