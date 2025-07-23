import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.agent import process_question

st.title("🛍️ E-commerce Data Q&A Agent")
user_q = st.text_input("💬 Ask a data question:")

if user_q:
    with st.spinner("Thinking..."):
        # Updated: Get both the result (answer) and the SQL query string
        answer, sql_query = process_question(user_q)

    # ✅ Display the SQL query used
    st.markdown("### 🧾 SQL Query Used:")
    st.code(sql_query, language="sql")

    # ✅ Show live-typing answer output
    st.markdown("### ✅ Result:")
    for line in answer.split('\n'):
        st.write(line)
        time.sleep(0.2)
