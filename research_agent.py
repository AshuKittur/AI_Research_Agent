import os
import requests
from textwrap import dedent

# Initialize Ollama
from langchain_ollama import OllamaLLM
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Configure Ollama model with the local URL
llm = OllamaLLM(model="llama2", api_url="http://localhost:11434")
os.environ["TAVILY_API_KEY"] = "Your-API-Key"

# Tavily search
def tavily_search(query):
    headers = {"Authorization": f"Bearer {os.getenv('TAVILY_API_KEY')}"}
    params = {
        "query": query,
        "search_depth": "advanced",
        "include_answers": True,
        "include_raw_content": False,
        "max_results": 5
    }
    response = requests.post("https://api.tavily.com/search", headers=headers, json=params)
    return response.json()

# Format results
def format_research_results(results):
    formatted = []
    if 'answer' in results and results['answer']:
        formatted.append(f"## Tavily Summary\n{results['answer']}\n")
    for item in results.get('results', []):
        formatted.append(dedent(f"""
        - **Title**: {item.get('title', 'N/A')}
          **URL**: [{item.get('url', 'N/A')}]({item.get('url', 'N/A')})
          **Content**: {item.get('content', 'N/A')[:200]}...
          **Relevance Score**: {item.get('score', 0):.2f}
        """))
    return "\n".join(formatted)

# Setup prompt
prompt = PromptTemplate(
    input_variables=["research_results"],
    template="""
You are an expert research analyst. Based on the following research results:
{research_results}
Please provide a well-structured response with these sections:
1. Key Findings (bullet points)
2. Detailed Analysis (2-3 paragraphs)
3. Top References (formatted as [Title](URL))
Format the response in Markdown for better readability.
"""
)
llm = Ollama(model="llama2", temperature=0.7)
chain = LLMChain(llm=llm, prompt=prompt)

# Final function to be used in app.py
def complete_research(query):
    raw_results = tavily_search(query)
    research_results = format_research_results(raw_results)
    response = chain.invoke({"research_results": research_results})
    formatted_response = (
        response['text']
        .replace('•', '-') 
        .replace('\n\n\n', '\n\n')
    )
    final_output = f"# Research Results: {query}\n\n{formatted_response}"
    return final_output