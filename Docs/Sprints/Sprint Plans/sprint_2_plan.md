# Sprint 2 · UI Foundation Bootstrap

## 1 · Sprint Goal (≤25 words)
Create minimal Streamlit app with basic UI structure and test foundation for SpiceflowNavigator dashboard.

## 2 · Deliverables & Acceptance Criteria
**Task 1**: Create basic Streamlit app entry point  
• `app.py` renders "SpiceflowNavigator UI" with sidebar navigation  
• Unit test validates app loads without errors  

**Task 2**: Establish test infrastructure  
• Create `tests/` directory with `test_app.py`  
• Tests run green in CI pipeline  

**Task 3**: Add basic dashboard layout  
• Main area displays placeholder dashboard components  
• Navigation sidebar shows Goals, Results, Settings sections  

## 3 · Time-box & LOC Budget
**Duration**: 60 minutes  
**LOC Budget**: ≤120 net LOC across ≤4 files  
**Files**: `app.py`, `tests/test_app.py`, `src/ui/dashboard.py`, `src/ui/__init__.py`

## 4 · Workflow
1. **Think**: Review Streamlit patterns and UI requirements  
2. **Plan**: Outline component structure and test approach  
3. **Code**: Implement minimal viable UI with navigation  
4. **Test**: Write unit tests and verify CI passes locally  

## 5 · Self-Review Rubric
☐ All tests pass locally with `pytest tests/ -v`  
☐ Streamlit app runs without errors via `streamlit run app.py`  
☐ LOC count ≤120 across target files  
☐ No new dependencies added to requirements.txt  
☐ Commit message format: `feat(s2): description`  

## 6 · Proposed Next Sprint
Sprint 3: Goal management interface with CRUD operations for user goals. 