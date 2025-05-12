# AI Research Agent

An intelligent research assistant that combines real-time web search with powerful language models to generate concise research summaries.

## Features

- **Real-time Search**: Powered by Tavily API for up-to-date web results
- **Flexible AI Backend**: Supports both local (Ollama) and cloud-based LLMs (OpenAI, Groq, etc.)
- **Interactive UI**: Streamlit interface for easy use and result visualization
- **Portable Architecture**: Modular design for easy customization

## Deployment Options

### 1. Local Development (Recommended for Ollama Users)
```
pip install -r requirements.txt
streamlit run app.py
```
- **Best for**: Personal use, testing, and development
- **Requirements**:
  - Ollama running locally (`ollama serve`)
  - Tavily API key in environment variables

### 2. Cloud Deployment (For Public Sharing)
```
# Requires switching to cloud-based LLM (OpenAI/Groq/Anthropic)
pip install langchain-openai langchain-groq
```
- **Supported Providers**:
  - OpenAI (`gpt-3.5-turbo` or `gpt-4`)
  - Groq (`mixtral-8x7b-32768`)
  - Anthropic (`claude-3`)

### 3. Temporary Sharing (Local Demo)
```
ngrok http 8501  # Creates public URL for your local instance
```
- **Best for**: Short-term demos and testing
- **Limitations**: Requires keeping your local machine running

## Configuration Guide

1. For **local Ollama usage**:
   - Keep `OLLAMA_URL = "http://localhost:11434"`
   
2. For **cloud deployment**:
   ```
   # In your research_agent.py:
   from langchain_openai import ChatOpenAI
   llm = ChatOpenAI(model="gpt-3.5-turbo")  # Replace with your preferred cloud LLM
   ```

---

This version:
1. Clearly separates local vs cloud use cases
2. Provides specific code examples for different configurations
3. Maintains a professional tone while being technically precise
4. Includes all deployment options with their requirements
