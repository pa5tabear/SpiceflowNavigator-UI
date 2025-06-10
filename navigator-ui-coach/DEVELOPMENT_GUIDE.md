# 🛠️ **Navigator-UI Development Guide**

**Comprehensive technical guide for building SpiceflowNavigator's user interface**

## **🚀 Quick Setup**

### **Prerequisites**
```bash
# Required
python 3.9+
git

# For split repository development
git clone --recursive https://github.com/pa5tabear/SpiceflowNavigator-UI.git
cd SpiceflowNavigator-UI

# For monorepo development (current)
cd SpiceflowNavigator/quickstart/navigator-ui-coach/STARTER_CODE
```

### **Environment Setup**
```bash
# Install dependencies
pip install streamlit plotly altair pandas pytest

# Set environment variables
export RUNPOD_ENDPOINT="your-runpod-endpoint"  # Optional for development

# Test setup
streamlit run app.py
```

---

## **🏗️ Architecture Overview**

### **File Structure**
```
SpiceflowNavigator-UI/
├── app.py                     # Main Streamlit application
├── pages/                     # Multi-page app structure
│   ├── 01_dashboard.py        # RSS feed monitoring
│   ├── 02_analytics.py        # Strategic analysis views
│   ├── 03_search.py           # Content search interface
│   └── 04_settings.py         # Configuration management
├── components/                # Reusable UI components
│   ├── feed_status.py         # Feed status widgets
│   ├── goal_tracker.py        # Goal management UI
│   ├── search_bar.py          # Search interface
│   └── charts.py              # Visualization components
├── utils/                     # Utility functions
│   ├── data_formatting.py     # Data transformation
│   ├── styling.py             # CSS and themes
│   └── state_management.py    # Session state helpers
├── tests/                     # Test suite
│   ├── test_components.py     # Component unit tests
│   ├── test_integration.py    # Integration tests
│   └── test_data_flow.py      # Data pipeline tests
├── common-utils/              # Git submodule (split repo)
│   ├── config.py              # RSS feed configuration
│   └── runpod_client.py       # RunPod API client
├── requirements.txt           # Python dependencies
├── Makefile                   # Development commands
└── README.md                  # Repository documentation
```

### **Technology Stack**

#### **Core Framework**
```python
streamlit==1.28.0              # Web application framework
```

#### **Visualization**
```python
plotly>=5.15.0                 # Interactive charts and graphs
altair>=5.0.0                  # Declarative statistical visualization
```

#### **Data Processing**
```python
pandas>=2.0.0                  # Data manipulation and analysis
numpy>=1.24.0                  # Numerical computations
```

#### **Development & Testing**
```python
pytest>=7.4.0                 # Testing framework
ruff>=0.1.0                    # Code formatting and linting
```

---

## **🎨 UI Development Patterns**

### **1. Multi-Page Application Structure**

```python
# app.py - Main entry point
import streamlit as st

st.set_page_config(
    page_title="SpiceflowNavigator",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Sidebar navigation
    with st.sidebar:
        page = st.selectbox("Navigate to:", [
            "📊 Dashboard",
            "📈 Analytics", 
            "🔍 Search",
            "⚙️ Settings"
        ])
    
    # Route to appropriate page
    if page == "📊 Dashboard":
        show_dashboard()
    # ... other pages

def show_dashboard():
    # Dashboard implementation
    pass
```

### **2. Reusable Component Pattern**

```python
# components/feed_status.py
import streamlit as st

def feed_status_card(feed, success_rate=0.95, articles_today=10):
    """Reusable feed status component"""
    
    with st.container():
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            st.markdown(f"### {feed.name}")
            st.markdown(f"**URL:** {feed.url}")
        
        with col2:
            st.metric("Success Rate", f"{success_rate:.1%}")
        
        with col3:
            st.metric("Articles Today", articles_today)

# Usage in main app
from components.feed_status import feed_status_card

feeds = load_feeds()
for feed in feeds:
    feed_status_card(feed)
```

### **3. State Management Pattern**

```python
# utils/state_management.py
import streamlit as st

def initialize_session_state():
    """Initialize session state variables"""
    if 'user_preferences' not in st.session_state:
        st.session_state.user_preferences = {
            'theme': 'light',
            'refresh_interval': 5,
            'default_page': 'dashboard'
        }
    
    if 'search_history' not in st.session_state:
        st.session_state.search_history = []

def get_preference(key, default=None):
    """Get user preference with fallback"""
    return st.session_state.user_preferences.get(key, default)

def set_preference(key, value):
    """Set user preference"""
    st.session_state.user_preferences[key] = value
```

### **4. Data Integration Pattern**

```python
# Integration with CommonUtils
import sys
from pathlib import Path

# Add CommonUtils to path (for split repository)
if Path("common-utils").exists():
    sys.path.insert(0, str(Path("common-utils").resolve()))

try:
    from config import load_feeds, RSSFeed
    from runpod_client import RunPodClient
    COMMON_UTILS_AVAILABLE = True
except ImportError:
    COMMON_UTILS_AVAILABLE = False
    st.error("CommonUtils not available")

@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_rss_feeds():
    """Load RSS feeds with caching"""
    if COMMON_UTILS_AVAILABLE:
        return load_feeds()
    else:
        # Return mock data for development
        return []
```

---

## **📊 Visualization Patterns**

### **1. Interactive Charts with Plotly**

```python
import plotly.express as px
import plotly.graph_objects as go

def create_feed_performance_chart(feeds_data):
    """Create interactive performance chart"""
    
    fig = px.scatter(
        feeds_data,
        x='success_rate',
        y='articles_per_day',
        size='strategic_importance',
        color='avg_relevance',
        hover_name='name',
        title="RSS Feed Performance Overview"
    )
    
    fig.update_layout(
        xaxis_title="Success Rate",
        yaxis_title="Articles per Day"
    )
    
    return fig

# Usage
chart = create_feed_performance_chart(data)
st.plotly_chart(chart, use_container_width=True)
```

### **2. Real-time Data Updates**

```python
# Auto-refresh pattern
import time

def create_live_dashboard():
    """Dashboard with auto-refresh"""
    
    # Auto-refresh every 30 seconds
    if 'last_refresh' not in st.session_state:
        st.session_state.last_refresh = time.time()
    
    placeholder = st.empty()
    
    while True:
        with placeholder.container():
            # Load fresh data
            data = get_live_feed_data()
            
            # Display metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Active Feeds", data['active_feeds'])
            with col2:
                st.metric("Articles Today", data['articles_today'])
            with col3:
                st.metric("Success Rate", f"{data['success_rate']:.1%}")
        
        time.sleep(30)  # Refresh every 30 seconds
```

### **3. Responsive Design Pattern**

```python
# Responsive layout using columns
def responsive_layout():
    """Create responsive layout for different screen sizes"""
    
    # Different layouts based on screen width
    # Note: Streamlit doesn't have direct screen size detection,
    # but you can use column ratios for responsive behavior
    
    # Desktop layout
    col1, col2, col3 = st.columns([2, 3, 1])
    
    with col1:
        # Sidebar content
        show_feed_list()
    
    with col2:
        # Main content
        show_main_dashboard()
    
    with col3:
        # Status panel
        show_status_panel()
```

---

## **🧪 Testing Strategies**

### **1. Component Testing**

```python
# tests/test_components.py
import pytest
from unittest.mock import Mock, patch

def test_feed_status_card():
    """Test feed status card component"""
    
    # Mock feed data
    mock_feed = Mock()
    mock_feed.name = "Test Feed"
    mock_feed.url = "https://example.com"
    mock_feed.strategic_importance = 5
    
    # Test component (would need Streamlit testing framework)
    # This is a simplified example
    assert mock_feed.name == "Test Feed"
    assert mock_feed.strategic_importance == 5

def test_data_processing():
    """Test data processing separate from UI"""
    
    feeds_data = [
        {"name": "Feed1", "success_rate": 0.95},
        {"name": "Feed2", "success_rate": 0.85},
    ]
    
    avg_success = sum(f["success_rate"] for f in feeds_data) / len(feeds_data)
    assert avg_success == 0.9
```

### **2. Integration Testing**

```python
# tests/test_integration.py
@patch('config.load_feeds')
def test_dashboard_integration(mock_load_feeds):
    """Test dashboard integration with CommonUtils"""
    
    # Mock RSS feeds
    mock_load_feeds.return_value = [
        Mock(name="Feed1", url="http://test1.com", strategic_importance=5),
        Mock(name="Feed2", url="http://test2.com", strategic_importance=3),
    ]
    
    # Test data flow
    feeds = mock_load_feeds()
    assert len(feeds) == 2
    assert feeds[0].name == "Feed1"
```

### **3. Performance Testing**

```python
def test_large_dataset_performance():
    """Test UI performance with large datasets"""
    
    # Generate large dataset
    large_data = [{"id": i, "value": i*2} for i in range(10000)]
    
    import time
    start_time = time.time()
    
    # Simulate data processing
    processed = [item["value"] for item in large_data if item["value"] > 1000]
    
    end_time = time.time()
    
    assert len(processed) > 0
    assert (end_time - start_time) < 1.0  # Should complete quickly
```

---

## **🎨 Styling and Theming**

### **1. Custom CSS**

```python
# utils/styling.py
import streamlit as st

def apply_custom_css():
    """Apply custom CSS for professional styling"""
    
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1f77b4;
            margin-bottom: 1rem;
        }
        
        .metric-card {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 4px solid #1f77b4;
        }
        
        .status-healthy { color: #28a745; }
        .status-warning { color: #ffc107; }
        .status-error { color: #dc3545; }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
    </style>
    """, unsafe_allow_html=True)

# Usage in main app
apply_custom_css()
```

### **2. Theme Management**

```python
def get_theme_config(theme_name):
    """Get theme configuration"""
    
    themes = {
        'light': {
            'background': '#ffffff',
            'text': '#000000',
            'primary': '#1f77b4',
            'success': '#28a745',
            'warning': '#ffc107',
            'error': '#dc3545'
        },
        'dark': {
            'background': '#0e1117',
            'text': '#ffffff',
            'primary': '#ff6b6b',
            'success': '#51cf66',
            'warning': '#ffd43b',
            'error': '#ff6b6b'
        }
    }
    
    return themes.get(theme_name, themes['light'])
```

---

## **🔄 Development Workflow**

### **1. Local Development**

```bash
# Start development server
streamlit run app.py

# Run with auto-reload
streamlit run app.py --server.runOnSave true

# Run on specific port
streamlit run app.py --server.port 8502
```

### **2. Testing Workflow**

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run specific test file
pytest tests/test_components.py -v

# Run tests with live output
pytest tests/ -s
```

### **3. Code Quality**

```bash
# Format code
ruff format .

# Check code quality
ruff check .

# Auto-fix issues
ruff check --fix .
```

---

## **📊 Performance Optimization**

### **1. Caching Strategies**

```python
# Cache expensive computations
@st.cache_data(ttl=600)  # Cache for 10 minutes
def load_feed_data():
    """Load and process feed data"""
    # Expensive operation
    return processed_data

# Cache with dependencies
@st.cache_data(ttl=300)
def get_analytics_data(date_range, filters):
    """Load analytics with dependencies"""
    # Process based on parameters
    return analytics_data
```

### **2. Lazy Loading**

```python
def lazy_load_component():
    """Load component only when needed"""
    
    if st.button("Load Analytics"):
        with st.spinner("Loading analytics..."):
            analytics_data = load_expensive_analytics()
            display_analytics(analytics_data)
```

### **3. Progressive Loading**

```python
def progressive_dashboard():
    """Load dashboard progressively"""
    
    # Load critical data first
    st.subheader("System Status")
    quick_status = get_quick_status()
    display_status(quick_status)
    
    # Load detailed data in background
    with st.spinner("Loading detailed metrics..."):
        detailed_data = get_detailed_metrics()
        display_detailed_metrics(detailed_data)
```

---

## **🔧 Debugging and Troubleshooting**

### **Common Issues**

#### **1. CommonUtils Import Errors**
```bash
# Check submodule status
git submodule status

# Initialize submodules
git submodule update --init --recursive

# Update submodules
git submodule update --remote
```

#### **2. Streamlit Session State Issues**
```python
# Debug session state
st.write("Session State:", st.session_state)

# Clear session state
if st.button("Clear State"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
```

#### **3. Performance Issues**
```python
# Add performance monitoring
import time

start_time = time.time()
# ... expensive operation ...
end_time = time.time()

st.write(f"Operation took {end_time - start_time:.2f} seconds")
```

### **Development Tools**

```bash
# Streamlit diagnostics
streamlit doctor

# Check configuration
streamlit config show

# Clear cache
streamlit cache clear
```

---

## **📦 Deployment Preparation**

### **1. Production Configuration**

```python
# config/production.py
import os

PRODUCTION_CONFIG = {
    'debug': False,
    'auto_refresh': True,
    'cache_ttl': 300,
    'runpod_endpoint': os.getenv('RUNPOD_ENDPOINT'),
    'log_level': 'INFO'
}
```

### **2. Environment Variables**

```bash
# Required for production
RUNPOD_ENDPOINT=https://your-runpod-endpoint.com

# Optional
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### **3. Docker Configuration**

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## **🎯 Best Practices**

### **1. Component Design**
- Keep components small and focused
- Use consistent naming conventions
- Include docstrings and type hints
- Make components reusable across pages

### **2. State Management**
- Minimize use of session state
- Initialize state variables early
- Use caching for expensive operations
- Clear state when appropriate

### **3. Performance**
- Use `@st.cache_data` for data loading
- Implement progressive loading for large datasets
- Optimize chart rendering with appropriate data sampling
- Monitor and profile performance regularly

### **4. Testing**
- Test components independently from UI
- Mock external dependencies
- Use fixtures for common test data
- Test error handling and edge cases

### **5. Documentation**
- Document all public functions
- Include usage examples in docstrings
- Maintain up-to-date README files
- Document configuration options

---

## **🚀 Next Steps**

1. **Start with Feature 1** from the roadmap (Basic Streamlit Multi-Page Application)
2. **Use the starter code** as foundation for your implementation
3. **Follow the sprint template** for structured development
4. **Test early and often** using the provided test patterns
5. **Iterate based on feedback** and user needs

**Happy coding! Build something amazing! 🎉** 