---
number:          6
title:           "Enhanced Content Feed Implementation"
goal:            "Build interactive content feed with filtering and mock data integration"
timebox_minutes: 60          # wall-clock limit Codex may spend
loc_budget:      120         # net new/changed lines allowed
coverage_min:    85          # pytest --cov fail-under
test_pattern:    "test_content_feed"   # pytest -k filter for this sprint
template_version: 2.0 (2025-06-08)
require_golden_path: false
---

# Sprint 6 · Enhanced Content Feed Implementation

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

**Goal**: Build interactive content feed with filtering and mock data integration - DEMO-READY deliverable

**Why now**: Leverages Sprint 5 foundation success to create tangible, demo-able dashboard that showcases world-class content intelligence capabilities.

## 2 · Tasks ("Rule of Three")

| # | Task Name (imperative) | Acceptance Criteria (autotested) |
|---|------------------------|-----------------------------------|
| 1 | Create content feed component with rich mock data | Content feed displays 10+ realistic content cards with titles, sources, timestamps; `pytest -k test_content_feed` green |
| 2 | Add interactive filtering controls | Filter dropdowns for status/source work immediately, showing filtered results in real-time |
| 3 | Create compelling demo dashboard | Goals section shows polished content feed ready for stakeholder demonstration |

## 3 · Interfaces Changed / Added
(append only; one row per file or endpoint)

| File / API | Brief Change | Inputs → Outputs |
|------------|--------------|------------------|
| `src/ui/content_feed.py` | New content feed component | Mock data → Filtered content list |
| `src/ui/filters.py` | Basic filter controls | Filter state → Content filtering |
| `src/ui/dashboard.py` | Goals section integration | Navigation → Content feed display |
| `tests/test_content_feed.py` | Content feed tests | Test functions → Feed functionality validation |

## 4 · Success Metrics (CI-Enforced)

- Green CI badge for branch `sprint-6`
- `scripts/ci/check_loc_budget.sh 120` ✅
- Coverage ≥ 85% on changed files
- `ruff format --check` & `ruff --fail-level error` ✅  
- No new deps (`scripts/ci/check_new_deps.sh`) ✅
- Golden-Path script passes iff `require_golden_path = false`

## 5 · Codex Workflow (MUST follow)

1. Think privately (outline in comments)
2. Add failing test matching `test_content_feed`
3. Implement code to pass test within `loc_budget`
4. Run all CI checks locally
5. Self-Review Checklist (below)
6. Open PR to `sprint-6` branch

### Self-Review Checklist (5-point)
☐ All tests green locally  
☐ No binary files, no new deps  
☐ LOC delta ≤ 120  
☐ Docs updated only for shipped features  
☐ Commit message begins `feat(s6):` or `fix(s6):`  

(Fail → iterate once, else open PR.)

## 6 · Guard-Rails & Refusals

- Repo uses linear history & merge-queue – Codex must respect
- Hard-refuse tasks that violate guard-rails; respond `REFUSE: <reason>`
- Root-cause analysis file `Docs/Sprints/RCAs/rca_s6.md` is mandatory if CI fails at any point

## 7 · Post-Sprint Review Hooks (for Cursor)

- Cursor will create `sprint_6_review.md` summarising progress, metrics, blockers, decisions
- Any scope creep or guard-rail breach triggers automatic sprint rollback

## 8 · Celebration Criteria 🎉

**Success** = ✅ CI green • ✅ Coverage ↑ • ✅ No guard-rail hits • ✅ Honest docs

Anything else = re-scope next sprint.

---
**End of Sprint-Plan Template v2.0**  
*(If this template and a future command ever conflict, the template wins.)* 