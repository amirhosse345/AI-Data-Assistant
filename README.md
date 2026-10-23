
# AI-Data-Assistant

A beginner-friendly AI agent project built with Python and the OpenAI API.

## About the Project

AI-Data-Assistant answers questions about sales data by using Python functions and AI-powered function calling.

## Features

- Calculate total sales across all products.
- Find the product with the highest sales.
- Calculate sales for a specific product category.
- Use OpenAI function calling to connect the AI model with Python tools.

## Technologies

- Python
- Pandas
- OpenAI API
- Function Calling

## Project Structure

- `agent.py` — Connects the AI model with Python tools.
- `tools.py` — Contains the sales analysis functions.
- `main.py` — Main Python script.
- `data/sales.csv` — Sample sales dataset.
- `.gitignore` — Excludes private and temporary files.

## Setup

Install the required packages:

    pip install openai pandas python-dotenv

Create a `.env` file and add your OpenAI API key:

    OPENAI_API_KEY=your_api_key_here

Run the agent from the project directory:

    python agent.py

A valid OpenAI API key with available API credits is required to make AI requests.

## Learning Goals

This project is part of my journey toward becoming an AI engineer. I am learning Python, function calling, and how to connect AI models with real Python functions.

## Project Status

Work in progress.
