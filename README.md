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

Follow the steps below to run the project locally.

### 1. Clone the repository

git clone <your-repo-link>

cd AI-business-intelligence-assistant

## 2. Set Up Environment Variables

Before running the app, you need to set your API key:

1. In the root of the project, create a file named .env
2. Open .env in a text editor and add your Groq API key like this:

GROQ_API_KEY=your_api_key_here



> **Important:** Do NOT commit this .env file to GitHub. It contains your secret key.

---

## 3. Run the Application

Once your dependencies are installed and your .env file is set:

1. Open a terminal in your project folder.
2. Run the Streamlit app with:

streamlit run app/main.py












