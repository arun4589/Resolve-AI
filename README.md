# Resolve AI
# 🚀 Multi-Agent AI System using Google ADK

## 🧠 Overview

This project implements a **fully autonomous multi-agent system** built purely using **Google ADK**. The system takes a **user-defined goal**, plans the steps to accomplish it, executes those steps through an **execution loop**, enriches information via tools, evaluates intermediate results, and finally presents the output.

### ✅ Goal → 🧭 Plan → 🔁 Execute + Enrich + Evaluate → 🏁 Final Output

---

## 🧱 Architecture

|
|    Root Agent (SequentialAgent)
|    ├── 📌 Planner Agent
|    ├── 🔄 Execution Loop Agent (LoopAgent)
|    │ ├── 🧠 Enrichment Agent (Tool-using)
|    │ └── ✅ Evaluator Agent
|    └── 🏁 Final Agent


### Tool Access by Enrichment Agent:
- 🌦️ `get_weather_info`: Fetch current weather for a location
- 🚀 `get_latest_spacex_launch`: Retrieve info about latest crewed SpaceX mission
- 📰 `get_latest_news`: Fetch the latest global news

---

## 🛠️ Key Components

| Component           | Description                                                  |
|--------------------|--------------------------------------------------------------|
| `Planner Agent`     | Converts high-level goal into structured plan steps          |
| `Execution Loop`    | Executes each step, enriches with tools, evaluates results   |
| `Enrichment Agent`  | Uses tools to add relevant real-time context                 |
| `Evaluator Agent`   | Judges the quality and completion of each enriched step      |
| `Final Agent`       | Gathers results and generates the final output               |

---

## 🚀 Example Use Case

> **User Goal**: “Tell me about today’s weather and the latest SpaceX launch”

### System Flow:
1. ✅ **Planner Agent** creates steps: `Check weather`, `Find latest SpaceX launch`
2. 🔄 **Execution Loop** runs:
   - 🧠 **Enrichment Agent** fetches weather and launch info using tools
   - ✅ **Evaluator Agent** confirms completeness and quality
3. 🏁 **Final Agent** compiles and presents a summarized response

---

## 🧬 Technologies Used

- 🧠 **Google ADK**: Framework for building autonomous distributed agent systems
- 🛠️ **Custom Python tools**: Weather, SpaceX, and News APIs

---

## Project structure

```multi_ai_agent/
│
├── resolve_ai/
│   ├── .env               
│   ├── __init__.py          
│   ├── agent.py             
│   │
│   └── subagents/
│       ├── enrichment_agent/ 
|       |           |──__init__.py
|       |           |──agent.py
|       |           |──tools.py
│       ├── evaluator_agent/ 
|       |           |──__init__.py
|       |           |──agent.py
|       |           |──tools.py
│       ├── final_agent/ 
|       |           |──__init__.py
|       |           |──agent.py
|       |         
│       ├── planner_agent/ 
|       |           |──__init__.py
|       |           |──agent.py
|         
│
├
│  
│   
│  
│
├
│                  
│
├                       
├
├── .gitignore                     # Git ignore settings
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```
---

## ▶️ How to Run

1. Clone the repository:
   
   ```git clone https://github.com/your-username/google-adk-agent.git```
   ```cd google-adk-agent```
   
2. Create virtual environment
 ```python -m venv venv```

3. Activate it
# On Windows:
```venv\Scripts\activate```
# On macOS/Linux:
```source venv/bin/activate```

4. Install requirements
  ```pip install -r requirements.txt``

5. Create .env file in same location as in folder structure

6. use appropriate API keys in .env file
   ```GOOGLE_GENAI_USE_VERTEXAI=FALSE```
    ```GOOGLE_API_KEY= Your_google_api_key```
    ```WEATHER_API_KEY=your_weather_api_key```
    ```NEWS_API_KEY=your_news_api_key```
7. run the following command to access the agents(you will get a link in terminal click on that)
``` adk web``
   

   



