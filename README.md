
# E-commerce AI Data Q&A Agent

This project is a Streamlit-based web application that lets you ask natural-language questions ("What is my total sales?", "Which product had the highest CPC?", etc.) about your e-commerce business. The AI agent converts your question into an SQL query, fetches data from your database, then displays results, SQL logic, and visualizations—fully interactively.

## Features

- **Ask business questions in plain English**
- **LLM-powered SQL generation:** Converts your questions into SQL automatically
- **Results from your actual database**  
- **Transparent:** Shows the SQL query used and the AI's raw thinking
- **Interactive tables and auto-generated visualizations** (bar, line, and metric charts)
- **Typewriter/streaming effect** for answers

## Demo Screenshot
<img width="635" height="506" alt="image" src="https://github.com/user-attachments/assets/27570d7f-5e9a-440d-8a1f-3b2caaab3fd1" />

| User Question | AI Response |
|---------------|-------------|
| What is my total sales? | SQL: `SELECT SUM(total_sales) FROM total_sales;`<br>Answer: Data and chart displayed |

## Requirements

- **Python 3.8+**
- **Streamlit**
- **Pandas**
- **SQLite** (your data in a `.db` file, e.g., `ecom.db`)
- **Ollama** (for running a local LLM, such as `orca-mini`)
- **LLM Model**: `orca-mini` (recommended for low-memory devices)

## Project Folder Structure
<img width="390" height="526" alt="image" src="https://github.com/user-attachments/assets/91f0f193-cfe6-472c-84d7-4fd8998848a3" />


## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ecom-ai-agent.git
cd ecom-ai-agent
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate          # On Linux/Mac
venv\Scripts\activate             # On Windows
```
### 3. Install Python Dependencies
```bash
 pip install -r requirements.txt
```
## Typical requirements.txt includes:

# streamlit
# pandas
# sqlite3 (standard with Python, for DB)
# requests (if needed for Ollama API)

### 4. Set Up Your Database
# Place your SQLite DB file (e.g., ecom.db) inside the data/ folder.

# Make sure your tables match the schema used in the agent (see next section).

### 5. Install and Run Ollama (Local LLM)
 Download and install Ollama: https://ollama.com/download

### Pull the recommended model:
```bash
ollama pull orca-mini
```
### Start the Ollama model in a new terminal:
```bash
ollama run orca-mini
```
(Leave this terminal open during app usage.)

## Database Schema Example
# The default database expects tables like:

# -> ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
https://docs.google.com/spreadsheets/d/1ZATJteA4sU7DXN-fqJxG8Td_Nwif5QB2fTQvGK8LegY/edit?usp=sharing

# -> total_sales(date, item_id, total_sales, total_units_ordered)
https://docs.google.com/spreadsheets/d/1ftXt9Z6uEXUMlIHSZK0CR2kLlNZyj8TUi4lQmMF6qWo/edit?usp=sharing

# -> eligibility(eligibility_datetime_utc, item_id, eligibility, message)
https://docs.google.com/spreadsheets/d/1Loc32KsHwEGhLAahSfMA6t1aZdEvxJIPADxpdzZEZTw/edit?gid=95626969#gid=95626969

# Modify or initialize your DB accordingly.

### How to Run the App

### 1.Start Ollama and the orca-mini model (in one terminal):

```bash
ollama run orca-mini
```
### 2.Run the Streamlit app (in a new terminal):

```bash
streamlit run frontend/streamlit_app.py
```
## Open your browser:
Visit http://localhost:8501
## Ask questions in the input box and see answers, SQL logic.

