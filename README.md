# AI Business Intelligence Assistant

A simple AI-powered data analysis tool that allows users like me or anyone to upload a dataset and extract insights using natural language queries.

This project explores how large language models can assist in understanding structured data without requiring complex SQL queries or manual analysis.

---

## Overview

The goal of this project was to build a lightweight business intelligence assistant that can:

- Accept a CSV dataset
- Display a quick preview of the data
- Allow users to ask questions in plain English
- Generate meaningful insights using an LLM

Instead of traditional dashboards, this approach focuses on **conversational data analysis**, making it more intuitive for non-technical users.

---

## Features

- Upload CSV files directly through the UI  
- Instant dataset preview  
- Natural language querying  
- AI-generated insights based on dataset context  
- Fast responses using Groq-hosted models  

---

## Tech Stack

- **Python**
- **Streamlit** (for UI)
- **Pandas** (for data handling)
- **Groq API (LLaMA 3.1)** for inference
- **python-dotenv** for environment management  

---

## How It Works

1. You upload your CSV file  
2. The app reads the dataset using Pandas  
3. A sample of the dataset (first 20 rows) is passed into the prompt  
4. You just enter a question  
5. The LLM analyzes the data sample and generates insights  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd AI-business-intelligence-assistant


