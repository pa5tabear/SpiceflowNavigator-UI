.PHONY: test install dev clean help

help:
	@echo "SpiceflowNavigator-UI Development Commands"
	@echo "================================"
	@echo ""
	@echo "  test     Run tests"
	@echo "  install  Install dependencies + CommonUtils"
	@echo "  dev      Start development server"
	@echo "  clean    Clean temporary files"

test:
	pytest tests/ -v

install:
	pip install -r requirements.txt
	pip install -e ./common-utils/

dev:
	streamlit run app.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
