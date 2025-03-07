import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Streamlit App Setup
st.set_page_config(page_title="🧹 File Cleaner", layout="wide")
st.title("🧹 File Converter & Data Cleaning")
st.write("Easily convert files between CSV & Excel formats with built-in data cleaning and visualization tools!")

# File uploader
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read file based on extension
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error reading {file.name}: {str(e)}")
            continue

        # Display file details
        file_size = file.getbuffer().nbytes / 1024  # Convert bytes to KB
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file_size:.2f} KB")

        # Show Data Preview
        st.write("### 🔍 Data Preview")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox(f"Enable Cleaning for {file.name}"):

            # Remove Duplicates & Fill Missing Values
            if st.button(f"Clean Data for {file.name}"):
                initial_rows = df.shape[0]
                df.drop_duplicates(inplace=True)
                numeric_cols = df.select_dtypes(include=['number']).columns
                categorical_cols = df.select_dtypes(include=['object']).columns

                if len(numeric_cols) > 0:
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

                if len(categorical_cols) > 0:
                    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

                cleaned_rows = df.shape[0]
                st.write(f"✅ Cleaning Complete! Rows reduced from {initial_rows} to {cleaned_rows}.")
        
        # Column Selection
        st.subheader("📌 Select Columns")
        selected_columns = st.multiselect(f"Select columns for {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Charts for {file.name}"):
            numeric_cols = df.select_dtypes(include=['number']).columns
            if len(numeric_cols) > 0:
                st.bar_chart(df[numeric_cols])
            else:
                st.write("⚠ No numeric columns available for visualization.")

        # File Conversion
        st.subheader("📂 Convert & Download")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            new_ext = ".csv" if conversion_type == "CSV" else ".xlsx"
            new_file_name = file.name.replace(file_ext, new_ext)

            try:
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    mime_type = "text/csv"
                else:
                    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False)
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)

                st.download_button(
                    label=f"📥 Download {new_file_name}",
                    data=buffer,
                    file_name=new_file_name,
                    mime=mime_type
                )
                st.success(f"🎉 {file.name} successfully converted to {conversion_type}!")
            except Exception as e:
                st.error(f"❌ Error converting file: {str(e)}")

    st.success("✅ All files processed successfully!")
