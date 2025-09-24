import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title("This is my 1st app using python")
    st.sidebar.title("Upload your file")
    uploaded_file = st.sidebar.file_uploader("upload your own file",type=['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)

            st.sidebar.success("file uploaded successfully")

            st.subheader("data overview")
            st.dataframe(data.head())

            st.subheader("Basic information of the data")

            st.write("The shape of data is", data.shape)

            st.write('Columns in my data', data.columns)

            st.write('missing value',data.isnull().sum())

            st.subheader("I will show some stats")

            st.write(data.describe())

        except: ("it will handle if things go wrong")
    else: 
        pass
if __name__ == "__main__":
    main()
