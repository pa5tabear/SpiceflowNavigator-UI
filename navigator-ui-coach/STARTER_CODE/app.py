"""
SpiceflowNavigator UI - Main Application Entry Point

This is the starter code for the Navigator-UI agent. It demonstrates:
- Multi-page Streamlit application structure
- CommonUtils integration for RSS feed configuration
- Basic styling and navigation patterns
- Error handling and loading states

Usage:
    streamlit run app.py
"""

import streamlit as st
from pathlib import Path
import sys

# Add CommonUtils to path (for development in split repository)
if Path("common-utils").exists():
    sys.path.insert(0, str(Path("common-utils").resolve()))

try:
    from config import load_feeds, RSSFeed
    from runpod_client import RunPodClient
    COMMON_UTILS_AVAILABLE = True
except ImportError:
    COMMON_UTILS_AVAILABLE = False
    st.error("⚠️ CommonUtils not available. Make sure submodule is initialized: `git submodule update --init --recursive`")

# Configure Streamlit page
st.set_page_config(
    page_title="SpiceflowNavigator",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .metrics-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .status-indicator {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
    }
    .status-healthy { background-color: #28a745; }
    .status-warning { background-color: #ffc107; }
    .status-error { background-color: #dc3545; }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application entry point"""
    
    # Sidebar navigation
    with st.sidebar:
        st.title("🌊 SpiceflowNavigator")
        st.markdown("---")
        
        # Navigation menu
        page = st.selectbox(
            "Navigate to:",
            [
                "📊 Dashboard",
                "📈 Analytics", 
                "🔍 Search",
                "⚙️ Settings"
            ]
        )
        
        st.markdown("---")
        
        # System status in sidebar
        if COMMON_UTILS_AVAILABLE:
            st.markdown("### System Status")
            st.markdown("✅ CommonUtils: Connected")
            
            # Show feed count
            try:
                feeds = load_feeds()
                st.markdown(f"📡 RSS Feeds: {len(feeds)} configured")
            except Exception as e:
                st.markdown("⚠️ RSS Config: Error loading")
                
        else:
            st.markdown("### System Status")
            st.markdown("❌ CommonUtils: Not available")
    
    # Main content area
    if page == "📊 Dashboard":
        show_dashboard()
    elif page == "📈 Analytics":
        show_analytics()
    elif page == "🔍 Search":
        show_search()
    elif page == "⚙️ Settings":
        show_settings()

def show_dashboard():
    """RSS Feed Status Dashboard"""
    st.markdown('<h1 class="main-header">📊 RSS Feed Dashboard</h1>', unsafe_allow_html=True)
    
    if not COMMON_UTILS_AVAILABLE:
        st.error("CommonUtils required for dashboard functionality")
        return
    
    try:
        # Load RSS feeds from configuration
        feeds = load_feeds()
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Feeds", len(feeds))
        
        with col2:
            # Mock healthy feeds (in real implementation, this would check actual status)
            healthy_count = len([f for f in feeds if f.strategic_importance >= 3])
            st.metric("Healthy Feeds", healthy_count)
        
        with col3:
            # Mock average importance
            avg_importance = sum(f.strategic_importance for f in feeds) / len(feeds) if feeds else 0
            st.metric("Avg. Importance", f"{avg_importance:.1f}")
        
        with col4:
            st.metric("Last Updated", "2 minutes ago")
        
        st.markdown("---")
        
        # Feed details table
        st.subheader("Feed Details")
        
        for feed in feeds:
            with st.expander(f"📡 {feed.name} (Importance: {feed.strategic_importance})"):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(f"**URL:** {feed.url}")
                    st.write(f"**Strategic Importance:** {feed.strategic_importance}/5")
                    
                    # Mock status indicators
                    if feed.strategic_importance >= 4:
                        status_html = '<span class="status-indicator status-healthy"></span>Healthy'
                    elif feed.strategic_importance >= 2:
                        status_html = '<span class="status-indicator status-warning"></span>Warning'
                    else:
                        status_html = '<span class="status-indicator status-error"></span>Error'
                    
                    st.markdown(f"**Status:** {status_html}", unsafe_allow_html=True)
                
                with col2:
                    if st.button(f"Refresh {feed.name}", key=f"refresh_{feed.name}"):
                        st.success("Refresh initiated!")
        
    except Exception as e:
        st.error(f"Error loading RSS feeds: {str(e)}")
        st.info("Make sure your RSS configuration file is properly set up.")

def show_analytics():
    """Strategic Analysis and Insights"""
    st.markdown('<h1 class="main-header">📈 Strategic Analytics</h1>', unsafe_allow_html=True)
    
    st.info("🚧 Analytics features coming in Sprint 4-6!")
    
    # Mock analytics preview
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Content Relevance Heatmap")
        st.markdown("*Visualization of content-to-goal relevance scores*")
        st.empty()  # Placeholder for future heatmap
        
    with col2:
        st.subheader("Trending Topics")
        st.markdown("*Emerging themes and patterns*")
        st.empty()  # Placeholder for future trend analysis

def show_search():
    """Semantic Search Interface"""
    st.markdown('<h1 class="main-header">🔍 Semantic Search</h1>', unsafe_allow_html=True)
    
    st.info("🚧 Search features coming in Sprint 6!")
    
    # Mock search interface
    search_query = st.text_input("Search transcribed content:", placeholder="Enter keywords, topics, or questions...")
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.selectbox("Time Range:", ["Last 7 days", "Last 30 days", "Last 3 months", "All time"])
    with col2:
        st.selectbox("Source:", ["All sources", "TechCrunch", "Hacker News", "MIT Technology Review"])
    
    if search_query:
        st.subheader("Search Results")
        st.markdown("*Search functionality will be implemented in Sprint 6*")

def show_settings():
    """Configuration and Settings"""
    st.markdown('<h1 class="main-header">⚙️ Settings</h1>', unsafe_allow_html=True)
    
    # User preferences
    st.subheader("User Preferences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.selectbox("Theme:", ["Light", "Dark", "Auto"])
        st.selectbox("Default Page:", ["Dashboard", "Analytics", "Search"])
        
    with col2:
        st.slider("Refresh Interval (minutes):", 1, 60, 5)
        st.multiselect("Notification Types:", 
                      ["Feed Errors", "Strategic Alerts", "Goal Updates", "System Status"],
                      default=["Feed Errors", "Strategic Alerts"])
    
    # System configuration (read-only for now)
    st.subheader("System Configuration")
    
    if COMMON_UTILS_AVAILABLE:
        try:
            feeds = load_feeds()
            st.success(f"✅ RSS Configuration: {len(feeds)} feeds loaded")
        except Exception as e:
            st.error(f"❌ RSS Configuration: {str(e)}")
    else:
        st.error("❌ CommonUtils: Not available")
    
    # RunPod status
    st.markdown("**RunPod Integration:**")
    import os
    if os.getenv("RUNPOD_ENDPOINT"):
        st.success("✅ RunPod endpoint configured")
    else:
        st.warning("⚠️ RUNPOD_ENDPOINT environment variable not set")

if __name__ == "__main__":
    main() 