---
number:          2
title:           "UI Foundation Bootstrap"
goal:            "Create minimal Streamlit app with navigation and test infrastructure"
timebox_minutes: 60          # wall-clock limit Codex may spend
loc_budget:      120         # net new/changed lines allowed
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_ui_foundation"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 2 · UI Foundation Bootstrap

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

**Goal**: Create minimal Streamlit app with navigation and test infrastructure

**Why now**: Establishes foundational UI structure required for all future SpiceflowNavigator dashboard features and user interactions.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|------------------------|-----------------------------------|
| 1 | Create Streamlit app entry point | `pytest -k test_ui_foundation` green; app.py loads without errors |
| 2 | Build navigation sidebar structure | Navigation renders Goals/Results/Settings sections correctly |
| 3 | Establish test infrastructure | tests/ directory created with passing foundation tests |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|------------|--------------|------------------|
| `app.py` | New Streamlit entry point | None → Rendered UI with navigation |
| `tests/test_app.py` | New test suite | None → Test results for UI components |
| `src/ui/dashboard.py` | Dashboard layout module | None → UI component functions |

## 4 · Success Metrics (CI-Enforced)

- Green CI badge for branch `sprint-2`
- `scripts/ci/check_loc_budget.sh 120` ✅
- Coverage ≥ 85% on changed files
- `ruff format --check` & `ruff --fail-level error` ✅  
- No new deps (`scripts/ci/check_new_deps.sh`) ✅
- Golden-Path script passes iff `require_golden_path = false`

## 5 · Codex Workflow (MUST follow)

1. Think privately (outline in comments)
2. Add failing test matching `test_ui_foundation`
3. Implement code to pass test within `loc_budget`
4. Run all CI checks locally
5. Self-Review Checklist (below)
6. Open PR to `sprint-2` branch

### Self-Review Checklist (5-point)
☐ All tests green locally  
☐ No binary files, no new deps  
☐ LOC delta ≤ 120  
☐ Docs updated only for shipped features  
☐ Commit message begins `feat(s2):` or `fix(s2):`  

(Fail → iterate once, else open PR.)

## 6 · Guard-Rails & Refusals

- Repo uses linear history & merge-queue – Codex must respect
- Hard-refuse tasks that violate guard-rails; respond `REFUSE: <reason>`
- Root-cause analysis file `Docs/Sprints/RCAs/rca_s2.md` is mandatory if CI fails at any point

## 7 · Post-Sprint Review Hooks (for Cursor)

- Cursor will create `sprint_2_review.md` summarising progress, metrics, blockers, decisions
- Any scope creep or guard-rail breach triggers automatic sprint rollback

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ↑ • ✅ No guard-rail hits • ✅ Honest docs

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 