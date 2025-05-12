import streamlit as st
import time
from research_agent import complete_research

api_key = st.secrets["TAVILY_API_KEY"]

# App Configuration
st.set_page_config(
    page_title="Research Agent Pro",
    page_icon="🔍",
    layout="wide"
)

# for styling
st.markdown("""
    <style>
    .main {background-color: #f5f5f5;}
    .stButton>button {background-color: #4CAF50; color: white;}
    .stTextInput>div>div>input {border: 1px solid #4CAF50;}
    .report-title {font-size: 24px; color: #333333; text-align: center;}
    </style>
    """, unsafe_allow_html=True)

# Header with Image
st.image("https://image-optimizer.cyberriskalliance.com/unsafe/992x0/https://files.cyberriskalliance.com/wp-content/uploads/2025/03/031425_ai_agents.jpg", use_container_width=True)
st.markdown('<p class="report-title">Advanced Research Assistant using Ollama + LangChain</p>', unsafe_allow_html=True)

# Main Content
col1, col2 = st.columns([3, 1])

with col1:
    query = st.text_area(
        "Enter your research question:",
        placeholder="e.g., What are the latest breakthroughs in renewable energy?",
        height=100
    )

with col2:
    st.write("")  # Spacer
    st.write("")  # Spacer
    if st.button("🔍 Generate Research Summary", use_container_width=True):
        if not query:
            st.warning("Please enter a research question")
        else:
            with st.spinner("🧠 Analyzing research papers..."):
                progress_bar = st.progress(0)
                
                # Simulate progress
                for percent_complete in range(100):
                    time.sleep(0.01)  # Simulate processing time
                    progress_bar.progress(percent_complete + 1)
                
                result = complete_research(query, api_key)
                progress_bar.empty()
                
                # Results Section
                st.markdown("## 📝 Research Summary")
                st.success("Here are your research findings:")
                
                with st.expander("Detailed Analysis", expanded=True):
                    st.markdown(result)
                
                # Add some visual separation
                st.markdown("---")
                
                # Download option
                st.download_button(
                    label="📥 Download Summary",
                    data=result,
                    file_name="research_summary.md",
                    mime="text/markdown"
                )

# Sidebar for additional options
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    research_depth = st.select_slider(
        "Research Depth",
        options=["Brief", "Standard", "Comprehensive"]
    )
    
    st.markdown("## ℹ️ About")
    st.info("This tool uses Ollama and LangChain to analyze research papers and generate summaries.")
