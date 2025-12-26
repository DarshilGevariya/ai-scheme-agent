# Voice-First Agentic AI for Government Scheme Assistance (Hindi)

## Overview
This project implements a **voice-first, agentic AI system** that assists users in identifying and applying for **Indian government/public welfare schemes**, operating **end-to-end in Hindi**.

The system demonstrates **autonomous reasoning, planning, tool usage, memory, and failure handling**.  
All interactions are **voice-based** using a **native Indian language (Hindi)**.

---

## Key Features
- 🎙️ Voice-first interaction (STT → LLM → TTS)  
- 🗣️ Native Hindi reasoning  
- 🤖 Planner–Executor–Evaluator agentic workflow  
- 🛠️ Eligibility & scheme retrieval tools  
- 🔁 Multi-turn conversation memory  
- ⚠️ Failure and contradiction handling  
- 💻 Fully local and free (no paid APIs)

---

## System Architecture

1. **Speech-to-Text (STT)** converts Hindi voice input into text  
2. **LLM** performs reasoning and planning in Hindi  
3. **Tools** evaluate eligibility and retrieve applicable schemes  
4. **Agent Evaluator** validates results and handles failures or contradictions  
5. **Text-to-Speech (TTS)** responds back to the user in Hindi  

---

## Setup Instructions

1. Install **Ollama** and pull the `llama3` model  
2. Install Python dependencies using `requirements.txt`  
3. Run the application:
   ```bash
   python app.py
