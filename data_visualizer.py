***********CSV File Uploader & Visualizer***************


Install Required Libraries
If not already installed:

pip install streamlit pandas matplotlib

-----------


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📁 Data Visualizer", layout="wide")

st.title("📁 CSV File Uploader & 📈 Data Visualizer")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File successfully uploaded!")

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Column Selection")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if len(numeric_cols) >= 2:
        x_col = st.selectbox("Choose X-axis", numeric_cols)
        y_col = st.selectbox("Choose Y-axis", numeric_cols, index=1)

        if st.button("Generate Plot"):
            fig, ax = plt.subplots()
            ax.plot(df[x_col], df[y_col], marker='o')
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            ax.set_title(f"{y_col} vs {x_col}")
            st.pyplot(fig)
    else:
        st.warning("The uploaded CSV must have at least 2 numeric columns.")
else:
    st.info("📎 Please upload a CSV file to get started.")
