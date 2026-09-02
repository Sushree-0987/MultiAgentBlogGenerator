# 🤖 Multi-Agent Blog Generator

An AI-powered Multi-Agent Blog Generator built using **LangGraph, LangChain, Groq, and Streamlit**.

The system uses multiple AI agents to generate a structured and professional blog from a user-provided topic. Each agent is responsible for a specific stage of the blog generation process.

---

## 📌 Project Overview

Writing a high-quality blog usually involves multiple steps such as planning, research, content writing, and editing.

Traditional AI blog generators often try to generate the entire blog using a single prompt, which can result in:

- Poor content structure
- Repetitive information
- Weak readability
- Inconsistent content
- Limited control over the generation process

This project solves this problem by dividing the blog-generation process into multiple AI agents that work together through a structured workflow.

---

## ✨ Features

- 🧠 AI-powered blog generation
- 📋 Automatic blog planning and outline generation
- 🔎 Research-based content generation
- ✍️ AI-powered blog writing
- 🔄 Multi-agent workflow using LangGraph
- ⚡ Fast LLM inference using Groq
- 🖥️ User-friendly Streamlit interface
- 📄 Blog generation and PDF support
- 🔐 API key protection using environment variables

---

## 🏗️ System Architecture

```text
                 ┌─────────────────┐
                 │   User Topic    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Planner Agent  │
                 │                 │
                 │ Creates outline │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Research Agent  │
                 │                 │
                 │ Provides useful │
                 │ research data   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Writer Agent   │
                 │                 │
                 │ Generates blog  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Final Blog    │
                 └─────────────────┘