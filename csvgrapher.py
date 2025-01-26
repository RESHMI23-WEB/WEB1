import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Custom CSS for gradient background and other styles
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, rgb(234, 0, 255), rgb(173, 230, 251));
        color: black;
    }
    .stButton>button {
        background-color:rgb(76, 175, 167);
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title of the app
st.title("CSV Data Analyzer")

# File uploader for CSV files
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the first few rows of the DataFrame
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Show basic statistics
    st.write("### Basic Statistics")
    st.write(df.describe())

    # Select a column for visualization
    column = st.selectbox("Select a column to visualize", df.columns)

    # Create a histogram of the selected column
    if st.button("Show Histogram"):
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], bins=30, kde=True, color='blue')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        st.pyplot(plt)

    # Create a line chart for numerical columns
    if st.button("Show Line Chart"):
        if pd.api.types.is_numeric_dtype(df[column]):
            plt.figure(figsize=(10, 5))
            plt.plot(df[column], marker='o', linestyle='-', color='green')
            plt.title(f'Line Chart of {column}')
            plt.xlabel('Index')
            plt.ylabel(column)
            st.pyplot(plt)
        else:
            st.warning("Please select a numeric column for the line chart.")

    # Create a bar chart for categorical columns
    if st.button("Show Bar Chart"):
        if df[column].dtype == 'object':
            plt.figure(figsize=(10, 5))
            df[column].value_counts().plot(kind='bar', color='orange')
            plt.title(f'Bar Chart of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')
            st.pyplot(plt)
        else:
            st.warning("Please select a categorical column for the bar chart.")

    # Create a pie chart for categorical columns
    if st.button("Show Pie Chart"):
        if df[column].dtype == 'object':
            fig, ax = plt.subplots(figsize=(10, 5))
            wedges, texts, autotexts = ax.pie(df[column].value_counts(), colors=sns.color_palette("pastel"), autopct='%1.1f%%')
            plt.title(f'Pie Chart of {column}')
            st.pyplot(fig)
        else:
            st.warning("Please select a categorical column for the pie chart.")