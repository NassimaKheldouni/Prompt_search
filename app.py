import streamlit as st
import pandas as pd

# Function to filter the table based on keywords
def filter_table(df, keywords):
    filtered_df = df[df.apply(lambda row: any(keyword in str(row) for keyword in keywords), axis=1)]
    return filtered_df

# Function to read Excel file from SharePoint (replace with your SharePoint URL)
def read_excel_from_sharepoint(file_url):
    # Use appropriate method to read the Excel file from SharePoint
    # Example: df = pd.read_excel(file_url)
    # Replace the above line with your SharePoint file reading logic
    df = pd.DataFrame()  # Placeholder for demonstration
    return df

# Main Streamlit app
def main():
    st.title("Search App")

    # Get user input for keywords
    keywords = st.text_input("Enter keywords (comma-separated):")
    keywords = [keyword.strip() for keyword in keywords.split(',')]

    # Read Excel file from SharePoint (replace with your SharePoint URL)
    sharepoint_url = "https://your-sharepoint-url.com/your-excel-file.xlsx"
    df = read_excel_from_sharepoint(sharepoint_url)

    # Filter the table based on keywords
    if keywords:
        filtered_df = filter_table(df, keywords)
        st.write("Filtered Table:")
        st.write(filtered_df)
    else:
        st.warning("Please enter keywords to search.")

if __name__ == "__main__":
    main()
