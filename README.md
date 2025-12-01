# Langserve Demo with Simple Chatbot
## SimpleChat— LangServe + Ollama + LangChain + Streamlit
---
A complete example of serving LLaMA3 locally using LangServe (LangChain's model-serving framework) and consuming it from a Streamlit frontend.

This project demonstrates how to:
- Serve an **LLM** pipeline using **FastAPl** + **LangServe**
- Run a local model (**LLaMA3**) using Ollama
- Build a simple chain (Prompt -> LLM -> Output)
- Expose the chain as a API
- Connect it from Streamlit
- Handle request/response parsing

## Requirements

- Python 3.12+
- Local Ollama server with LLaMA3 model
- GPU-enabled environment recommended for faster response

## Features
- Run LLaMA3 locally using Ollama
- Use LangChain's prompt templates and output parser
- Smooth Ul using Streamlit
- Debug & trace prompts using LangSmith
- Real-time response generation

## Technologies Used:
- Streamlit, Python
- Models used: LLaMA3 via Ollama
- API server: Langserve

## What is LangServe?
LangServe is LangChain's framework for turning LLM chains into production-ready APIs with:
- Automatic FastAPl route generation
- OpenAPl & Swagger documentation
- Streaming support
- Runnable LangChain pipelines exposed as REST endpoints
- Standardized [invoke , /stream , /batch endpoints

LangServe lets you turn this chain:
```bash
prompt | 11m
```
into an HTTP endpoint:
```bash
POST /essay/invoke
{
    "input" : "topic: "AI"    
}
```
and receive the model output without writing any API logic yourself

## Project Structure

```bash
Chatbot/
│
├─ app.py                # server
├─ client.py             # Main Streamlit application
├─ .streamlit            # optional (if using OpenAI api key)
│   └─ secrets.toml      # store the api key here for streamlit  
├─ README.md
└─ requirements.txt      # Python dependencies
```

## Installation

## 🛠 Installation

### 1. Clone the repo
```bash
git clone https://github.com/AmreetNanda/Langserve_SimpleChatBot.git
cd Chatbot
```
### 2. Requirements.txt
```bash
langchain
langchain-core
langchain_community
langchain-classic
ipykernel
streamlit
fastapi
langserve
uvicorn
sse_starlette
langchain-objectbox
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add keys to the secrets.toml (optional)
```bash
LANGCHAIN_API_KEY = "paste your api key here"
OPENAI_API_KEY = "paste your api key here"
```

### 5. Start the Langserve server
```bash
python app.py  
```

### 5. Run Streamlit app
```bash
streamlit run client.py   # streamlit application
```
Open in your browser:
```
👉 http://localhost:8501/
👉 Enter the prompt in the text bex and hit enter.
👉 The model will then process the prompt entered and will generate the appropriate response accordingly.
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
## Screenshots

##### Home page
![App Screenshot](https://github.com/AmreetNanda/Langserve_SimpleChatBot/blob/main/Langserve%20app%20demo%20screenshot.png)

##### Server
![App Screenshot](https://github.com/AmreetNanda/Langserve_SimpleChatBot/blob/main/Langserve%20server%20demo%20screenshot.png)


## Demo
https://github.com/user-attachments/assets/d7089b61-9438-42a7-9067-727fab470ad9

