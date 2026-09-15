#use as note taking application - to create streamlit application #streamlit run home.py
import streamlit as st 

st.title("Day 2")
st.header("Application")
st.write ("streamlit run home.py")
st.write ("Step 1. Create hom.py file, using 'touch home.py in the terminal")
st.write("Step 2. Run streamlit webserver, using streamlit run home.py in the terminal")

#1. allow user to upload a document 
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

#2. allow user to chunck the document 

#3. save each chuck of the document - to your project directory

#4. reads the first chunk you have saved and stores it in a variable

#5. displays the first chunk back to the user