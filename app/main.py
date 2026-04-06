from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st
import pandas as pd
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Business Intelligence Assistant")
st.write("Upload a dataset to begin.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Ask Questions About Your Data")
    query = st.text_input("Enter your question")

    if query:
        with st.spinner("Analyzing data..."):
            data_sample = df.head(20).to_string()

            prompt = f"""
You are a data analyst.

Here is a dataset sample:
{data_sample}

Answer the following question based on the data:
{query}

Give a clear, concise insight.
"""

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            st.write(response.choices[0].message.content)
